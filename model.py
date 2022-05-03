from datetime import date

class Stanje:
    def __init__(self, kategorije):
        self.kategorije = kategorije

    def dodaj_kategorijo(self, kategorija):
        self.kategorije.append(kategorija)


class Kategorija:
    def __init__(self, ime, opravila):
        self.ime = ime
        self.opravila = opravila

    def stevilo_neopravljenih(self):
        neopravljena = 0
        for opravilo in self.opravila:
            if not opravilo.opravljeno:
                neopravljena += 1
        return neopravljena

    def dodaj_opravilo(self, opravilo):
        self.opravila.append(opravilo)


class Opravilo:
    def __init__(self, opis, rok=None, opravljeno=False):
        self.opis = opis
        self.rok = rok
        self.opravljeno = opravljeno


    def opravi(self):
        self.opravljeno = True


    def zamuja(self):
        return not self.opravljeno and self.rok and self.rok < date.today()
