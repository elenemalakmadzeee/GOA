#შექმენით რიცხვების სია და დაპრინტეთ სიის თითოეული ელემენტი უკუღმა(გამოიყენეთ range() ფუქნცია ან შექმენით ცვლადი)
numbers = [1, 2, 3, 4, 5]
length = len(numbers)
index = length - 1

while index >= 0:
    print(numbers[index])
    index -= 1