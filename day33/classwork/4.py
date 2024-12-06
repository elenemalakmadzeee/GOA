# შექმენით manual_replace ფუნქცია, რომელიც იქნება .replace() ფუნქციის კლონი. ამ ფუნქციამ სთრინგში არსებული sapce-ები უნდა შეცვალოს ტირეებად.

#არ გამოიყენოთ ჩაშენებული ფუნქციები და კომენტარებით ახსენით მე-4 დავალება



def manual_replace(input_string, old, new):
    result = ""  
    i = 0  
   
    while i < len(input_string):

        if input_string[i:i+len(old)] == old:
            result += new  # დაამატეთ "new" სიტყვა result-ში
            i += len(old)  # გადავდივართ "old"-ის შემდეგი პოზიციაზე
        else:
            result += input_string[i]  # თუ არ არის match, უბრალოდ დავამატოთ მიმდინარე სიმბოლო
            i += 1  # გავიდეთ შემდეგ სიმბოლოზე
    
    return result  # დააბრუნეთ საბოლოო შედეგი
