#შექმენით ფუნქცია, manual_capitalize რომელიც იქნება capitalize ფუნქციის კლონი
def manual_capitalize(text):
    result = ""
    
    if text:  # თუ სტრინგი არ არის ცარიელი
        result = text[0].upper()  # პირველი ასო დიდად
        result += text[1:].lower()  # დანარჩენი ასოები დაბლად
    
    return result

# ტესტი:
print(manual_capitalize("HellO, MY namE IS elene"))






def manual_capitalize(string1):
    return string1[0].upper() + string1[1:].lower()

print(manual_capitalize("hEllo HSDIJSD HEllo"))