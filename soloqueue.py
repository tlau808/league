from random import random
import matplotlib.pyplot as plt
spread = 0
history = [0]
winrate = .55
game_count = 200
for i in range(game_count):
    x = random()
    if x < winrate:
        spread += 1
    else:
        spread -=1
    history.append(spread)


expected_spread = round(winrate*game_count-(1-winrate)*game_count)
plt.figure(figsize=(12, 6))
plt.plot(history)
plt.xlabel('Games played')
plt.ylabel('Win/loss spread')
plt.title(f'Expected spread: {expected_spread}')
plt.show()