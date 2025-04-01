# Kirjuta programm, mis küsib kasutajalt failinime kujul “failinimi.ext” 
# (ext - extension - faili laiend) ja prindib välja laiendi (“ext”). (str.split)

filename = input("failinimi.ext: ")
splitted_filename = filename.split(".") #.split() on Pythonis stringi meetod, mida kasutatakse teksti jagamiseks väiksemateks osadeks.
print(splitted_filename[-1])

