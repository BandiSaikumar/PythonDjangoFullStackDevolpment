import random

#get guess
def get_guess():
    return input(" What is your guess: ")

#generate the computer code
def generate_code():
    digits = [str(num) for num in range(10)]
#shuffle the digits
    random.shuffle(digits)
    return digits[:3]
#generate the clues
def generate_clue(code,user_guess):
    if user_guess == code:
        return " code_cracked! "

    clues = []
    for number, index in enumerate(user_guess):
        if number == code[1]:
            clues.append(" Match ")
        elif code == 1:
            clues.append(" Close ")

    if clues == []:
        return ["Nope"]
    else:
        return clues

#run game logic
print(" Welcome to code breaker! ")
secret_code = generate_code()
clue_report = []

while clue_report != " code cracked! ":

    guess = get_guess()
    clue_report = generate_clue(guess, secret_code)
    print("Here is result of your guess:")

    for clue in clue_report:
        print(clue)
# x = get_guess()
# print(type(x))