#შექმენით ფუნქცია, რომელსაც გადასცემთ რიცხვების სიას. გადაუარეთ გადმოცემულ სიას for ციკლით და დააბრუნეთ ახალი სია,
#  სადაც ჩამატებული იქნება გადმოცემული სიიდან მხოლოდ ის რიცხვები, რომლებიც მეტია 10-ზე. საბოლოოდ დააბრუნეთ ეს სია
def filter_greater_than_10(numbers):
    result = []
    for number in numbers:
        if number > 10:
            result.append(number)
    return result
numbers = [5, 12, 8, 20, 3, 15, 7]
filtered_numbers = filter_greater_than_10(numbers)
print(filtered_numbers)
