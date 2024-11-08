# შექმენით ცვლადი სადაც შეინახავთ სთრინგს და გაიგეთ, არის თუ არა ის პალინდრომი(პალინდრომი არის ისეთი სიტყვა, რომელიც ორივე მხრიდან ერთნაირად იკითხება, მაგალითად, "ana"...)
string = "elene"

# შევამოწმოთ, არის თუ არა პალინდრომი
if string == string[::-1]:
    print("This string is palidrome")
else:
    print("This string is not palidrome")