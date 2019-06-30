def transfer(k,input):
    i=0
    j=len(input)-k-1
    ka=len(input)-k
    print (input[i],input[j] ,input[ka])
    while ka<len(input):
        input[i],input[j],input[ka] =input[ka],input[i],input[j]
        i=i+1
        j=j+1
        ka=ka+1
    return input


input =[1,2,3,4,5,6,7]
print (transfer(3, input))
input =[1,2,3,4,5,6,7]
print (transfer(2, input))