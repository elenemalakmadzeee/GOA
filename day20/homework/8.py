#შექმენით ფუნქცია, რომელსაც გადაეცემა რიცხვების სია. გადაუარეთ ამ სიას for ციკლით და
#  ჩაამატეთ მხოლოდ ლუწი რიცხვები ახალ სიაში. საბოლოოდ დააბრუნეთ ეს სია
def filter_even_numbers(numbers):
    even_numbers = []  # ახალი სია, სადაც ჩაიმატება მხოლოდ ლუწი რიცხვები
    for num in numbers:
        if num % 2 == 0:  # თუ რიცხვი ლუწია
            even_numbers.append(num)
    return even_numbers


numbers = [1, 2, 3, 4, 5, 6, 7, 8]
result = filter_even_numbers(numbers)
print(result)

