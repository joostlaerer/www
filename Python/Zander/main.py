import Skrivut
import Syntax

def hoved():

    svar = int(input("skriv inn forsøket ditt: "))
    Syntax.sjekker(svar)
    if svar == "1":
        Skrivut.gratulerer()

hoved()
