import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_values = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winnings_lines =[]
    for line in range(lines):
       # print("01 " + str(range(lines)))
        symbol = columns[0][line]
        #print("02 " + symbol)
        for column in columns:
            symbol_to_check = column[line]
            #print("03 " + symbol_to_check)
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winnings_lines.append(line +1)
    return winnings, winnings_lines


###spin of machine
def get_slot_machine_spin(rows, cols, symbols):
    all_symbols =[]
    for symbol,symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column =[]
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i,column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row],end=" | ")
            else:
                print(column[row], end="")    

        print()

### deposit money###
def deposit():
    while True:
        amount = input("what would you like to depsoit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than zero")
        else:
            print("please enter a number.")
    return amount

###getting lines to bet from user
def get_number_of_lines():
    while True:
        lines = input("enter number of lines to bet on (1-" + str(MAX_LINES)+ ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                    print("enter a valid number of lines")
        else:
            print("please enter a number.")
    return lines

##getting bet amount on each line
def get_bet():
    while True:
        amount = input("what would you like to bet? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("please enter a number.")
    return amount

def spin(balance):
    lines = get_number_of_lines()
    while True: 
        bet = get_bet()
        #print("01-here")
        total_bet = bet * lines

       #print(f"02-here {total_bet}")
        if total_bet > balance:
            print(f"Not enough money to bet. Your current balance is ${balance}")
        else:
            break

    print(f"you are betting ${bet} on {lines} lines. Total bet = ${total_bet}")

    slots = get_slot_machine_spin(ROWS,COLS,symbol_count)
    print_slot_machine(slots)
    winnings,winnings_lines = check_winnings(slots, lines, bet, symbol_values)
    print(f"You won ${winnings}.")
    print(f"You won on lines:",*winnings_lines)
    return winnings- total_bet

def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        play = input("press enter to play(q to quit)")
        if play == "q":
            break
        balance +=spin(balance)

    print(f"you left with ${balance}")


main()
              
