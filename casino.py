import random

print("entering the casino !!")
print("please select your choice coin flip or leave")
choice = input("you: ").strip().lower()
while True:
    if choice == "coinflip":
        print("great choice!!")
    print("lets begin")

    heads = 1
    tails = 0
    result = random.randint(0, 1)

    print("heads or tails?")
    guess = input("you: ").strip().lower()

    if (guess == "heads" and result == heads) or (guess == "tails" and result == tails):
        print("victory")
    else:
        print("you lose")
else:
    print("you leave")

