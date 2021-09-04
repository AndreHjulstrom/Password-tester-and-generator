import random

password = input("Enter your current password:")
passwordlist = []
special_characters = "!@#$%^&*()-+?_=,<>/."
def fun(x, y):
    for i in y:
        x.append(i)
fun(passwordlist, password)
lettercount = 0
digitcount = 0
special_characterscount = 0
upperlettercount = 0

for a in range(0, len(passwordlist)):
    isdigit = passwordlist[a].isdigit()
    isletter = passwordlist[a].isalpha()
    isupper = passwordlist[a].isupper()
    if isupper == True:
        upperlettercount += 1
    elif isdigit == True:
        digitcount += 1
    elif isletter == True:
        lettercount += 1
    elif any(s in special_characters for s in passwordlist) == True:
        special_characterscount += 1

total_length = lettercount + digitcount + special_characterscount
if total_length <= 5:
    print("your password is too short")
elif 12 >= total_length > 5:
    print("your password could be longer for increased security")
elif total_length > 12:
    print("your password is of satisfactory length")
if lettercount == 0 or digitcount == 0 or special_characterscount == 0 or upperlettercount == 0:
    print(
        "your password should contain a variety of symbols,such as lower and uppercase letters, digits and special characters")

words_list = ["scary", "destruction", "wise", "dreary", "embarrass", "ignorant", "gleaming", "oval",
              "territory", "route", "agree", "interrupt", "didactic", "utopian", "hospitable", "known",
              "division", "connect", "deserve", "paddle", "bathe", "animated", "dysfunctional", "path",
              "hill", "tranquil", "roomy", "matter", "worthless", "rabid", "equable", "concentrate", "naughty",
              "zoom", "blush", "somber", "snotty", "righteous", "produce", "calculate", "complete", "fence",
              "nice", "painful", "economic", "agonizing", "effect", "quickest", "jolly", "boiling"]
words_list = [w.capitalize() for w in words_list]
rand_num = random.randint(1, 100)
choice = input(print("Do you want to generate a suggested password?"))
if choice == "yes":
    print(random.choice(words_list) + "-" + random.choice(words_list) +
          "-" + str(rand_num) + "-" + random.choice(words_list) + "-" + random.choice(words_list))
else:
    pass