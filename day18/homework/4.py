#შექმენით რიცხვების სია, სადაც გექნებათ დუბლიკატები. გადაუარეთ მას for loop-ით და დაბეჭდეთ მხოლოდ ისეთი რცხვების ჯამი,
#  რომლებიც არ მეორდება სიაში
chars = ["a", "a", "a", "b", "c", "b", "c"]

no_duplicates = []

for char in chars:
     if char not in no_duplicates:
         no_duplicates.append(char)

print(no_duplicates)