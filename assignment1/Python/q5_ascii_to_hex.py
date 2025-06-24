def hexa(str):
    res = ""
    for ch in str :
        res += hex(ord(ch)).lower() + " "
    return res

print(hexa("string"))