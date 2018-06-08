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
hardtime = ['15 Minutes', '30 Minutes', '1 Hour', '2 Hours', '6 Hours', '12 Hours']
hard = ['15', '20', '25', '30', '35', '40']
yesno = ['Yes', 'No']
level = ['Easy', 'Medium', 'Hard', 'Extreme']



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
elif x == 'Hard':
        print("Time: ") + (random.choice(hardtime))
        print("Delete After: ") + (random.choice(hardtime))
        print("How Many Extensions: ") + (random.choice(hard))
        print("Extension Duration: ") + (random.choice(hardtime))
        print("Pussy Out: ") + (random.choice(yesno))
        print("Enable Downoads: ") + (random.choice(yesno))
        print("Enable Comments: ") + ('Yes')
elif x == 'Extreme':
    print("Randomise all")
