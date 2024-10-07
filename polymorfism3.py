from typing import Protocol

class Spelfigur(Protocol):
    def rör_sig(self):
        pass

class Spelare:
    def rör_sig(self):
        print("Spelaren rör sig framåt.")

class Fiende:
    def rör_sig(self):
        print("Fienden rör sig mot spelaren.")

def uppdatera(figur: Spelfigur):
    figur.rör_sig()

spelare = Spelare()
fiende = Fiende()

uppdatera(spelare)  # Output: Spelaren rör sig framåt.
uppdatera(fiende)   # Output: Fienden rör sig mot spelaren.
