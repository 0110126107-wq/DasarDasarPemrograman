#NOMOR 1
def celcius_ke_fahrenheit(celcius):
    hasil=(celcius*(9/5))+32
    print(hasil)
    
celcius_ke_fahrenheit(0)
celcius_ke_fahrenheit(100)


#NOMOR 2
def is_genap(bilangan):
    print(bilangan % 2 == 0)

is_genap(4)
is_genap(7)


#NOMOR 3
def nilai(score):
    if score >= 80 :
       print("LULUS")
    elif score <= 60:
        print("GAGAL")
    else:
        print("nilai kamu pas pasan")

nilai(90)
nilai(71)
nilai(40)


#NOMOR 4
def bilangan(angka):
    for i in range(1, angka+1):
        if i % 2 != 0:
            print(i, end="")
bilangan(20)    