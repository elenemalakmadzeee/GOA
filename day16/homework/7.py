#შექმენით ცლვადი სადაც შეინახავთ string-ს, შემდეგ შექმენით ახალი ცვლადი სადაც შეინახავთ ამ სტრინგს შემოტრიალებულად და დაბეჭდეთ ის
chars = ['a', 'b', 'c', 'a', 'd', 'b']
unique_chars = []

for char in chars:
    if char not in unique_chars:
        unique_chars.append(char)

print( unique_chars)
