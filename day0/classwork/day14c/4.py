#შექმენით სახელების სია სადაც გექნებათ მინიმუმ 10 სახელი, დაბეჭდეთ ამ სიიდან მხოლოდ ის სახელები რომლების ინდექსებიც არის ლუწი
names = ["elen", "ana", "nini", "mari", "luka", "saba", "kaxi", "andria", "lasha", "lizi", "elisabrdi"]

evens = []


for index in range(len(names)):
    if index % 2 == 0: 
        evens.append(names[index]) 

print( evens)