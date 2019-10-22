n,m,a=[int(b) for b in input().split()]
if n%a==0 and m%a==0:
    c=n//a
    d=m//a
    e=c*d
    print (e)
 
 
elif n%a==0 and m%a!=0:
    c=n//a
    d=m//a+1
    e=c*d
    print (e)
 
elif n%a!=0 and m%a==0:
    c=n//a+1
    d=m//a
    e=c*d
    print (e)
 
 
elif n%a!=0 and m%a!=0:
    c=n//a+1
    d=m//a+1
    e=c*d
    print (e)
