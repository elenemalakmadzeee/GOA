#მომხმარებელს შემოატანინეთ რიცხვი 1-დან 100-ის ჩათვლით(ეს იქნება მისი ქულა). თუ მაგალითად 90-დან 100-ის ჩათვლით ექნება ქულა გამოუტანეთ "Your grade is A", თუ 80-დან 90-მდე, გამოუტანეთ "Your grade is B", თუ 70-დან 80-მდე გამოუტანეთ "Your grade is C", სხვა შემთხვევაში გამოუტანეთ "Your grade is D"
grade=int(input("enter your grade:"))
if grade>=90 and grade<=100:
  print ("your grad is A")
elif grade>=80 and grade <90:
  print("your grade if B")
elif grade>=70 and grade<80:
  print ("your grade is C")
elif grade<70:
  print ("your grade is D")
else:
  print ("your grade is F")
