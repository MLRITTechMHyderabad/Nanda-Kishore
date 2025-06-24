s = "Robert000Smith000123"

li1 = ["first_name","last_name","id"]
li2 = []
str = ''

for i in range(len(s)) :
    if s[i] != '0' :
        str += s[i]
    else:
        if len(str) != 0 :
            li2.append(str)
            str = ''
li2.append(str)

res = dict(zip(li1,li2))

print(res)