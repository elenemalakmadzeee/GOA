#დაბეჭდეთ 1-დან 100-მდე ყველა ლუწი რიცხვის საშუალო არითმეტიკული. გამოიყენეთ while loop-ი.(დაგჭირდებათ ორი ცვლადის შექმნა, ერთში შეინახავთ ჯამს, მეორეში რაოდენობას)
num=1
sum=0
count=0

while num<100:
   if num%2==0:
    sum += num 
    count += 1  
   num += 1 

print(num)

average_even = sum / count 


print( average_even)


  












