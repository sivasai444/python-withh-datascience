def caluculator_(a,b):
    opr=input('enter the operator frome these (/,*,-,+):')
    
    if opr=='-':
        print('substraction:',a-b)
    elif opr=='+':
        print('addition:',a+b)
    
    elif opr=='/'and a>=1 or b>=1:
        print('division:',a/b or b/a)
    elif opr=='*':
        print('multiplication:',a*b)
    else:
        print('enter valid operator 😎')
    return 'operator is',opr
a=int(input('entert the value :'))
b=int(input('enter b vlaue: '))
cal=caluculator_(a,b)
print(cal)
    