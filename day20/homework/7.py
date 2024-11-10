#შექმენით ფუნქცია, რომელსაც გადაეცემა რიცხვების სია. გადაუარეთ ამ სიას while ციკლით და
#  ჩაამატეთ გაორმაგებული რიცხვები ახალ სიაში. საბოლოოდ დააბრუნეთ ეს სია
def double_numbers(numbers):
    doubled_numbers = []  
    i = 0  # ინდექსი
    while i < len(numbers):
        doubled_numbers.append(numbers[i] * 2)  # გაორმაგებული რიცხვის დამატება სიაში
        i += 1  # ინდექსის მომატება
    return doubled_numbers
numbers = [1, 2, 3, 4, 5]
result = double_numbers(numbers)
print(result)
