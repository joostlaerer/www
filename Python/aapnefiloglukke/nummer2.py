def aapneOgLukkeFil(filename):
    f = open(filename,"w")
    
    try:
        f.write("hello!")
    except:
        print("Noe gikk feil")
    f.close()

aapneOgLukkeFil("test.txt")