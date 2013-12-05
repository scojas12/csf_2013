n=13
series = 'fibonacci'

#if the string series is fibonacci
if series == "fibonacci":
    a=1
    b=0
   
    #calculates fibonacci
    for i in range(n):
        c=a+b
        print c
        a=b
        b=c

#if the string(series) is sum
elif series== "sum":
    number=0
    sums=0
    
    #finds the sum of the multiples of 3 to the nth numbber
    for i in range(n+1):
        number= 3 * i
        sums= number + sums
    print sums
    
#if the string(series) isn;t fib or sum
else:
    print "Invalid string"
    
#collaborator Alex, Micah, Brandon
    

        



    
    
