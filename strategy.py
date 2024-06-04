import random
import matplotlib.pyplot as plt

def fibonacci_sequence(n):
    fib_sequence = [1, 1]  # Start with [1, 1] to avoid zero bets
    for i in range(2, n):
        fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])
    return fib_sequence

def roulette_spin():
    options = [-1, 0] + list(range(1, 37))
    weights = [1, 1] + [2] * 36
    return random.choices(options, weights=weights)[0]

def play_roulette(fib_sequence, games):
    total_profit = 0
    total_win = 0
    total_loss = 0
    current_bet_index = 0
    balance_history = []
    not_hit_count = 0

    for i in range(1, games + 1):
        current_bet = fib_sequence[current_bet_index]
        total_bet = current_bet * 2
        profit = 0

        spin_result = roulette_spin()

        if spin_result in range(1, 25):
            profit = total_bet * 2
            total_profit += profit
            total_win += total_bet
            current_bet_index = 0
            not_hit_count = 0
        else:
            total_loss += total_bet
            not_hit_count += 1
            if not_hit_count >= 15:
                current_bet_index = (current_bet_index + 1) % len(fib_sequence)

            if total_loss >= 1000:
                break

        balance_history.append((i, total_profit - total_loss, total_win, total_loss))

    return balance_history

fib_sequence = fibonacci_sequence(100)
games = 10000
balance_history = play_roulette(fib_sequence, games)

x_values = [x[0] for x in balance_history]
y_values = [x[1] for x in balance_history]

plt.plot(x_values, y_values)
plt.xlabel('Number of Games')
plt.ylabel('Balance')
plt.title('Balance over Games')

for x, y, _, _ in balance_history:
    if y < 0:
        plt.scatter(x, y, color='red', marker='x')

plt.savefig('balance_plot.png')
plt.show()

print("Balance History:")
print("Game Number\tTotal Win\tTotal Loss")
for item in balance_history:
    print("{:12}\t{:10}\t{:10}".format(item[0], item[2], item[3]))

with open('balance_history.txt', 'w') as f:
    for item in balance_history:
        f.write("{},{},{}\n".format(item[0], item[2], item[3]))
