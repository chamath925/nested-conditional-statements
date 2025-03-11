print("select your ride")
print("1.bike")
print("2.car")

choice = int(input("enter your choice: "))

if(choice == 1):
    print("what type of bike?")
    print("1.scooty\n ")
    print("2.scooter\n")

choice2=int(input("Enter your choice 2: "))
if choice2 == 1:
    print("you have selected scooty")
else:
    print("you have selected scooter")