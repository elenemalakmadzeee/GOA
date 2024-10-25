# შექმენით პროგრამა რომელიც მომხმარებელს შეეკითხება pin კოდს (4 ციფრიანი კოდი) მანამდე სანამ არ შეიყვანს 1234-ს
pin=input ("enter 4 letter pin:")
correct_pin=1234
if pin != correct_pin:
  print ("correct")
if pin==correct_pin:
    print("incorrect")