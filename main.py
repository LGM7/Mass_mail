

with open("../Mail Merge Project Start/Input/Names/invited_names.txt",'r') as file:
    temp1 = file.read().splitlines()

with open("../Mail Merge Project Start/Input/Letters/starting_letter.txt", "r") as file:
    letter = file.read()

for n in range(0, len(temp1)):
    x = letter.replace("[name]", temp1[n])
    with open(f"./Output/ReadyToSend/letter_to_{temp1[n]}.txt", mode="w") as file:
        file.write(x)