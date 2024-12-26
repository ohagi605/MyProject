import numpy as np
import random

score = []

# 正規分布に近い形で点数を生成
score += np.random.normal(loc=70, scale=10, size=1000).astype(int).tolist()
score += np.random.normal(loc=70, scale=15, size=200).astype(int).tolist()

s = int(input())
print(int((s - np.mean(score))/np.std(score)*10+50))



