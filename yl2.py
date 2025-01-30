# Kirjuta programm, mis küsib kasutajalt raadiuse ja arvutab ringi pindala ja ümbermõõdu. (math.pi)

import math

radius = int(input("Sisesta raadius: "))
circumference = math.pi *radius** 2 # Math.pi konstant tagastab pi väärtuse: 3.141592653589793.
area = 2 *math.pi* radius

print("Ringi ümbermõõt on: ", round(circumference, 2)) 
print("Ringi pindala on: ", round(area, 2)) 