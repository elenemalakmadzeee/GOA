#შექმენით ორი ცვლადი, პირველში შეინახეთ 1-დან 20-ის ჩათვლით ყველა ლუწი რიცხვის ჯამი, მეორეში კი ყველა კენტის. აიყვანეთ ორივე მე-5 ხარისხში და დაპრინტეთ ის, რომელიც არის მეტი
for even_num in range(1, 21) :
  if even_num % 2 == 0:

   for odd_num in range(1, 21):
    if odd_num % 2 != 0:
     
     even = even_num ** 5
     odd = odd_num ** 5

   if even > odd:
      print(even,"even")
   else:
      print(odd,"odd")
       