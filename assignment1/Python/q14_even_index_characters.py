s = "H1e2l3l4o5w6o7r8l9d"
num = "1234567890"
i = 1
for ch in s :
  if i % 2 == 1 and ch not in num :
    print(ch,end = '')
  i += 1