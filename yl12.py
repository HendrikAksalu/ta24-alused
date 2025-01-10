# Anna muutuja väärtuseks list kolmest oma lemmik puuviljast ja väljasta see
# Väljasta listi esimene väärtus
# Lisa listi lõppu uus puuvili
# Väljasta listi viimane väärtus
# Muuda ühe elemendi väärtust ja väljasta kogu list
# Kontrolli kas väärtus (näiteks õun) eksisteerib listis
# Väljasta listi pikkus
# Eemalda listist element ja väljasta kogu list
# Muuda listi järjekord vastupidiseks
# Sorteeri list ja väljasta
# (jada, list, listi element, listi meetodid)


puuviljad = ["banaan", "mango", "ananass"]
print("Esialgne list:", puuviljad)

print("Esimene väärtus:", puuviljad[0])

puuviljad.append("apelsin")
print("Pärast uue puuvilja lisamist:", puuviljad)

print("Viimane väärtus:", puuviljad[-1])

puuviljad[1] = "õun"
print("Pärast elemendi muutmist:", puuviljad)

if "õun" in puuviljad:
    print("Õun eksisteerib listis.")
else:
    print("Õun ei eksisteeri listis.")

print("Listi pikkus:", len(puuviljad))

puuviljad.remove("banaan")
print("Pärast elemendi eemaldamist:", puuviljad)

puuviljad.reverse()
print("List pärast järjekorra muutmist vastupidiseks:", puuviljad)

puuviljad.sort()
print("Sorteeritud list:", puuviljad)