#	Faile python_kursas.py sukurti objekto klasę PythonKursas, kuri paveldėtų viską iš 
#klasės Kursas, bei perrašytų metodą destyti() taip, kad jis spausdintų „Vyksta programavimas!“
from dataclasses import dataclass
from kursas import Kursas

@dataclass
class PhytonKursas(Kursas):
    pavadinimas: str
    destytojas: str
    trukme: str


    def destyti(self):
        print("Vyksta programavimas!")
