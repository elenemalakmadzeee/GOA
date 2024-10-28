#მომხარებელს შემოატანინეთ რიცხვი და დაბეჭდეთ მიღებული რიცხვის ყველა გამყოფი(გამოიყენეთ for loop-ი)

number = int(input("enter number: "))

for i in range(1, number + 1):
    if number % i == 0: 
        print(i)
