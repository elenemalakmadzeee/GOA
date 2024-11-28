#შექმენით ფუნქცია manual_pop, რომელსაც გადაეცემა ორი არგუმენტი, სია და ინდექსი. წაშალეთ სიიდან, გადმოცემულ ინდექსზე მყოფი ელემენტი. საბოლოოდ კი დააბრუნეთ ეს სია(არ გამოიყენოთ .pop ფუნქცია)

def manual_pop(lst, index):
    
    if index < 0 or index >= len(lst):
        return lst
    
    return lst[:index] + lst[index + 1:]


