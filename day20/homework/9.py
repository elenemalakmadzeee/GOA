#შექმენით ფუნქცია, რომელსაც გადაეცემა სახელების სია. შექმენით ახალის სია, სადაც ჩაამატებთ გადმოცემული 
# სიიდან მხოლოდ იმ სახელებს, რომლებიც იწყება "N"-ზე`. საბოლოოდ დააბრუნეთ ეს სია
def filter_names_starting_with_n(names):
    n_names = []  # ახალი სია, სადაც ჩავამატებთ სახელებს, რომლებიც იწყება "N"-ზე
    for name in names:
        if name.startswith('N') or name.startswith('n'):  # ამოწმებს, თუ სახელის პირველი ასო არის "N" ან "n"
            n_names.append(name)
    return n_names
names = ["Nina", "John", "Nathan", "Anna", "nancy", "Mike"]
result = filter_names_starting_with_n(names)
print(result)
  