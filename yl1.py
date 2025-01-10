# Kirjuta programm, mis teisendab kasutaja poolt kroonides sisestatud summa eurodesse ja väljastab ümardatud tulemuse. (round)

eek = int (input("Sisesta summa kroonides "))
eur = eek / 15.6466
print("See on eurodes:", round (eur, 2))