#1) შექმენით ცვლადი, სადაც შეინახავთ string-ს. დაბეჭდეთ მისი თითოეული სიმბოლო და გვერდით მიუწერეთ რიგით მერამდენეა ის.

#მგალითად: "Hello" >>> "H - 1", "e - 2"...

word = "Hello"
l_word=len(word)
for i in range(l_word):
    print(word[i],i+1)
