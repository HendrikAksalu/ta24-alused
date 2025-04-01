# Kirjuta programm, mis küsib kasutajalt sisendina stringi.
# Eemalda selle sisendi algusest ja lõpust tühikud.
# String peab vastama tingimustele, et selles on vähemalt seitse sümbolit ja et sümbolite arv on paarituarvuline.
# Väljasta selle stringi kolm keskmist sümbolit.
# (stringi meetodid, list)

string = input("Sisesta sõna: ")
print(string)
string = string.strip() # strip() meetod on Pythonis stringimeetod, mis eemaldab tühikud (või määratud märgid) stringi algusest ja lõpust.
print(string, "*")

if len(string) >= 7 and len(string) % 2 != 0: # Greater than or equal ( >= )
   middle = len(string) // 2 # Funktsioon len() tagastab objektis olevate elementide arvu.
   print(string[middle-1:middle+2])
   

else:
    print("Ei vasta tingimustele!")
