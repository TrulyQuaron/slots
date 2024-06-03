import random
import time

def play_slot_machine(balance, bet):
    slots = ["🍒", "💯", "🎰", "🪙", "🤑", "💵", "💰"]

    balance -= bet

    for i in range(10):
        slot = [random.choice(slots) for _ in range(3)]
        print("\r", slot, end="")
        time.sleep(0.10)
    print()

    if slot.count("🤑") == 3:
        outcome = "JACKPOT!!"
        multiplier = 1000
    elif slot.count("💯") == 3:
        outcome = "💯 💯 💯"
        multiplier = 500
    elif len(set(slot)) == 1:
        outcome = "Triple Match"
        multiplier = 100
    else:
        outcome = "No Win"
        multiplier = 0

    winnings = bet * multiplier
    balance += winnings

    print(f"Result: {outcome}")
    print(f"Bet: ${bet}, Multiplier: {multiplier}x")
    print(f"Winnings: ${winnings}")
    print(f"New Balance: ${balance}")

    return balance

def main():
    balance = 100  

    while True:
        print(f"Balance: ${balance}")
        bet = int(input("Enter your bet amount: "))
        
        if bet > balance:
            print("You don't have enough balance.")
            continue

        input("Press ENTER to roll the slots!\n")
        balance = play_slot_machine(balance, bet)

        if balance <= 0:
            print("You've run out of balance. Game Over!")
            break

        print()


if __name__ == "__main__":
    main()



input("Press ENTER to exit... \n")