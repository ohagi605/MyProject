import matplotlib.pyplot as plt
import random

# 8×8の正方形のマス目を用意
grid_size = 8

# ランダムに1つの色を決定
color_choices = ["red", "blue", "green", "yellow", "purple", "orange", "pink", "cyan"]
selected_color = random.choice(color_choices)

# グリッドを作成し、ランダムな場所に色を塗る
grid = [[selected_color if random.random() < 0.5 else "white" for _ in range(grid_size)] for _ in range(grid_size)]

# グリッドの描画
fig, ax = plt.subplots(figsize=(6, 6))

# 色をマス目に適用
for i in range(grid_size):
    for j in range(grid_size):
        ax.add_patch(plt.Rectangle((j, grid_size - 1 - i), 1, 1, color=grid[i][j]))

plt.xlim(0, grid_size)
plt.ylim(0, grid_size)
ax.axis('off')  # 軸と目盛りを非表示にする
plt.gca().set_aspect('equal', adjustable='box')
plt.show()
