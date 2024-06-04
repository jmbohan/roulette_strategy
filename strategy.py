import random
import matplotlib.pyplot as plt

def fibonacci_sequence(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])
    return fib_sequence

def roulette_spin():
    return random.randint(0, 36)

def play_roulette(fib_sequence, games):
    total_profit = 0
    current_bet_index = 0
    total_loss = 0
    balance_history = []

    for i in range(1, games + 1):
        current_bet = fib_sequence[current_bet_index]
        total_bet = current_bet * 2  # Betting on two streets
        profit = 0

        spin_result = roulette_spin()

        if spin_result in range(1, 25):  # Winning spin
            profit = total_bet * 2  # 2:1 payout
            total_profit += profit
            current_bet_index = 0  # Start over
        else:
            total_loss += total_bet
            if total_loss >= 1000:
                break  # Quit if total loss reaches 1000 units
            current_bet_index = (current_bet_index + 1) % len(fib_sequence)  # Move to next bet in Fibonacci sequence

        if i % 10 == 0 or total_loss >= 1000:  # Record balance every 10 games or when reaching loss limit
            balance_history.append((i * 10, total_profit - total_loss))  # Record the game number and balance

    return balance_history

fib_sequence = fibonacci_sequence(100)  # Generate Fibonacci sequence for up to 100 bets
games = 10000
balance_history = play_roulette(fib_sequence, games)

# Plot the balance history
x_values = [x[0] for x in balance_history]
y_values = [x[1] for x in balance_history]

plt.plot(x_values, y_values)  # Plot the balance history
plt.xlabel('Number of Games')
plt.ylabel('Balance')
plt.title('Balance over 10 Games')

# Highlighting losses with red 'x' markers
for x, y in balance_history:
    if y < 0:
        plt.scatter(x, y, color='red', marker='x')

plt.savefig('balance_plot.png')  # Save the plot as an image
plt.show()

# Print the balance history to the console
print("Balance History:")
print(balance_history)

# Export the balance history to a text file
with open('balance_history.txt', 'w') as f:
    for item in balance_history:
        f.write("%s\n" % str(item))
