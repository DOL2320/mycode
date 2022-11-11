#!/usr/bin/python3
user_input = int(input('How many bottles of beer? '))
while user_input > 100:
    user_input = int(input('How many bottles of beer? '))
for line in range(user_input):
    print(f'{user_input} bottles of beer on the wall! {user_input} bottles of beer! You take one down, pass it around!')
    user_input -= 1
    print(f'{user_input} bottles of beer on the wall!')
