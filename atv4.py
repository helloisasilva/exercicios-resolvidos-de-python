a=input('digite algo: ')
print(type(a))
if type(a)==str or type(a)==int:
    print(f'só tem espaços? {False}')
else:
    print(f'só tem espaços? {True}')
