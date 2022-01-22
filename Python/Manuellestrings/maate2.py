""" Program som spytter ut en string """
def skrivInnInfo():
    fnavn=input ("Skriv inn fornavnet navnet ditt: ")
    enavn=input ("Skriv inn etternavnet ditt: ")
    bursdag= input ("Skriv inn når du har bursdag: ")
    """ Bruk heller fstrings """
    print(f"Fornavnet ditt er: {fnavn} Etternavnet ditt er: {enavn} Du har bursdag: {bursdag}")
if __name__ == "__main__":
    skrivInnInfo()