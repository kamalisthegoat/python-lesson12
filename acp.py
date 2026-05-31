jj = int(input("enter the first number of the range :"))
jj2 = int(input("enter the ending number of the range :"))

sqr = []

for i in range(jj, jj2+1):
    sqr.append(i*i)
print("the sqaures of the numbers are,", sqr)

evens= []
odd = []

for j in sqr:
    if j % 2 == 0:
        evens.append(j)

    else:
        odd.append(j)    

print("the even square are :", evens)

print("the odd square are :", odd)