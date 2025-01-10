# Kivi-paber-käärid mäng. 
# Arvuti mõtleb välja ühe variandi - kivi, paber või käärid. Arvuti küsib kasutaja valikut. Programm ütleb, kes võitis.
# Täienda programmi nii, et mängitakse seni, kuni kasutaja ei taha enam mängida.


import random

choices = ["kivi", "paber", "käärid"]


while True:
   
    random_choice = random.choice(choices)
   
    input_choice = input("Vali kivi, paber või käärid: ").lower()
   
    if input_choice not in choices:
        print("Palun vali kivi, paber või käärid.")
        continue
     
    if input_choice == random_choice:
        print("Viik!")
    elif (input_choice == "kivi" and random_choice == "käärid") or \
         (input_choice == "paber" and random_choice == "kivi") or \
         (input_choice == "käärid" and random_choice == "paber"):
        print("Võitsid!")
    else:
        print("Arvuti võitis!")
    

    again = input("Kas soovid mängida uuesti? (jah/ei): ").lower()
    if again != "jah":
        print("Aitäh mängimast! Head päeva!")
        break
