# შექმენით manual_join ფუნქცია, რომელსაც გადაეცემა სთინგების სია და ერთი სთრინგი. ამ ფუნქციამ უნდა შეართოს ეს სია და თითოეულ ელემენტს შორის ჩასვას გადმოცემული სთრინგი

#არ გამოიყენოთ .join() ფუნქცია
def manual_join(str_list, sr):
    if not str_list:
        return ""
    result = str_list[0]
  
    for i in str_list[1:]:
        result += sr + i
    
    return result



def manual_join(str_list, string1):
    result = ""

    for i in str_list:
        result += i + string1
    return result[:-3]


print(manual_join(list("Python"), " - "))