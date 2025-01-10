# Kirjuta programm, mis küsib kasutajalt nime, tervitab teda nimepidi, küsib kasutajalt elukoha, kui elukoht on Saaremaa, 
# siis väljastab mingi kommentaari, küsib kasutajalt vanuse, kui vanus on väiksem kui 18, 
# siis ütleb, et kasutaja on liiga noor, et autot juhtida, kui vanus on 18, 
# siis õnnitleb täisealiseks saamise puhul, kui kasutaja on vanem kui 18, 
# siis ütleb, et kasutaja võib autot juhtida. (sõne - string)



nimi = input("Sisesta oma nimi: ")
print(f"Tere, {nimi}!")

elukoht = input("Kus on sinu elukoht? ")

if elukoht.lower() .find("saaremaa") != -1 :
    print("Saaremaa on üks kena koht kus elada.")

vanus = int(input("Kui vana sa oled? "))

if vanus < 18:
    print("Sa oled liiga noor, et autot juhtida.")
elif vanus == 18:
    print("Palju õnne täisealiseks saamise puhul!")
else:
    print("Sa võid autot juhtida.")