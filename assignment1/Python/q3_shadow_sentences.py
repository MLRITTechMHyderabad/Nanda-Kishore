def shadows(s1,s2):
    s1_words = s1.split()
    s2_words = s2.split()

    if len(s1_words) != len(s2_words):
        return False

    for i in range(len(s1_words)) :
        if len(s1_words[i]) != len(s2_words[i]):
            return False

    s1_char = s1.replace(" ","").lower()
    s2_char = s2.replace(" ","").lower()

    for ch in s1_char :
        if ch in s2_char :
            return False

    return True

print(shadows("fold two times","they are round"))