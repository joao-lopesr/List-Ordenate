def ordenate(lis):
    
    k = ' '
    for i in range(len(lis)):
        for k in range(i, len(lis)):
            if lis[i] > lis[k]:
                b = lis[i]
                lis[i] = lis[k]
                lis[k] = b

    
