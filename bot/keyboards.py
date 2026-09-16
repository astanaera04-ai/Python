from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder

class StudyKeyboards:
    @staticmethod
    def get_main_menu():
        builder = InlineKeyboardBuilder()
        builder.row(
            types.InlineKeyboardButton(text="🚀 Start Study", callback_data="menu_start"),
            types.InlineKeyboardButton(text="👥 Online (⚡️)", callback_data="menu_online")
        )
        builder.row(
            types.InlineKeyboardButton(text="📊 Stats & Chart", callback_data="menu_stats"),
            types.InlineKeyboardButton(text="🏆 Leaderboard", callback_data="menu_leaderboard")
        )
        builder.row(
            types.InlineKeyboardButton(text="📅 My Daily Schedule", callback_data="menu_schedule")
        )
        builder.row(
            types.InlineKeyboardButton(text="⚙️ Settings Panel", callback_data="menu_settings")
        )
        return builder.as_markup()

    @staticmethod
    def get_schedule_menu():
        """Скедуал ішіндегі батырмалар"""
        builder = InlineKeyboardBuilder()
        builder.row(types.InlineKeyboardButton(text="➕ Add Task", callback_data="sched_add"))
        builder.row(types.InlineKeyboardButton(text="🗑 Clear Schedule", callback_data="sched_clear"))
        builder.row(types.InlineKeyboardButton(text="⬅️ Back to Menu", callback_data="back_to_menu"))
        return builder.as_markup()

    @staticmethod
    def get_timer_type_menu(subject):
        builder = InlineKeyboardBuilder()
        builder.row(types.InlineKeyboardButton(text="⏱ Normal Timer", callback_data=f"mode_normal_{subject}"))
        builder.row(types.InlineKeyboardButton(text="🍅 Pomodoro Mode (25m)", callback_data=f"mode_pomo_{subject}"))
        builder.row(types.InlineKeyboardButton(text="⬅️ Back", callback_data="menu_start"))
        return builder.as_markup()

    @staticmethod
    def get_settings_menu():
        builder = InlineKeyboardBuilder()
        builder.row(types.InlineKeyboardButton(text="➕ Add Custom Subject", callback_data="set_add_subject"))
        builder.row(types.InlineKeyboardButton(text="🎯 Set Daily Goal", callback_data="set_daily_goal"))
        builder.row(types.InlineKeyboardButton(text="⬅️ Back to Menu", callback_data="back_to_menu"))
        return builder.as_markup()

    @staticmethod
    def get_subjects_menu(subjects_list):
        builder = InlineKeyboardBuilder()
        for sub in subjects_list:
            builder.row(types.InlineKeyboardButton(text=f"📚 {sub}", callback_data=f"select_{sub}"))
        builder.row(types.InlineKeyboardButton(text="⬅️ Back", callback_data="back_to_menu"))
        return builder.as_markup()

    @staticmethod
    def get_stop_menu():
        builder = InlineKeyboardBuilder()
        builder.row(types.InlineKeyboardButton(text="🛑 Stop Session", callback_data="menu_stop"))
        return builder.as_markup()

    @staticmethod
    def get_back_button():
        builder = InlineKeyboardBuilder()
        builder.row(types.InlineKeyboardButton(text="⬅️ Back to Menu", callback_data="back_to_menu"))
        return builder.as_markup()