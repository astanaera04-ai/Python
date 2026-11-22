import numpy as np


def show(grid):
    for row in grid:
        print(" ".join("#" if cell else "." for cell in row))
    print()

def count_neighbors(grid):
    m, n = grid.shape
    padded = np.pad(grid, 1)
    counts = np.zeros((m, n), dtype=int)

    for dr in (-1, 0, 1):
        for dc in (-1, 0, 1):
            if dr == 0 and dc == 0:
                continue
            counts += padded[1 + dr : 1 + dr + m, 1 + dc : 1 + dc + n]

    return counts


print("=== Бөлім 1 ===")
grid = np.array([[0, 1, 0],
                 [0, 1, 0],
                 [0, 1, 0]])
print(count_neighbors(grid))


def next_generation(grid):
    nb = count_neighbors(grid)
    alive = (nb == 3) | ((grid == 1) & (nb == 2))
    return np.where(alive, 1, 0)


print("\n=== Бөлім 2 ===")
grid = np.array([[0, 1, 0],
                 [0, 0, 1],
                 [1, 1, 1],
                 [0, 0, 0]])
print(next_generation(grid))

blinker = np.array([[0, 0, 0, 0, 0],
                    [0, 0, 1, 0, 0],
                    [0, 0, 1, 0, 0],
                    [0, 0, 1, 0, 0],
                    [0, 0, 0, 0, 0]])
step1 = next_generation(blinker)
show(blinker)
show(step1)
print("Тік күйге оралды ма:", np.array_equal(next_generation(step1), blinker))


# Бөлім 3. Модельдеу
def simulate(grid, steps):
    current = grid.copy()
    population = [int(current.sum())]

    for _ in range(steps):
        current = next_generation(current)
        population.append(int(current.sum()))

    return current, np.array(population)


print("\n=== Бөлім 3 ===")
glider = np.zeros((6, 6), dtype=int)
glider[0, 1] = glider[1, 2] = glider[2, 0] = glider[2, 1] = glider[2, 2] = 1

final_glider, glider_pop = simulate(glider, 4)
show(glider)
show(final_glider)
print(final_glider)
print(glider_pop)


# Бөлім 4. Кездейсоқ әлем
print("\n=== Бөлім 4 ===")
rng = np.random.default_rng(2026)
world = (rng.random((10, 10)) < 0.35).astype(int)

final_world, pop = simulate(world, 10)

print("Популяция:", pop)
print("Бастапқы популяция:", pop[0])
print("10 ұрпақтан кейін:", pop[-1])
print("Популяция ең көп болған ұрпақ:", pop.argmax(), f"({pop.max()} тірі клетка)")

show(final_world)