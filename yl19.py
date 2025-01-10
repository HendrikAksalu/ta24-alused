# Leia muutuja abil etteantud tekstis olevate täishäälikute (a, e, i, o, u, õ, ä, ö, ü) arv.

vowels = "aeiouõäöü"
text = "Kuressaare Ametikool"
count = 0

for c in text.lower():
    
    if c in vowels:
        print(c)
        count += 1

print(count)