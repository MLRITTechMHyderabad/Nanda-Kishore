def check(sen):
   words = sen.lower().split()
   for word in words :
       if len(word) != len(set(word)) :
           return True
   return False

print(check("im Nanda Kishore"))