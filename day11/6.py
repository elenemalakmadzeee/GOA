# დაწერეთ პროგრამა, რომელიც მომხარებელს შემოატანინებს რიცხვს და დაბეჭდავს ეს რიცხვი დადებითია, უარყოფითია თუ 0-ია
num=float(input("enter number:"))
if num <0:
  print ("your number is negative")
elif num>0:
   print("your number is positive")
else:
 print("your number is 0")