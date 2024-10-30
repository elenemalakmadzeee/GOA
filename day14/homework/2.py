#შექმენით სახელების სია სადაც გექნებათ მინიმუმ 10 სახელი, დაბეჭდეთ ამ სიიდან მხოლოდ ის სახელები რომლების ინდექსებიც არის ლუწი
names = ["mari", "giorgi", "ana", "dato", "elene", "saba", "nika", "tamari", "rezo", "qeta"]

# for ციკლი
for index in range(len(names)):
    if index % 2 == 0:  
        print(names[index])