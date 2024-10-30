# შექმენით ხილების სია სადაც გექნებათ მინიმუმ 10 ელემენტი, while loop-ის გამოყენებით წაშალეთ სიის ბოლო ელემენტი იქამდე სანამ სიაში არ დარჩება ორი ელემენტი. ყოველი ელემენტის წაშლისას დაბეჭდეთ ხილების სია
fruits = ["banana", "strawberry", "apple", "orange", "pear", "pinapple", "kiwi", "watermelon", "melon", "berry"]

while len(fruits) > 2:
    fruits.pop()  
print( fruits)