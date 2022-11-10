#!/usr/bin/python3

challenge= ["science", "turbo", ["goggles", "eyes"], "nothing"]


trial= ["science", "turbo", {"eyes": "goggles", "goggles": "eyes"}, "nothing"]


nightmare= [{"slappy": "a", "text": "b", "kumquat": "goggles", "user":{"awesome": "c", "name": {"first": "eyes", "last": "toes"}},"banana": 15, "d": "nothing"}]

print("My " + challenge[2][1] + "! The " + challenge[2][0] + " do " + challenge[3] + "!")

eyes = trial[2]['goggles']
goggles = trial[2]['eyes']
nothing = trial[3]
print(f"My {eyes}! The {goggles} do {nothing}!")

eyes = nightmare[0]['user']['name']['first']
goggles = nightmare[0]['kumquat']
nothing = nightmare[0]['d']
print("My ", eyes, "! The ", goggles, " do ", nothing, "!", sep="")
