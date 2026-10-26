string='ENTER THE STRING'

pr=list(i for i in string if i in 'aeiouAEIOU')
# v=['a','e','i','o','u','A','E','I','O','U']
# pr=list(i for i in string if i in v)
print('extarcted vowels: ',pr)
