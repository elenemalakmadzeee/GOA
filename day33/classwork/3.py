#შექმენით manual_count ფუნქცია, რომელსაც გადაეცემა სთრინგი ნა სია და ელემენტი რომლის რაოდენობაც უნდა გაიგოთ. დააბრუნეთ მიღებული შედეგი.

def manual_count(input_string, element):
    count = 0  
    i = 0  
    
    
    while i < len(input_string):
       
        if input_string[i:i+len(element)] == element:
            count += 1  
            i += len(element)  
        else:
            i += 1  
    
    return count 

original_string = "hello world, hello again, hello everyone"
element = "hello"
count_result = manual_count(original_string, element)
print(count_result)
