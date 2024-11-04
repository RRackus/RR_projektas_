#	Faile main.py importuoti PythonKursas modulį (failą)
#	Faile main.py inicijuoti Kursas objektą su norimomis savybėmis
#	Faile main.py inicijuoti PythonKursas objektą su norimomis savybėmis
#	Paleisti abiejų objektų metodą destyti()
#import python_kursas
#import kursas

import os, sys, subprocess

from modules.python_kursas import Kursas, PhytonKursas
#from models.kursas import Kursas, PhytonKursas
#from python_kursas import PhytonKursas

if __name__ == "__main__":

    class Mokymai:
        def __init__(self):
            self.sarasas =[]

        def prideti_kursus(self):
            kurso_pavadinimas = input("Kurso pavadinimas:__ ")
            kurso_destytojas = input("Dėstytojo pavardė:__ ")
            kurso_trukme = input("Kurso trukme:__")
            self.komplektas = Kursas(kurso_pavadinimas, kurso_destytojas, kurso_trukme)
            self.sarasas.append(self.komplektas)

        def atspausdinti(self):
            for self.komplektas in self.sarasas:
                print(self.komplektas)

    #class destyti:    # cia negerai

kursu_sarasas = Mokymai()

kursu_sarasas.prideti_kursus()

print(kursu_sarasas.atspausdinti())


