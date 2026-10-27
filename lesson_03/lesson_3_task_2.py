from smartphone import Smartphone

catalog = [
    Smartphone("Apple iPhone", "15 Pro Max", "+79738291643"),
    Smartphone("Samsung Galaxy", "S25 Ultra", "+79845623712"),
    Smartphone("Xiaomi", "15 Ultra", "+79645097452"),
    Smartphone("realme", "GT 7 Pro", "+79534218465"),
    Smartphone("HONOR", "400 Pro", "+796452834152")
]

for smartphone in catalog:
    print(smartphone.marka + " - " + smartphone.model + ". " + smartphone.number)