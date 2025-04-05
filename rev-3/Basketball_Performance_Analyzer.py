import numpy as np

points = np.array([
    [10, 25, 30, 22, 12, 18, 26, 32, 24, 29],
    [20, 15, 12, 28, 24, 26, 30, 18, 22, 25],
    [35, 30, 32, 40, 28, 34, 29, 31, 26, 37],
    [12, 18, 20, 15, 22, 14, 19, 21, 23, 17],
    [28, 26, 27, 25, 30, 29, 35, 32, 31, 38]
])

avg_points = np.mean(points, axis=1)
total_points = np.sum(points, axis=1)
best_player = np.argmax(total_points)
worst_player = np.argmin(total_points)
exceptional_games = [list(np.where(player > 30)[0] + 1) for player in points]
sorted_indices = np.argsort(total_points)[::-1]

print("Average points per game:")
print(np.round(avg_points, 1).tolist())

print(f"\nBest-performing player: Player {best_player + 1} (Total: {total_points[best_player]} points)")
print(f"Worst-performing player: Player {worst_player + 1} (Total: {total_points[worst_player]} points)")

print("\nGames with scores above 30:")
for i, games in enumerate(exceptional_games):
    if games:
        print(f"Player {i + 1}: Games {games}")

print("\nSorted Players by Total Points:")
for rank, idx in enumerate(sorted_indices, start=1):
    print(f"{rank}. Player {idx + 1} - {total_points[idx]} points")
