#Faile kursas.py
# sukurti objekto klasę Kursas, # #kuri turėtų savybes pavadinimas, destytojas, trukme,
# taip pat metodą destyti(), kuris spausdintų „Vyksta mokymas!“
from dataclasses import dataclass

@dataclass
class Kursas:
    pavadinimas : str
    destytojas : str
    trukme : str

    def destyti(self):
        print("Vyksta mokymas!")