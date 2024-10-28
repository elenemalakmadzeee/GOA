#მომხარებელს შემოატანინეთ ორი რიცხვი, აიყვანეთ ისინი მე-3 ხარისხში და გაიგეთ მათი ჯამი, თუ ჯამი ლუწია დაპრინტეთ "Result is Even", სხვა შემთვევაში "Result is Odd
#შევქმნათ ორი ცვლადი
num1=int(input("enter number:"))
num2=int(input("enter second number:"))
#ავიყვანოთ კუბში
num3=num1**3
num4=num2**3
#შევკრიბოთ
sum=num3+num4
#გავიგოთ ეს ლუწია თუ კენტი
if sum%2==0:
  print("your number is even")
else:
  print("your number is odd")



