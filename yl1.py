# Kirjuta programm, mis teisendab kasutaja poolt kroonides sisestatud summa eurodesse ja väljastab ümardatud tulemuse. (round)

eek = int (input("Sisesta summa kroonides ")) # Funktsioon input() võimaldab kasutajal sisestada andmeid.
eur = eek / 15.6466
print("See on eurodes:", round (eur, 2)) ## round funktsioon tagastab lähima täisarvu
#Funktsioon print() kuvab määratud teate ## ümardab muutuja eur väärtuse kuni kahe kümnendkohani.
