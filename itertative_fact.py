def iterative_fact(n):
    if(n==0):
        fact=1;
        return(fact);
    elif (n<0):
        print( "Undefined for negative numbers");
        return;
    else:
            fact=1;
            for i in range(2,n+1):
                fact=fact*i;
            return(fact);
print(iterative_fact(6));