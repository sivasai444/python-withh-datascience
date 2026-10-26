def simple_interest(p,t,r):
    if p>=1 and t>=2 and r>=1:
       return p*t*r/100
    else:
        return 'enter valid input'
    
p=float(input('enter the price p: '))
r=float(input('enter the rate of interest r:'))
t=float(input('enter the time period t :'))
rel=simple_interest(p,t,r)
print('total simple interest is ',rel)
print('total money you have to recieve is ',rel+p)