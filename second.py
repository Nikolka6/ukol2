def cislo_text(cislo):
    cislo = int(cislo)

    jednotky = ["", "jedna", "dva", "tři", "čtyři", "pět", "šest", "sedm", "osm", "devět"]
    desitky = ["", "deset", "dvacet", "třicet", "čtyřicet", "padesát", "šedesát", "sedmdesát", "osmdesát", "devadesát"]
    teen = ["deset", "jedenáct", "dvanáct", "třináct", "čtrnáct", "patnáct", "šestnáct", "sedmnáct", "osmnáct", "devatenáct"]

    if cislo == 0:
        return "nula"

    if cislo < 0 or cislo > 999:
        return "číslo mimo rozsah"

    vysledek = ""

    if cislo >= 100:
        stovky = cislo // 100

        if stovky == 1:
            vysledek = "sto"
        elif stovky == 2:
            vysledek = "dvě stě"
        elif stovky == 3:
            vysledek = "tři sta"
        elif stovky == 4:
            vysledek = "čtyři sta"
        else:
            vysledek = jednotky[stovky] + " set"

        cislo = cislo % 100

        if cislo > 0:
            vysledek += " "

    if cislo >= 10 and cislo < 20:
        vysledek += teen[cislo - 10]
    else:
        desitka = cislo // 10
        jednotka = cislo % 10

        if desitka > 0:
            vysledek += desitky[desitka]

        if jednotka > 0:
            if desitka > 0:
                vysledek += " "
            vysledek += jednotky[jednotka]

    return vysledek


print(cislo_text(0))
print(cislo_text(1))
print(cislo_text(15))
print(cislo_text(25))
print(cislo_text(100))
