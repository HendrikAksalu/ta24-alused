# Kolmnurki liigitatakse külgede pikkuse järgi erikülgseteks, võrdhaarseteks ja võrdkülgseteks. 
# Kirjutada programm, mis küsib kasutajalt kolme külje pikkused ning väljastab vastusena kolmnurga liigi. 
# Lisaks tuleb kontrollida, kas etteantud küljepikkustega kolmnurk saab üldse eksisteerida.
# Külje pikkused ei pea olema täisarvud. (ujukomaarv - float)


a = float(input("Sisesta esimese külje pikkus: "))
b = float(input("Sisesta teise külje pikkus: "))
c = float(input("Sisesta kolmanda külje pikkus: "))

if not (a + b > c and a + c > b and b + c > a):
    print("Sellist kolmnurka ei saa olemas olla")
elif a == b and a == c:
    print("Võrdkülgne kolmnurk")
elif a == b or b == c or a == c:
    print("Võrdhaarne kolmnurk")
else:
    print("Erikülgne kolmnurk")