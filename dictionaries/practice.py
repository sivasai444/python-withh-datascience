dict1={'hyderabad','mumbai','chenai','bangalore'}
value='city'
res=dict.fromkeys(dict1,value)
print(res)
del res['chenai']
print(res)
m=res.pop('mumbai')
print(m)
print(res)