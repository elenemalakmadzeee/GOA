#შექმენით სია სადაც გექნებათ რიცხვები. for loop-ის გამოყენებით იპოვეთ ამ სიაში ყველაზე პატარა რიცხვi
numbers = [10, 45, 3, 67, 23, 89, 2]
min_number = numbers[0]

for number in numbers:
    if number < min_number:
        min_number = number

print( min_number)