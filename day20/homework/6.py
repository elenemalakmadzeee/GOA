#შექმენით ფუნქცია, რომელსაც გადაეცემა ორი რიცხვების სია, გადაურეთ ორივეს for ციკლით და გაიგეთ თითოეულ 
# სიაში რიცხვების ჯამი(შეინახეთ ცალკე ცვლადებში), გაამრავლეთ ორივე ერთმანეთზე და დააბრუნეთ

def multiply_sums(list1, list2):
    sum1 = 0
    sum2 = 0

    for num in list1:
        sum1 += num
    for num in list2:
        sum2 += num
    return sum1 * sum2
 

list1 = [1, 2, 3]
list2 = [4, 5, 6]

result = multiply_sums(list1, list2)
print(result)




