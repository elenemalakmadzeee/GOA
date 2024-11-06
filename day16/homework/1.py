#შექმენით სია სადაც გექნებათ რიცხვები. for loop-ის გამოყენებით იპოვეთ ამ სიაში ყველაზე დიდი რიცხვი
numbers = [10, 45, 3, 67, 23, 89, 2]
max_number = numbers[0]

for number in numbers:
    if number > max_number:
        max_number = number

print( max_number)