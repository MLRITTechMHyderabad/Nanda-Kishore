def minion_game(string):
    # your code goes here
    surat = kevin = 0
    vowels = 'AEIOU'
    length = len(string)

    for i in range(length) :
        if string[i] in vowels :
            kevin += length - i
        else :
            surat += length - i

    if kevin > surat :
        print("Kevin",kevin)
    elif kevin < surat :
        print("Stuart",surat)
    else :
        print("Draw")

minion_game("BANANA")