from abc import ABC, abstractmethod

class Produkt(ABC):
    def __init__(self, namn, pris):
        self._namn = namn
        self._pris = pris

    @abstractmethod
    def beskrivning(self):
        pass

    def get_namn(self):
        return self._namn

    def set_namn(self, namn):
        if namn == self._namn:
            print("Kan inte ändra till samma namn!")
            return
        self._namn = namn

    def get_pris(self):
        return self._pris

    def set_pris(self, pris):
        if pris <= 0:
            print("Ogiltligt pris! Måste vara positivt!")
            return
        self._pris = pris

class Bok(Produkt):
    def __init__(self, namn, pris, författare):
        super().__init__(namn, pris)
        self._författare = författare

    def get_författare(self):
        return self._författare

    def beskrivning(self):
        return f"Boken '{self._namn}' av {self._författare}, pris: {self._pris} kr"

class Elektronik(Produkt):
    def __init__(self, namn, pris, märke):
        super().__init__(namn, pris)
        self._märke = märke

    def get_märke(self):
        return self._märke

    def beskrivning(self):
        return f"Elektronisk enhet '{self._namn}' från {self._märke}, pris: {self._pris} kr"

class Kläder(Produkt):
    def __init__(self, namn, pris, storlek):
        super().__init__(namn, pris)
        self._storlek = storlek

    def get_storlek(self):
        return self._storlek

    def beskrivning(self):
        return f"Klädesplagg '{self._namn}' i storlek {self._storlek}, pris: {self._pris} kr"

# Exempel på användning

class Företag:
    def __init__(self, namn) -> None:
        self.namn = namn

    def beskrivning(self):
        print(f"Här är en beskrivning av {self.namn}!")

produkter = [
    Bok("Lär dig Python", 299, "Anna Svensson"),
    Elektronik("Laptop", 8999, "TechBrand"),
    Kläder("Jeans", 499, "L")
]

skola = Företag("Teknikhögskolan")
skola2 = Företag({"Namn":"Teknikhöskolan", "Address":"ASDafsddsfa"})

for produkt in produkter:
    print(produkt.beskrivning())

def print_beskrivning(objeken):
    for obj in objeken:
        obj.beskrivning()

# print_beskrivning([produkt,[skola]]) # < [bok, elektronik, kläder, [skola]]
print_beskrivning([produkt]+[skola]) # < [bok, elektronik, kläder, skola]

print(skola.namn)
print(skola2.namn)