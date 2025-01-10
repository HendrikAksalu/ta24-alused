# Koosta dictionary vähemalt viie endale iseloomuliku tunnusega (näiteks: eesnimi, perenimi, sünniaasta, elukoht, lemmik magustoit).
# Väljasta elukoht kahel erineval viisil (kasutades get() meetodit ja mitte kasutades seda).
# Muuda magustoidu väärtust.
# Tee kordus üle dictionary ja väljasta kõik võtmed.
# Tee kordus üle dictionary ja väljasta kõik väärtused (pööra tähelepanu sellele, et saab mitmel viisil, proovi erinevaid võimalusi).
# Kontrolli, kas isikukood on dictionary's olemas.
# Leia dictionary suurus (elementide arv).
# Lisa element enda pikkuse jaoks.
# Eemalda element sünniaasta (pane tähele, et saab mitut moodi).
# Pane tähele, et del võtmesõnaga on võimalik kogu dictionary kustutada.
# Saa aru ja katseta del võtmesõna ja clear meetodi erinevusest.
# Tutvu kõigi dictionary meetoditega.
# Läbi ülesanne juhendi lõpus.
# https://www.w3schools.com/python/python_dictionaries.asp

dict = {
    "first_name" : "Mati",
    "last_name" : "Maasikas",
    "year_of_birth" : 1946,
    "address" : "Karu 8, Tõrva",
    "fav_dessert" : "koogel-moogel",
}
#
print(dict["address"])
print(dict.get("address"))

#
dict["fav_dessert"] = "kohupiim"
print(dict)

#
for k in dict:
    print(k)

#
for i in dict.keys():
    print(i)

#
for k in dict:
    print(dict[k])

#
for v in dict.values():
    print(v)

#
if "nin" in dict.keys():
    print("isikukood on olemas")
else:
    print("isikukoodi ei ole")

#
print(len(dict))

#
dict["height"] = 155
print(dict)

dict.update({"height":160})

dict.pop("year_of_birth")
print(dict)

del dict["address"]
print(dict)



