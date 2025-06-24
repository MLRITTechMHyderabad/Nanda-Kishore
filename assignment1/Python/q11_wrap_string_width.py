str = "ABCDEFGHIJKLIMNOQRSTUVWXYZ"
w = 4
res = ''

i = 0
while i < len(str) :
  if i + w > len(str) :
    res += str[i:]
    break
  res += str[i:i+w] + '\n'
  i += w
print(res)