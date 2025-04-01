# Küsi kasutajalt lemmikloom. Väljasta selle muutuja esimene täht.
# Koosta list, mis koosneb kolmest loomast.
# Lisa selle listi lõppu kasutaja sisestatud lemmikloom.
# Väljasta see lemmikloomade list.
# Väljasta listi viimase elemendi viimane täht.
# (sõne kui list, mitmemõõtmeline ilist - multi dimensional)

lemmikloom = input("lemmikloom: ")

print(lemmikloom[0])

lemmikloomade_list = ["kass", "jänes", "papagoi"]
print()

lemmikloomade_list.append(lemmikloom)
#.append() on Pythonis meetod, mida kasutatakse loendisse (list) uue elemendi lisamiseks. See lisab uue elemendi loendi lõppu.

print("lemmikloomade_list:", lemmikloomade_list)

print("Viimase elemendi viimane täht:", lemmikloomade_list[-1][-1])