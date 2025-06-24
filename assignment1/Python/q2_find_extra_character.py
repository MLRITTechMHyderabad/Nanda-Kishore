def comp(str1,str2) :
    for ch in str2 :
        if ch not in str1 :
            return ch
    return ''

print(comp('eueiieo','iieoedue'))