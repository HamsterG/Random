import random

print("Please Chose a Difficulty")
print("Easy")
print("Medium")
print("Hard")
print("Extreme")
Easy = 'Easy'
Medium = 'Medium'
Hard = 'Hard'
Extreme = 'Extreme'
easy = ['1', '5']
medium = ['5', '10']
yesno = ['Yes', 'No']


x = input("Difficulty: ")


if x == 'Easy':
    print("Time: ") + (random.choice(easy))
    print("Delete After: ") + (random.choice(easy))
    print("How Many Extensions: ") + (random.choice(easy))
    print("Extension Duration: ") + (random.choice(easy))
    print("Pussy Out: ") + (random.choice(yesno))
    print("Enable Downoads: ") + (random.choice(yesno))
    print("Enable Comments: ") + (random.choice(yesno))

elif x == 'Medium':
    print("Time: ") + (random.choice(medium))
    print("Delete After: ") + (random.choice(medium))
    print("How Many Extensions: ") + (random.choice(medium))
    print("Extension Duration: ") + (random.choice(medium))
    print("Pussy Out: ") + (random.choice(yesno))
    print("Enable Downoads: ") + (random.choice(yesno))
    print("Enable Comments: ") + (random.choice(yesno))
