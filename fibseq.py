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

        balance_history.append((i, total_profit - total_loss, total_win, total_loss, spin_result, total_bet))

    return balance_history

fib_sequence = fibonacci_sequence(100)
games = 100
balance_history = play_roulette(fib_sequence, games)

# Plot the balance history
x_values = [x[0] for x in balance_history]
y_values = [x[1] for x in balance_history]

plt.plot(x_values, y_values, marker='o')  # Plot the balance history
plt.xlabel('Number of Hands')
plt.ylabel('Balance')
plt.title('Balance over 100 Hands')

# Highlighting losses with red 'x' markers
for x, y, _, _, spin_result, total_bet in balance_history:
    if y < 0:
        plt.scatter(x, y, color='red', marker='x')
    else:
        plt.scatter(x, y, color='green', marker='o')

plt.savefig('balance_plot.png')  # Save the plot as an image
plt.show()

# Print the balance history to the console
print("Balance History:")
print("{:<12} {:<10} {:<10} {:<10} {:<14} {:<9}".format("Hand Number", "Total Win", "Total Loss", "Balance", "Winning Number", "Total Bet"))
for item in balance_history:
    print("{:<12} {:<10} {:<10} {:<10} {:<14} {:<9}".format(item[0], item[2], item[3], item[1], item[4], item[5]))

# Export the balance history to a markdown file
with open('balance_history.md', 'w') as f:
    f.write("| Hand Number | Total Win | Total Loss | Balance | Winning Number | Total Bet |\n")
    f.write("|-------------|-----------|------------|---------|----------------|-----------|\n")
    for item in balance_history:
        f.write("| {:11} | {:9} | {:10} | {:7} | {:14} | {:9} |\n".format(item[0], item[2], item[3], item[1], item[4], item[5]))

# Export the balance history to a text file
with open('balance_history.txt', 'w') as f:
    for item in balance_history:
        f.write("{},{},{},{},{},{}\n".format(item[0], item[2], item[3], item[1], item[4], item[5]))