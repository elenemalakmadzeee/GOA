#შექმენით სია სადაც, შეიტანთ მინიმუმ 10 რიცხვს, გადაუარეთ for ციკლის დახმარებით და დაბეჭდეთ თითოეული რიცხვი კენტია თუ ლუწი.
numbers = [1,2,3,4,5,6,7,8,9,10]

evens = []
odds = []

for number in numbers:
  if number % 2 == 0:
        evens.append(number)
  else:
        odds.append(number)
      
print(evens)
print(odds)