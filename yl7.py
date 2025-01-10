# Kirjuta programm, mis ütleb, kas kasutaja poolt etteantud täisarv on paarisarv või mitte. 
# (paarisarvu mõiste - odd/even)

a = int(input('a: '))

if a % 2 == 0:
    print(a, 'on paaris')    
else:
    print(a, 'on paaritu')