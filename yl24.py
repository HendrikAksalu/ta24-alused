# UPC vöötkoodi kontrollsumma arvutamise ülesanne. Alusta algoritmi koostamisest. 
# Kommentaarides on kah lahendused, aga proovi ise lahendada. 
# Defineeri kontrollsumma arvutamise funktsioon. (https://www.w3schools.com/python/python_functions.asp)

def upc_check(code):

    code = upc_check.zfill(11)
    print(code)
    
    res = 0

    for i in range(0, 11, 2):
        # print(code[i])
        res += int(code[i])

    res *= 3
    
    for i in range(1, 10, 2):
        # print(code[i])
        res += int(code[i])

    res %= 10

    if res != 0:
        res = 10 - res

    return res
       
print(upc_check("03600029145"))

