print ("Give me some words")
user_input = input()
words = user_input.split(" ")
initials = " "
for word in words:
    initials = initials + word[0]
print (initials.upper())