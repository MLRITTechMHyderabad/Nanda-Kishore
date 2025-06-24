def block_win(n1,n2) :
    winning = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for win in winning :
        if n1 in win and n2 in win :
            for w in win :
                if w != n1 and w != n2 :
                    return w
    return -1
print(block_win(0,1))