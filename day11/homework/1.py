#გააიაზრეთ ეს კოდი, დაკომენტარეთ თითოეული კოდი
#შვქმნათ პროგრამა სადაც მომხმარებელი გამოიცნობს პატოლს სამ ცდაში
#შევქმნათ ორი ცვლადი ერთში შევინახოთ პაროლი
secret_pass = "luka1234"
user_pass = ''
#ცდების რაოდენობა
tries = 3
#ყოველ არასწორ პაროლშე ცდებს აკლდება 1
while tries > 0 and user_pass != secret_pass:
    user_pass = input("Enter your password (you have " + str(tries) + " tries left): ")
    tries = tries - 1
#თუ სწორად გამოიცნობს დავბეჭდეოთ წდომა გაქვს ხოლო თუ არა დავბეჭდოთ ისევ ცადეთ
    if user_pass == secret_pass:
        print("Access granted!")
    elif tries == 0:
        print("You've reached the maximum number of tries. Access denied!")
    else:
        print("Access denied! Try again.")