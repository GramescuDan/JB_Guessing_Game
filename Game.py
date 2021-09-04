import random


def word_check(wch):
    word_list = list(wch)
    new_word = ""
    for i in word_list:
        if i in ['0', '1']:
            new_word += i
    return new_word


def triad_check(word):
    word_list = list(word)
    for i in range(3, len(word)):
        tri = word_list[i - 3] + word_list[i - 2] + word_list[i - 1]
        if word_list[i] == "1":
            triads[tri][1] += 1
        elif word_list[i] == "0":
            triads[tri][0] += 1


def to_bit(num):
    cicle = 0
    bit = ""
    while cicle != 3:
        if int(num % 2) == 0:
            bit += '0'
        else:
            bit += "1"
        num = int(num / 2)
        cicle += 1
    return bit


def guess_former(string_guess):
    bt = random.randint(26, 43)
    bt = to_bit(bt)
    computer_string = bt
    for i in range(3, len(string_guess)):
        tri = string_guess[i - 3] + string_guess[i - 2] + string_guess[i - 1]
        if triads[tri][0] > triads[tri][1]:
            computer_string += "0"
        elif triads[tri][0] < triads[tri][1]:
            computer_string += "1"
        elif triads[tri][0] == triads[tri][1]:
            if i % 2 == 0:
                computer_string += "1"
            else:
                computer_string += "0"

    return computer_string


def last_three(cmp_str):
    last = list(cmp_str)
    return last[len(last) - 3] + last[len(last) - 2] + last[len(last) - 1]


def first_three(cmp_str):
    last = list(cmp_str)
    return last[0] + last[1] + last[2]


triads = {"000": [0, 0], "001": [0, 0], "010": [0, 0], "011": [0, 0],
          "100": [0, 0], "101": [0, 0], "110": [0, 0], "111": [0, 0]}
real_word = ""


def check_difference(string_guess, ai_guess):
    nr = 0
    first = list(string_guess)
    second = list(ai_guess)
    for i in range(3, len(first)):
        if first[i] == second[i]:
            nr += 1
    return nr


def start():
    print("Please give AI some data to learn...")
    print("The current data length is 0, 100 symbols left")
    real_word = ""
    while True:
        word = input("Print a random string containing 0 or 1:")
        word = word_check(word)
        real_word += word
        print("The current data length is {0}, {1} symbols left".format(len(real_word), 100 - len(real_word)))
        if len(real_word) >= 100:
            print("Final data string:")
            print(real_word)
            break
    triad_check(real_word)



def game():
    start()
    money = 1000
    print("""You have $1000. Every time the system successfully predicts your next press, you lose $1.
Otherwise, you earn $1. Print "enough" to leave the game. Let's go!""")
    while True:
        print("Print a random string containing 0 or 1:")
        string_guess = input()
        if string_guess == "enough":
            break
        else:
            string_guess = word_check(string_guess)
            if string_guess == "":
                continue
        print("prediction:")
        ai_guess = guess_former(string_guess)
        print(ai_guess)
        a = check_difference(string_guess, ai_guess)
        print("Computer guessed right {0} out of {1} symbols ({2} %)".format(a, len(ai_guess) - 3,
                                                                             round((a * 100) / (len(ai_guess) - 3), 2)))
        money -= a
        money += len(ai_guess) - 3 - a
        print("Your balance is now ${0}".format(money))

    print("Game over!")

game()
