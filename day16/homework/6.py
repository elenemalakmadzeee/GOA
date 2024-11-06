#შექმენით სიმბოლოების სია, სადაც იქნება დუბლიკატები. შექმენით ახალი სია სადაც ყველა სიმბოლო მხოლოდ ერთხელ გვხვდება
chars = ['a', 'b', 'c', 'a', 'd', 'b']
unique_chars = []
for char in chars:
  if unique_chars.count(char)==0:
    unique_chars.append(char)
 
print(unique_chars)
#მეორე ხერხი
chars = ["a", "a", "a", "b", "c", "b", "c"]

no_duplicates = []

for char in chars:
    if char not in no_duplicates:
       no_duplicates.append(char)

print(no_duplicates)