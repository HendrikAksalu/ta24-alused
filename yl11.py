# Kirjuta programm, mis küsib kasutajalt sisendina stringi.
# Eemalda selle sisendi algusest ja lõpust tühikud.
# String peab vastama tingimustele, et selles on vähemalt seitse sümbolit ja et sümbolite arv on paarituarvuline.
# Väljasta selle stringi kolm keskmist sümbolit.
# (stringi meetodid, list)

string = input("Sisesta sõna: ")
print(string)
string = string.strip()
print(string, "*")

if len(string) >= 7 and len(string) % 2 != 0:
   middle = len(string) // 2
   print(string[middle-1:middle+2])
   

else:
    print("Ei vasta tingimustele!")
