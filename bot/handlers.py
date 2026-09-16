import asyncio
import os
from datetime import datetime
import matplotlib.pyplot as plt
from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.exceptions import TelegramBadRequest

from database import StudyDatabase
from keyboards import StudyKeyboards


class Form(StatesGroup):
    waiting_for_subject_name = State()
    waiting_for_daily_goal = State()
    # Жаңа FSM күйлері
    waiting_for_time_slot = State()
    waiting_for_task_desc = State()


class StudyHandlers:
    def __init__(self, db: StudyDatabase):
        self.db = db
        self.router = Router()
        self.active_sessions = {}
        self.register_handlers()

    def register_handlers(self):
        self.router.message(Command("start"))(self.cmd_start)
        self.router.callback_query(F.data == "back_to_menu")(self.back_to_menu)
        self.router.callback_query(F.data == "menu_settings")(self.settings_menu)
        self.router.callback_query(F.data == "set_add_subject")(self.add_subject_start)
        self.router.message(Form.waiting_for_subject_name)(self.add_subject_finish)
        self.router.callback_query(F.data == "set_daily_goal")(self.set_goal_start)
        self.router.message(Form.waiting_for_daily_goal)(self.set_goal_finish)
        self.router.callback_query(F.data == "menu_start")(self.select_subject)
        self.router.callback_query(F.data.startswith("select_"))(self.choose_timer_mode)
        self.router.callback_query(F.data.startswith("mode_"))(self.start_study)
        self.router.callback_query(F.data == "menu_stop")(self.stop_study)
        self.router.callback_query(F.data == "menu_stats")(self.show_stats)
        self.router.callback_query(F.data == "menu_leaderboard")(self.show_leaderboard)
        self.router.callback_query(F.data == "menu_online")(self.show_online_users)

        # Скедуал хендлерлері
        self.router.callback_query(F.data == "menu_schedule")(self.show_schedule)
        self.router.callback_query(F.data == "sched_add")(self.add_schedule_start)
        self.router.message(Form.waiting_for_time_slot)(self.add_schedule_time)
        self.router.message(Form.waiting_for_task_desc)(self.add_schedule_finish)
        self.router.callback_query(F.data == "sched_clear")(self.clear_schedule)

    async def cmd_start(self, message: types.Message):
        await message.answer(
            f"Hi {message.from_user.first_name}! Welcome back to your Advanced YPT Bot 🔥\n"
            "Achieve your goals and climb the leaderboard!",
            reply_markup=StudyKeyboards.get_main_menu()
        )

    async def back_to_menu(self, callback: types.CallbackQuery, state: FSMContext):
        await state.clear()
        await callback.message.edit_text("Main Menu:", reply_markup=StudyKeyboards.get_main_menu())

    async def settings_menu(self, callback: types.CallbackQuery):
        await callback.message.edit_text("⚙️ *Settings Panel*\n\nCustomize your subjects or change your daily target:",
                                         parse_mode="Markdown", reply_markup=StudyKeyboards.get_settings_menu())

    async def add_subject_start(self, callback: types.CallbackQuery, state: FSMContext):
        await state.set_state(Form.waiting_for_subject_name)
        await callback.message.edit_text("📝 Please type the **name of the subject** you want to add:")

    async def add_subject_finish(self, message: types.Message, state: FSMContext):
        subject_name = message.text.strip()
        user_id = message.from_user.id
        if self.db.add_custom_subject(user_id, subject_name):
            await message.answer(f"✅ Subject *'{subject_name}'* successfully added!", parse_mode="Markdown",
                                 reply_markup=StudyKeyboards.get_main_menu())
        else:
            await message.answer("❌ You already have this subject!", reply_markup=StudyKeyboards.get_main_menu())
        await state.clear()

    async def set_goal_start(self, callback: types.CallbackQuery, state: FSMContext):
        await state.set_state(Form.waiting_for_daily_goal)
        await callback.message.edit_text("🎯 How many **hours** do you want to study daily?:")

    async def set_goal_finish(self, message: types.Message, state: FSMContext):
        try:
            hours = int(message.text.strip())
            self.db.set_daily_goal(message.from_user.id, hours)
            await message.answer(f"🎯 Your daily target is set to *{hours} hours*!", parse_mode="Markdown",
                                 reply_markup=StudyKeyboards.get_main_menu())
        except ValueError:
            await message.answer("❌ Please enter a valid number (integer).")
        await state.clear()

    async def select_subject(self, callback: types.CallbackQuery):
        user_id = callback.from_user.id
        if user_id in self.active_sessions:
            await callback.message.edit_text("You are already studying!", reply_markup=StudyKeyboards.get_stop_menu())
            return
        subjects = self.db.get_user_subjects(user_id)
        await callback.message.edit_text("Select a subject to start:",
                                         reply_markup=StudyKeyboards.get_subjects_menu(subjects))

    async def choose_timer_mode(self, callback: types.CallbackQuery):
        subject = callback.data.split("_")[1]
        await callback.message.edit_text(
            f"📚 Subject: *{subject}*\nChoose your timer mode:",
            parse_mode="Markdown",
            reply_markup=StudyKeyboards.get_timer_type_menu(subject)
        )

    async def start_study(self, callback: types.CallbackQuery):
        user_id = callback.from_user.id
        data_parts = callback.data.split("_")
        mode = data_parts[1]
        subject = data_parts[2]
        user_name = callback.from_user.username if callback.from_user.username else callback.from_user.first_name

        self.active_sessions[user_id] = {
            "subject": subject,
            "start_time": datetime.now(),
            "user_name": user_name,
            "mode": mode
        }

        asyncio.create_task(self.update_live_timer(user_id, callback.message))

    async def update_live_timer(self, user_id: int, message: types.Message):
        animation_frames = ["⏳", "⌛️", "🔆", "✨"]
        frame_index = 0

        while user_id in self.active_sessions:
            session = self.active_sessions.get(user_id)
            if not session: break

            elapsed = datetime.now() - session["start_time"]
            total_seconds = int(elapsed.total_seconds())
            current_frame = animation_frames[frame_index % len(animation_frames)]
            frame_index += 1

            if session["mode"] == "pomo":
                remaining = 1500 - total_seconds
                if remaining <= 0:
                    self.active_sessions.pop(user_id, None)
                    self.db.save_session(user_id, session["user_name"], session["subject"],
                                         session["start_time"].strftime("%Y-%m-%d %H:%M:%S"),
                                         datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 1500)
                    try:
                        await message.answer(f"⏰ *Pomodoro finished (25m)!* Time to take a 5-minute break! ☕️",
                                             parse_mode="Markdown")
                        await message.delete()
                    except TelegramBadRequest:
                        pass
                    break
                m, s = divmod(remaining, 60)
                timer_text = f"`{m:02d}:{s:02d}`"
            else:
                h, r = divmod(total_seconds, 3600)
                m, s = divmod(r, 60)
                timer_text = f"`{h:02d}:{m:02d}:{s:02d}`"

            try:
                await message.edit_text(
                    f"{current_frame} *Subject:* {session['subject']}\n"
                    f"⏱ *Time:* {timer_text}\n\n"
                    f"Status: *Deep Focus Mode* 🧠\n"
                    f"_Keep your phone away and do your best!_",
                    parse_mode="Markdown", reply_markup=StudyKeyboards.get_stop_menu()
                )
            except TelegramBadRequest:
                pass
            await asyncio.sleep(10)

    async def stop_study(self, callback: types.CallbackQuery):
        user_id = callback.from_user.id
        if user_id not in self.active_sessions:
            await callback.message.edit_text("No active session.", reply_markup=StudyKeyboards.get_main_menu())
            return

        session = self.active_sessions.pop(user_id)
        start_time = session["start_time"]
        end_time = datetime.now()
        duration = int((end_time - start_time).total_seconds())

        self.db.save_session(user_id, session["user_name"], session["subject"],
                             start_time.strftime("%Y-%m-%d %H:%M:%S"), end_time.strftime("%Y-%m-%d %H:%M:%S"),
                             duration)
        h, r = divmod(duration, 3600)
        m, s = divmod(r, 60)
        await callback.message.edit_text(
            f"🛑 *Session finished!*\n📂 *Subject:* {session['subject']}\n⏱ *Total Time:* {h}h {m}m {s}s\n\nSaved! ☕️",
            parse_mode="Markdown", reply_markup=StudyKeyboards.get_main_menu())

    async def show_stats(self, callback: types.CallbackQuery):
        user_id = callback.from_user.id
        today_str = datetime.now().strftime("%Y-%m-%d")
        rows, daily_goal_hours, today_seconds = self.db.get_stats_data(user_id, today_str)

        stats_text = "📊 *Your Study Dashboard*\n\n"
        total_all = 0
        if not rows:
            stats_text += "No sessions recorded yet.\n"
        else:
            for row in rows:
                subject, total_seconds = row
                total_all += total_seconds
                h, r = divmod(total_seconds, 3600)
                m, _ = divmod(r, 60)
                stats_text += f"🔹 *{subject}:* {h}h {m}m\n"

        h_all, r_all = divmod(total_all, 3600)
        stats_text += f"\n🏆 *Total Time:* {h_all}h {r_all // 60}m\n-------------------------\n"

        today_h, today_r = divmod(today_seconds, 3600)
        stats_text += f"📅 *Today's Focus:* {today_h}h {today_r // 60}m\n"

        if daily_goal_hours > 0:
            percent = min(int((today_seconds / (daily_goal_hours * 3600)) * 100), 100)
            bar = "█" * (percent // 10) + "░" * (10 - (percent // 10))
            stats_text += f"🎯 *Daily Goal:* {daily_goal_hours}h\n📈 *Progress:* [{bar}] {percent}%\n"
        else:
            stats_text += "🎯 *Daily Goal:* Not set.\n"

        weekly_data = self.db.get_weekly_data(user_id)
        days = [d[5:] for d in weekly_data.keys()]
        hours = list(weekly_data.values())

        plt.figure(figsize=(6, 3.5))
        plt.bar(days, hours, color='#3498db', edgecolor='#2980b9', width=0.5)
        plt.title('Weekly Study Progress (Hours)', fontsize=12, fontweight='bold')
        plt.xlabel('Date')
        plt.ylabel('Hours')
        plt.ylim(0, max(hours) + 1 if hours and max(hours) > 0 else 5)
        plt.tight_layout()

        chart_path = f"chart_{user_id}.png"
        plt.savefig(chart_path, dpi=100)
        plt.close()

        try:
            await callback.message.delete()
        except TelegramBadRequest:
            pass

        photo = types.FSInputFile(chart_path)
        await callback.message.answer_photo(photo=photo, caption=stats_text, parse_mode="Markdown",
                                            reply_markup=StudyKeyboards.get_back_button())

        if os.path.exists(chart_path):
            os.remove(chart_path)

    async def show_leaderboard(self, callback: types.CallbackQuery):
        rows = self.db.get_leaderboard()
        leader_text = "🏆 *Global Leaderboard (Top 5 Users)*\n\n"
        medals = ["🥇", "🥈", "🥉", "4️⃣", "5️⃣"]

        if not rows:
            leader_text += "The leaderboard is empty."
        else:
            for i, row in enumerate(rows):
                user_name, total_seconds, user_id = row
                display_name = f"@{user_name}" if user_name else f"User {user_id}"
                is_me = " (You)" if user_id == callback.from_user.id else ""
                leader_text += f"{medals[i]} *{display_name}*{is_me} — {total_seconds // 3600}h {(total_seconds % 3600) // 60}m\n"

        await callback.message.edit_text(leader_text, parse_mode="Markdown",
                                         reply_markup=StudyKeyboards.get_back_button())

    async def show_online_users(self, callback: types.CallbackQuery):
        online_text = "👥 *Live Focus Status (Studying Now) ⚡️*\n\n"

        if not self.active_sessions:
            online_text += "Nobody is studying right now. Be the first one to start! 🚀"
        else:
            for uid, session in self.active_sessions.items():
                elapsed = datetime.now() - session["start_time"]
                h, r = divmod(int(elapsed.total_seconds()), 3600)
                m, _ = divmod(r, 60)
                display_name = f"@{session['user_name']}" if session['user_name'] else f"User {uid}"
                online_text += f"🔥 *{display_name}* — is studying *{session['subject']}* ({h:02d}h {m:02d}m)\n"

        await callback.message.edit_text(online_text, parse_mode="Markdown",
                                         reply_markup=StudyKeyboards.get_back_button())

    # --- NEW SCHEDULE HANDLERS ---
    async def show_schedule(self, callback: types.CallbackQuery):
        user_id = callback.from_user.id
        rows = self.db.get_user_schedule(user_id)

        sched_text = "📅 *Your Daily Schedule (Бір күндік план)*\n\n"
        if not rows:
            sched_text += "Your schedule is empty. Plan your day ahead! 📑"
        else:
            for row in rows:
                time_slot, task_desc = row
                sched_text += f"⏰ *{time_slot}* — {task_desc}\n"

        await callback.message.edit_text(sched_text, parse_mode="Markdown",
                                         reply_markup=StudyKeyboards.get_schedule_menu())

    async def add_schedule_start(self, callback: types.CallbackQuery, state: FSMContext):
        await state.set_state(Form.waiting_for_time_slot)
        await callback.message.edit_text("⏰ Please enter the **time slot** (e.g., `09:00 - 11:00` or `Morning`):",
                                         parse_mode="Markdown")

    async def add_schedule_time(self, message: types.Message, state: FSMContext):
        await state.update_data(time_slot=message.text.strip())
        await state.set_state(Form.waiting_for_task_desc)
        await message.answer(
            "📝 Now type the **task or subject** for this time (e.g., `IELTS Reading practice`, `Math lecture`):",
            parse_mode="Markdown")

    async def add_schedule_finish(self, message: types.Message, state: FSMContext):
        user_data = await state.get_data()
        time_slot = user_data['time_slot']
        task_desc = message.text.strip()
        user_id = message.from_user.id

        self.db.add_schedule_task(user_id, time_slot, task_desc)
        await state.clear()

        await message.answer("✅ Task successfully added to your schedule!", reply_markup=StudyKeyboards.get_main_menu())

    async def clear_schedule(self, callback: types.CallbackQuery):
        user_id = callback.from_user.id
        self.db.clear_user_schedule(user_id)
        await callback.message.edit_text("🗑 Your daily schedule has been completely cleared.",
                                         reply_markup=StudyKeyboards.get_back_button())