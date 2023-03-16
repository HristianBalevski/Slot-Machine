import random


class SlotMachine:
    def __init__(self):
        self.symbols = ['🍇', '🍉', '🍋', '🍒', '💰']
        self.bet = 0
        self.balance = 0

    def play(self):

        while True:
            try:
                print()
                self.bet = int(input('Please place your bet: '))
                if self.bet <= 0 or self.bet > self.balance:
                    raise ValueError
                break
            except ValueError:
                print(f'Please bet money between $1 and ${self.balance}')
        display = []
        for _ in range(3):
            spins = [random.choice(self.symbols) for _ in range(4)]
            display.append(spins)

        print()
        winning = 0
        win_fruit = []
        if display[0][0] == display[0][1] == display[0][2] == display[0][3]:
            if len(win_fruit) == 0:
                win_fruit.append(display[0][0])
                winning += 1
            else:
                if win_fruit[0] == display[0][0]:
                    winning += 1

        if display[1][0] == display[1][1] == display[1][2] == display[2][3]:
            if len(win_fruit) == 0:
                win_fruit.append(display[1][0])
                winning += 1
            else:
                if win_fruit[0] == display[1][0]:
                    winning += 1

        if display[2][0] == display[2][1] == display[2][2] == display[2][3]:
            if len(win_fruit) == 0:
                win_fruit.append(display[2][0])
                winning += 1
            else:
                if win_fruit[0] == display[2][0]:
                    winning += 1

        if display[0][0] == display[1][0] == display[2][0]:
            if len(win_fruit) == 0:
                win_fruit.append(display[0][0])
                winning += 1
            else:
                if win_fruit[0] == display[0][0]:
                    winning += 1

        if display[0][1] == display[1][1] == display[2][1]:
            if len(win_fruit) == 0:
                win_fruit.append(display[0][1])
                winning += 1
            else:
                if win_fruit[0] == display[0][1]:
                    winning += 1

        if display[0][2] == display[1][2] == display[2][2]:
            if len(win_fruit) == 0:
                win_fruit.append(display[0][2])
                winning += 1
            else:
                if win_fruit[0] == display[0][2]:
                    winning += 1

        if display[0][3] == display[1][3] == display[2][3]:
            if len(win_fruit) == 0:
                win_fruit.append(display[0][3])
                winning += 1
            else:
                if win_fruit[0] == display[0][3]:
                    winning += 1

        for row in display:
            print(*row)

        if winning == 1:
            winning = self.bet * 5
            print(f"YOU WON ${winning}")
        elif winning == 2:
            winning = self.bet * 10
            print(f"YOU WON ${winning}")
        elif winning == 3:
            winning = self.bet * 15
            print(f"YOU WON ${winning}")
        elif winning == 4:
            winning = self.bet * 20
            print(f"YOU WON ${winning}")
        elif winning == 5:
            winning = self.bet * 25
            print(f"YOU WON ${winning}")
        elif winning == 6:
            winning = self.bet * 30
            print(f"YOU WON ${winning}")
        elif winning == 7:
            winning = self.bet * 100
            print(f"JACKPOT!!! YOU WON ${winning}!")
        else:
            winning = 0
            print("Sorry You didn't win this time.")
        self.balance += winning - self.bet
        print(f"Current Balance: ${self.balance}")

    def add_money(self, amount):
        self.balance += amount
        print(f"Current Balance: ${amount}")

    def withdraw(self, amount):
        while True:
            if 0 < amount <= self.balance:
                self.balance -= amount
                print()
                print(f'Money Out: ${amount}')
                print(f'Current Balance: ${self.balance}')
                break
            else:
                amount = int(input(f'Please enter amount between $1 and ${self.balance}: '))


machine = SlotMachine()
print(f'{"🍀♧~♡~☆~◇ WELCOME TO CASINO ROYAL ♧~♡~☆~◇ 🍀"}')
print()
money_in = int(input('Please insert your money: '))
machine.add_money(money_in)

while machine.balance > 0:
    machine.play()

    if machine.balance > 0:
        print()
        answer = input("Press enter to play or (w) to withdraw money. ")
        if answer == "w":
            try:
                amount = int(input("Please enter amount: "))
                machine.withdraw(amount)
            except ValueError:
                print("Invalid Input")
print('Good Bye...')
