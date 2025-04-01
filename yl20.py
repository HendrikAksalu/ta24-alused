# Väljasta korduslause abil 8 korrutis arvudega 0..12 ja vorminda väljund nii:
# 8 x 0 = 0
# 	8 x 1 = 8
# 	8 x 2 = 16
# 	…
# 	8 x 12 = 96
# Täienda programmi nii, et kasutajalt küsitakse arv x, mille kohta korrutustabel väljastatakse

a = int(input("Sisestage arv: "))

for x in range(0, 13): # for x in range(0, 13): → tsükkel käib läbi arvud 0 kuni 12.
    print(a, "x", x, "=", a*x)
# a*x → korrutab kasutaja sisestatud arvu a tsükli väärtusega x.