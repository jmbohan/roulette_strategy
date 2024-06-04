import random
import matplotlib.pyplot as plt

def custom_fibonacci_sequence():
    fib_sequence = [5, 10]  # Start with [5, 10] to avoid zero bets and skip the second 5
    for i in range(2, 1000):
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
    street1_bet_index = 0
    street2_bet_index = 0
    balance_history = []

    for i in range(1, games + 1):
        street1_bet = fib_sequence[street1_bet_index]
        street2_bet = fib_sequence[street2_bet_index]

        total_bet = street1_bet + street2_bet
        profit = 0

        spin_result = roulette_spin()

        if spin_result in range(1, 13):  # Street 1 win
            profit = street1_bet * 11
            street1_bet_index = 0  # Reset the Fibonacci sequence for Street 1
        elif spin_result in range(13, 25):  # Street 2 win
            profit = street2_bet * 11
            street2_bet_index = 0  # Reset the Fibonacci sequence for Street 2
        else:  # Loss
            if street1_bet_index < len(fib_sequence) - 1:
                street1_bet_index += 1
            if street2_bet_index < len(fib_sequence) - 1:
                street2_bet_index += 1

        total_profit += profit - total_bet
        total_win += profit
        total_loss += total_bet

        win = profit
        loss = total_bet

        balance_history.append((i, total_profit, total_win, total_loss, spin_result, total_bet, street1_bet, street2_bet, win, loss))

        if total_loss >= 1000:
            break

    return balance_history

fib_sequence = custom_fibonacci_sequence()
games = 10000
balance_history = play_roulette(fib_sequence, games)

# Plot the balance history
x_values = [x[0] for x in balance_history]
y_values = [x[1] for x in balance_history]

plt.plot(x_values, y_values, marker='o')  # Plot the balance history
plt.xlabel('Number of Hands')
plt.ylabel('Balance')
plt.title('Balance over 10000 Spins')

# Highlighting losses with red 'x' markers
for x, y, _, _, spin_result, total_bet, street1_bet, street2_bet, win, loss in balance_history:
    if y < 0:
        plt.scatter(x, y, color='red', marker='x')
    else:
        plt.scatter(x, y, color='green', marker='o')

plt.savefig('balance_plot.png')  # Save the plot as an image
plt.show()

# Print the balance history to the console
print("Balance History:")
print("{:<12} {:<10} {:<10} {:<10} {:<14} {:<9} {:<10} {:<10} {:<6} {:<6}".format("Hand Number", "Total Win", "Total Loss", "Balance", "Winning Number", "Total Bet", "Street 1 Bet", "Street 2 Bet", "Win", "Loss"))
for item in balance_history:
    print("{:<12} {:<10} {:<10} {:<10} {:<14} {:<9} {:<10} {:<10} {:<6} {:<6}".format(item[0], item[2], item[3], item[1], item[4], item[5], item[6], item[7], item[8], item[9]))

# Export the balance history to a markdown file
with open('balance_history.md', 'w') as f:
    f.write("| Hand Number | Total Win | Total Loss | Balance | Winning Number | Total Bet | Street 1 Bet | Street 2 Bet | Win | Loss |\n")
    f.write("|-------------|-----------|------------|---------|----------------|-----------|--------------|--------------|-----|------|\n")
    for item in balance_history:
        f.write("| {:11} | {:9} | {:10} | {:7} | {:14} | {:9} | {:12} | {:12} | {:4} | {:4} |\n".format(item[0], item[2], item[3], item[1], item[4], item[5], item[6], item[7], item[8], item[9]))

# Export the balance history to a text file
with open('balance_history.txt', 'w') as f:
    for item in balance_history:
        f.write("{},{},{},{},{},{},{},{},{},{}\n".format(item[0], item[2], item[3], item[1], item[4], item[5], item[6], item[7], item[8], item[9]))
