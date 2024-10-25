#4) შექმნით რიცხვის გამოცნობის თამაში while ციკლით, რომელიც მომხმარებელს შეეკითხება რიცხვს 1-დან 10-მდე, სანამ მომხმარებელი არ შეიყვანს თქვენთვის სასურველ რიცხვს
my_num=3
guess=0

while my_num!=guess:
    guess=int(input("enter your guess:"))

    if my_num==guess:
     print("correct")
    else:
     print("incorrect try again")