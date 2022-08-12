import subprocess


def opentabs(antall_tabs):
    teller=1
    while(teller<antall_tabs):
            processes = subprocess.run(['C:\Program Files\Google\Chrome\Application\chrome.exe', '--incognito', 'https://chelseafc.3ddigitalvenue.com/login'])
            teller=teller+1

#lager ett nytt vindu. Dette kan vi bruke for å stacke vinduer over hverandre. Vi bør klare minst 4 vinduer.
def openwindows (antall_vinduer,tabs):
    teller=1
    while(teller<antall_vinduer):
            process = subprocess.run(['C:\Program Files\Google\Chrome\Application\chrome.exe', '--incognito','--new-window', 'https://chelseafc.3ddigitalvenue.com/login'])
            opentabs(tabs)
            teller=teller+1

def hoved():
    antall_input_tabs = int(input("Skriv inn antall faner: "))
    antall_input_windows =int(input("Skriv inn antall vinduer"))
    openwindows(antall_input_windows,antall_input_tabs)
    #opentabs(antall_input_tabs)


hoved()