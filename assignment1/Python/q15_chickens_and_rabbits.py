h = 34
l = 94
# 2c + 4r = l
# c + r = h
for i in range(h) :
  t_l = 2 * (h - i) + 4 * i
  if t_l == l :
    print(f"Chicken : {i}, Rabbit : {h-i}")
    break