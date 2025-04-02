def freq_of_num(list1):
    intcount = {}
    for i in list1:
        intcount[i] = intcount.get(i, 0) + 1
    return intcount

list1 = [1,2,3,1,2,3,6,7,8,6,5,4,6,4,3]
print(freq_of_num(list1))