#შექმენით სია სადაც ჩაამატებთ 1-დან 100-მდე ყველა ლუწ რიცხვს. საბოლოოდ დაპრინტეთ ეს სია(გამოიყენეთ for loop)
even_numbers = []

for number in range(1, 101):
    if number % 2 == 0:
        even_numbers.append(number)

print( even_numbers)
