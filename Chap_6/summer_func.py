def summer(list1):
    if type(list1[0]) == int or type(list1[0]) == float :
        sum1=0
    elif type(list1[0]) == str :
        sum1 = ''
    elif type(list1[0]) == list :
        sum1 = []
    for i in list1:
        sum1 = sum1 + i
    return sum1

print(summer(['aa','bb','cc']))
print(summer([1,2,3,4,5.1]))
print(summer([[1,2,3,4,5],['a','b','c','d']]))