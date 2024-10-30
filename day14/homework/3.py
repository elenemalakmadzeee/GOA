#შექმენით სია სადაც გექნებათ 10 რიცხვი, თქვენი დავალებაა გაიგოთ ამ სიაში ყველა ლუწი და კენტი რიცხვიოს ჯამი და დაბეჭდოთ
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_sum = 0
odd_sum = 0


for number in numbers:
    if number % 2 == 0: 
        even_sum += number
    else:  
        odd_sum += number

print( even_sum)
print( odd_sum)