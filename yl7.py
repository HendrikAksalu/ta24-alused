# Kirjuta programm, mis ütleb, kas kasutaja poolt etteantud täisarv on paarisarv või mitte. 
# (paarisarvu mõiste - odd/even)

a = int(input('a: '))
#Väljend (num % 2) == 0 kontrollib, kas arv num on paaris või mitte.
if a % 2 == 0: # % on mooduli (modulus) operaator, mis tagastab jagamise jäägi.
#num % 2 tähendab, et num jagatakse 2-ga ja tagastatakse jääk. == on võrdlusoperaator, mis kontrollib, kas kaks väärtust on võrdsed
    print(a, 'on paaris')    
else:
    print(a, 'on paaritu')