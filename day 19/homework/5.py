#შექმენით რიცხვების სია, გადაუარეთ მას for loop-ით, გაიგეთ რამდენი ლუწი და რამდენი კენტი რიცხვი გვაქვს სიაში და დაბეჭდეთ მათი რაოდენობა
numbers=[10,7,9,45,68,1,2,9]
even_num=0
odd_num=0

for number in numbers:
    if number % 2 == 0:
        even_num += 1 
    else:
        odd_num += 1  

print(even_num)
print(odd_num)
