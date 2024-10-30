# შექმენით სია სადაც ჩაამატებთ ყველა რიცხვს 1-დან 50-ის ჩათვლით. შემდეგ გადაუარეთ for loop-ით და ამ სიიდან წაშალეთ ყველა კენტი რიცხვი. საბოლოოდ დაპრინტეთ მიღებული სია

numbers = list(range(1, 51))


even_numbers = []


for number in numbers:
    if number % 2 == 0:  
        even_numbers.append(number) 


print( even_numbers)