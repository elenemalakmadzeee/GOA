# შექმენით ფუნქცია, რომელსაც გადაეცემა სიმბოლოების სია. ფუნქციამ უნდა დააბრუნოს ეს სია პირველი და ბოლო ელემენტების გარეშე, გამოიყენეთ slicing-ი
def remove_first_and_last(char_list):
    return char_list[1:-1]
char_list = ['a', 'b', 'c', 'd', 'e']
result = remove_first_and_last(char_list)
print(result)
