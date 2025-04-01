# Arvu arvamise mäng. 
# Arvuti mõtleb välja arvu nullist sajani. Lase kasutajal pakkuda, mis arvu arvuti välja mõtles. 
# Vale pakkumise korral annab arvuti vihje, kas pakkumine on õigest arvust suurem või väiksem. 
# Pakkuda saab seni, kuni kasutaja on õige arvu pakkunud. (juhuarv - random)
# import random
# print(random.randrange(0, 100)) võib ka


import random # juhusliku arvu genereerimiseks

while True: # mäng käib uuesti, kuni kasutaja soovib lõpetada.
    random_num = random.randint(0, 100)
    # genereerib arvu, mida kasutaja peab ära arvama. 
    print(random_num)

    input_num = -1

    while input_num != random_num:
    #sisemine tsükkel, mis kestab seni, kuni õige number leitakse.

        input_num = int(input("Sisesta täisarv vahemikus 0 - 100: "))
    
        if not (0 <= input_num <= 100):
            print("Sisestatud arv ei jää vahemikku 0 - 100. Proovi uuesti.")
            continue

        if input_num < random_num: # annavad vihje, kas õige arv on suurem või väiksem.
            print("Õige arv on suurem, proovi uuesti.")
        else:
            print("Õige arv on väiksem, proovi uuesti.")

    print("Õige vastus!")

    if input("Kas soovid uuesti mängida? y - jah, n - ei: ").lower() == "n": 
        break
    # küsib, kas mängida uuesti või lõpetada.
        
