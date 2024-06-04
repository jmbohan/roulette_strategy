def place_bet():
    """Asks the user for their bet amount."""
    while True:
        try:
            bet = int(input("Enter your bet amount: "))
            if bet > 0:
                return bet
            else:
                print("Bet must be a positive amount.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def choose_bet_type():
    """Asks the user to choose the type of bet."""
    print("Choose your bet type:")
    print("1. Single number (0-36, 00)")
    print("2. Color (red/black)")
    print("3. Even/Odd")
    print("4. High/Low (1-18/19-36)")
    print("5. Dozen (1-12, 13-24, 25-36)")
    print("6. Column (1st, 2nd, 3rd)")
    print("7. Street (e.g., 1-2-3)")
    print("8. Six line (e.g., 1-2-3-4-5-6)")
    print("9. Split (e.g., 1-2)")
    print("10. Corner (e.g., 1-2-4-5)")
    while True:
        choice = input("Enter the number of your choice: ")
        if choice in [str(i) for i in range(1, 11)]:
            return choice
        else:
            print("Invalid choice. Please enter a number from 1 to 10.")

def get_user_bet(bet_type):
    """Gets the specific bet based on the chosen type."""
    if bet_type == '1':
        while True:
            number = input("Enter the number you want to bet on (0-36, 00): ")
            if number.isdigit() and 0 <= int(number) <= 36 or number == '00':
                return int(number) if number != '00' else '00'
            else:
                print("Invalid number. Please enter a number between 0-36 or '00'.")
    elif bet_type == '2':
        while True:
            color = input("Enter the color you want to bet on (red/black): ").lower()
            if color in ['red', 'black']:
                return color
            else:
                print("Invalid color. Please enter 'red' or 'black'.")
    elif bet_type == '3':
        while True:
            eo = input("Enter 'even' or 'odd': ").lower()
            if eo in ['even', 'odd']:
                return eo
            else:
                print("Invalid choice. Please enter 'even' or 'odd'.")
    elif bet_type == '4':
        while True:
            hl = input("Enter 'high' (19-36) or 'low' (1-18): ").lower()
            if hl in ['high', 'low']:
                return hl
            else:
                print("Invalid choice. Please enter 'high' or 'low'.")
    elif bet_type == '5':
        while True:
            dozen = input("Enter '1' for 1-12, '2' for 13-24, '3' for 25-36: ")
            if dozen in ['1', '2', '3']:
                return int(dozen)
            else:
                print("Invalid choice. Please enter '1', '2', or '3'.")
    elif bet_type == '6':
        while True:
            column = input("Enter '1' for 1st column, '2' for 2nd column, '3' for 3rd column: ")
            if column in ['1', '2', '3']:
                return int(column)
            else:
                print("Invalid choice. Please enter '1', '2', or '3'.")
    elif bet_type == '7':
        while True:
            street = input("Enter three consecutive numbers (e.g., 1-2-3): ").split('-')
            if len(street) == 3 and all(num.isdigit() and 0 <= int(num) <= 36 for num in street):
                return list(map(int, street))
            else:
                print("Invalid input. Please enter three consecutive numbers (e.g., 1-2-3).")
    elif bet_type == '8':
        while True:
            six_line = input("Enter six consecutive numbers (e.g., 1-2-3-4-5-6): ").split('-')
            if len(six_line) == 6 and all(num.isdigit() and 0 <= int(num) <= 36 for num in six_line):
                return list(map(int, six_line))
            else:
                print("Invalid input. Please enter six consecutive numbers (e.g., 1-2-3-4-5-6).")
    elif bet_type == '9':
        while True:
            split = input("Enter two adjacent numbers (e.g., 1-2): ").split('-')
            if len(split) == 2 and all(num.isdigit() and 0 <= int(num) <= 36 for num in split):
                return list(map(int, split))
            else:
                print("Invalid input. Please enter two adjacent numbers (e.g., 1-2).")
    elif bet_type == '10':
        while True:
            corner = input("Enter four adjacent numbers (e.g., 1-2-4-5): ").split('-')
            if len(corner) == 4 and all(num.isdigit() and 0 <= int(num) <= 36 for num in corner):
                return list(map(int, corner))
            else:
                print("Invalid input. Please enter four adjacent numbers (e.g., 1-2-4-5).")

def calculate_winnings(bet_type, user_bet, result, bet):
    """Calculates the winnings based on the bet and result."""
    number, color = result
    if bet_type == '1' and user_bet == number:
        return bet * 35  # 35:1 payout for a correct number bet
    elif bet_type == '2' and user_bet == color:
        return bet * 2  # 1:1 payout for a correct color bet
    elif bet_type == '3' and ((user_bet == 'even' and number != '00' and number % 2 == 0) or (user_bet == 'odd' and number % 2 == 1)):
        return bet * 2  # 1:1 payout for even/odd bet
    elif bet_type == '4' and ((user_bet == 'high' and 19 <= number <= 36) or (user_bet == 'low' and 1 <= number <= 18)):
        return bet * 2  # 1:1 payout for high/low bet
    elif bet_type == '5' and ((user_bet == 1 and 1 <= number <= 12) or (user_bet == 2 and 13 <= number <= 24) or (user_bet == 3 and 25 <= number <= 36)):
        return bet * 3  # 2:1 payout for dozen bet
    elif bet_type == '6' and ((user_bet == 1 and number % 3 == 1) or (user_bet == 2 and number % 3 == 2) or (user_bet == 3 and number % 3 == 0)):
        return bet * 3  # 2:1 payout for column bet
    elif bet_type == '7' and number in user_bet:
        return bet * 12  # 11:1 payout for street bet
    elif bet_type == '8' and number in user_bet:
        return bet * 6  # 5:1 payout for six line bet
    elif bet_type == '9' and number in user_bet:
        return bet * 18  # 17:1 payout for split bet
    elif bet_type == '10' and number in user_bet:
        return bet * 9  # 8:1 payout for corner bet
    else:
        return 0
