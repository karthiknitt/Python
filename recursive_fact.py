def recursive_fact(n):
   
    if(n==0 or n==1):
        fact=1;
        return(fact);
    elif (n<0):
        print( "Undefined for negative numbers");
        return;
    else:
            fact=recursive_fact(n-1);
            fact=fact*n;
            return(fact);

print(recursive_fact(7));