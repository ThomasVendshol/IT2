import os
import sys
import json
from politiker import Politiker
 
def rens_terminal():
    if sys.platform == "Windows":
        os.system("cls")
    else:
        os.system("clear")

# 1. Oppsett
# Åpner json_fila og putter alt innholder i variabelen data        
with open("representanter.json", "r", encoding="utf-8") as fil:
    data = json.load(fil)
representanter = data["dagensrepresentanter_liste"] # henter ut lista med representater

# Opretter en liste med politiker-objekter (objekter av klassen Politiker):
politikere = []
for politiker_ordbok in representanter:
    ny_politiker = Politiker(politiker_ordbok)
    politikere.append(ny_politiker)


print("-- Velkommen til Stortinget-fantasy --") 

while True:
    rens_terminal()
    print("-- Stortinget-fantasy --")  
    print("1: Politikeroversikt")
    print("2: Avslutt")
    brukervalg = input(">")
 
    if brukervalg == "1":
        print("-- Politikeroversikt --")
        for politiker in politikere:
            print(politiker)
        input("Trykk enter for å gå tilbake til hovedmenyen")
    elif brukervalg == "2":
        print("Avslutter..")
        break # bryter ut av while-løkken
    else:
        print("Ugyldig input")
        