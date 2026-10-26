n=int(input('entre the value: '))
dicti={}

for i in range(n):
    key=input('enter the key product name : ')
    value=int(input('entre the price of the product :'))
    dicti[key]=value

# highest_price=0
# highest_product=''
# for product, price in dicti.items():
#     if price>highest_price:
#         highest_price=price
#         highest_product=product

# print('the highet price product : ',highest_product,':',highest_price)

highest_price=max(dicti.values())
for product,price in dicti.items():
    if price==highest_price:
        print({product:price})



