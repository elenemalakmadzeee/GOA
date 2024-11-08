# შექმენით რიცხვების სია შემგარი 10 მინიმუმ ელემენტისგან. გაიგეთ ამ სიაში ყველაზე პატარა და დიდი რიცხვი, შემდეგ კი დაბეჭდეთ მათი ჯამი
numbers = [15, 42, 7, 88, 33, 56, 1, 99, 23, 71]

smallest = numbers[0]  
largest = numbers[0]   

for num in numbers:
    if num < smallest:
        smallest = num  
    if num > largest:
        largest = num  


print(smallest + largest)

