#1) შექმენით რიცხვების სია, შემდგარი მინიმუმ 10 ელემენტისგან. გადაუარეთ ამ საის while loop-ის გამოყენებით.
#  გაიგეთ ცალკე ლუწი და კენტი რიცხვების ჯამი, საბოლოოდ შეადარეთ ისინი ერთმანეთს და დაპრინტეთ უდიდესი



numbers = [5, 8, 13, 4, 7, 10, 6, 2, 9, 11]


index = 0
even_sum = 0
odd_sum = 0

while index < len(numbers):
    if numbers[index] % 2 == 0:
        even_sum += numbers[index]
    else:
        odd_sum += numbers[index]
    index += 1


if even_sum > odd_sum:
    print("even num is greater ")
else:
    print("odd num is greater")



