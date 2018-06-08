import random
import time



Mistress = 'Mistress'
Weather = 'Weather'
Stocks = 'Stocks'
task = ['Crotch Rope', 'No Underwear','Gym Work Out','School Fun Time','Gym Fun Walk']

print("Good Morning Sir," + " How may I help you?")
print("1.Mistress")
print("2.Weather")
print("3.Stocks")
print("4.Reminderes")

choice = input("What is your choice: ")


if choice == Mistress:
    print("Good choice sir, fetching her now...")
    time.sleep(2)
    print("Good Morning Boy!")
    print("Get on you knees and wait until I make my choice")
    time.sleep(10)
    print(random.choice(task))
elif choice == Weather:
    print("Weather")
elif choice == Stocks:
    print("Stocks")
