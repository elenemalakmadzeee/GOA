# შექმენით ფუნქიცა, manual_find, რომელსაც გადაეცემა არგუმენტად სთრინგი და ერთი სიმბოლო, რომელიც უნდა ვიპოვოთ ამ სთრინგში.
#  თუ სიმბოლო მოიძებნა დააბრუნეთ მისი ინდექსი, სხვა შემთხვევაში დააბრუნეთ -1


def manual_find(word, symbol):
    if symbol not in word:
        return -1

    index = 0

    for i in word:
        if i == symbol:
            return index
        index += 1


print(manual_find("nika", "a"))
