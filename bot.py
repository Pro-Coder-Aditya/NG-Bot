import random

print("Hello this is NG-Bot")

bot_number = random.randrange(1, 101)
player_number = int(input("Enter your number: "))

if (player_number > bot_number):
    print("Bot number: ", bot_number)
    print("Your guess number is too high!")
elif (bot_number > player_number):
    print("Bot number: ", bot_number)
    print("Your guess number is too low!")
else:
    print("Bot number: ", bot_number)
    print("Your guess number is equal")