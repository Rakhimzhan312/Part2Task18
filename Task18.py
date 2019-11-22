def countingvalleys(num_of_steps, path):
    x=num_of_steps
    y=list(path)
    i=0
    level=0
    counter=0
    for x in range(2,9):
        if i==len(y):
            return counter
        if y[i]=='D' or y[i]=='d':
            level+=1
            i+=1
        elif y[i]=='U' or y[i]=='u':
            level-=1
            i+=1
        else:
            print('Not U or D')
        if level==0:
            counter+=1
        x-=1
    return counter
print(countingvalleys(8, 'dduuuudd'))