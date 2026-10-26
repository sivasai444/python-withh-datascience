try:
    lis=[]
    a=1
    b=50
    for i in range(a,b+1):
        if i>1:
            for j in range(2,i):
                if i%j==0:
                    break
            else:
                lis.append(i)
    print(lis)
except Exception as e:
    print('error: ',e)

finally:
    print('the program has excuted successfully')
