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

        grape = 0
        watermelon = 0
        lemon = 0
        cherry = 0
        dollars = 0

        print()
        for row in range(len(display)):
            for col in range(len(display) + 1):
                if display[row][col] == self.symbols[0]:
                    grape += 1
                elif display[row][col] == self.symbols[1]:
                    watermelon += 1
                elif display[row][col] == self.symbols[2]:
                    lemon += 1
                elif display[row][col] == self.symbols[3]:
                    cherry += 1
                else:
                    dollars += 1

        for row in display:
            print(*row)

        if 5 <= dollars <= 7:
            winning = self.bet * 5
            print(f"YOU WON ${winning}")
        elif 8 <= dollars <= 11:
            winning = self.bet * 8
        elif dollars == 12:
            winning = self.bet * 100 + 50000
            print(f"JACKPOT!!! YOU WON ${winning}!")

        elif 5 <= grape <= 7:
            winning = self.bet * 4
            print(f"YOU WON ${winning}")
        elif 8 <= grape <= 12:
            winning = self.bet * 7
            print(f"YOU WON ${winning}")

        elif 5 <= watermelon <= 7:
            winning = self.bet * 3
            print(f"YOU WON ${winning}")
        elif 8 <= watermelon <= 12:
            winning = self.bet * 6
            print(f"YOU WON ${winning}")

        elif 5 <= lemon <= 7:
            winning = self.bet * 2
            print(f"YOU WON ${winning}")
        elif 8 <= lemon <= 12:
            winning = self.bet * 5
            print(f"YOU WON ${winning}")

        elif 5 <= cherry <= 7:
            winning = self.bet * 1
            print(f"YOU WON ${winning}")
        elif 8 <= cherry <= 12:
            winning = self.bet * 2
            print(f"YOU WON ${winning}")
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
