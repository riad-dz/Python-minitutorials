#### Program with conditions to estimate which category of age you are ######

age=int(input("What is your age"))

if age == 100:
    print("you're a century old")

elif age >= 18:
    print("you're an adult")

elif age < 0:
    print("you're not yet born")

else:
    print("you' re a child")