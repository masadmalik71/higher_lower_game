from art import logo
from art import vs
from game_data import data
import re
import random
import os

random_number1 = random.randint(0, len(data))
random_number_bol = False
while not random_number_bol:
    random_number2 = random.randint(0, len(data))
    if random_number1 != random_number2:
        random_number_bol = True

current_score = 0
user_choice = 0
left = 0
compare_a = data[random_number1]
compare_b = data[random_number2]


def compare_maker(already_number):
    go_out = False
    while not go_out:
        random_number = random.randint(0, len(data))
        if already_number != random_number:
            return random_number


game_loop = False
while not game_loop:
    os.system('cls')
    print(logo)
    print(f"Compare A: {compare_a['name']}, a {compare_a['description']}, from {compare_a['country']}.")
    print(vs)
    print(f"Compare B: {compare_b['name']}, a {compare_b['description']}, from {compare_b['country']}.")
    input_loop = False
    while not input_loop:
        user_input = input("Who has more followers: ")
        user_input_list = re.findall("a|b", user_input)
        if user_input_list:
            user_input = ''.join(user_input_list)
            if user_input == 'a':
                user_choice = int(compare_a['follower_count'])
                left = int(compare_b['follower_count'])
            elif user_input == 'b':
                user_choice = int(compare_b['follower_count'])
                left = int(compare_a['follower_count'])
            input_loop = True
        else:
            print("You entered wrong input. Please enter again.")

    if user_choice >= left:
        current_score += 1
        print(f"You're right! Currently score: {current_score}")
        if compare_b["follower_count"] > compare_a["follower_count"]:
            compare_a = compare_b
        already_used_number = data.index(compare_b)
        compare_b = data[compare_maker(already_used_number)]
    elif user_choice < left:
        print(f"Sorry, that's wrong. Final score: {current_score}")
        input("Press any key and enter if want to close console")
        game_loop = True
