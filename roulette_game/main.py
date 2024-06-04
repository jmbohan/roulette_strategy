import os
import matplotlib.pyplot as plt
import pandas as pd
from bets import place_bet, choose_bet_type, get_user_bet, calculate_winnings
from wheel import spin_wheel

def generate_chart(running_totals):
    plt.figure()
    plt.plot(running_totals, marker='o')
    plt.title('Running Total Over Time')
    plt.xlabel('Round')
    plt.ylabel('Running Total')
    plt.grid(True)

    # Ensure the directory exists
    os.makedirs('logs', exist_ok=True)

    plt.savefig('logs/running_total_chart.png')
    plt.close()

def generate_markdown(log):
    md_content = "# Roulette Game Log\n\n"
    md_content += "| Round | Bet Amount | Bet Type | Bet       | Result     | Winnings | Running Total |\n"
    md_content += "|-------|-------------|----------|-----------|------------|----------|---------------|\n"
    for entry in log:
        md_content += f"| {entry['round']:<5} | {entry['bet_amount']:<11} | {entry['bet_type']:<8} | {entry['user_bet']:<9} | {entry['result']:<10} | {entry['winnings']:<8} | {entry['running_total']:<13} |\n"

    with open('logs/game_log.md', 'w') as f:
        f.write(md_content)

def main():
    total = 0
    rounds = []
    results = []
    running_totals = []

    round_number = 1

    while True:
        print("\nWelcome to Command Line Roulette!")
        bet = place_bet()
        bet_type = choose_bet_type()
        user_bet = get_user_bet(bet_type)
        
        result = spin_wheel()
        number, color = result
        print(f"The wheel landed on {number} ({color}).")

        winnings = calculate_winnings(bet_type, user_bet, result, bet)
        total += winnings - bet

        print(f"bet: {bet}")
        print(f"winnings: {winnings}")
        print(f"running total: {total}")

        # Log the result of the round
        rounds.append({
            "round": round_number,
            "bet_amount": bet,
            "bet_type": bet_type,
            "user_bet": user_bet,
            "result": f"{number} ({color})",
            "winnings": winnings,
            "running_total": total
        })

        running_totals.append(total)
        round_number += 1

        again = input("Do you want to play again? (yes/y/no/n): ").lower()
        if again not in ['yes', 'y']:
            break

    # Generate chart and markdown log
    generate_chart(running_totals)
    generate_markdown(rounds)

if __name__ == "__main__":
    main()
