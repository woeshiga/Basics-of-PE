from random import randint

name = input("Enter your name: ")

age = input("Enter your age: ")

hobby = input("Enter your hobby: ")

print(f"Your name is {name}\nYour age is {age}\nYour hobby is {hobby}")

print("Nice to meet you! Let's play to my game!")

number = randint(0, 1)

while True:
    user_number = int(input("Zero or One? (0/1)"))
    if user_number not in [0, 1]:
        break

if user_number == number:
    print("Yes!))")
else:
    print("Nooo((")

input()
