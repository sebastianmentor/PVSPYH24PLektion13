from abc import ABC, abstractmethod

# Definiera en abstrakt klass
class Fågel(ABC):
    # Abstrakt metod (måste implementeras av underklasser)
    @property
    @abstractmethod
    def art(self):
        pass

    @art.setter
    @abstractmethod
    def art(self, art):
        pass

    @abstractmethod
    def ljud(self):
        """Måste se till att fågeln kan sjunga fint!"""
        pass

    # Vanlig metod (kan användas direkt)
    def flyg(self):
        print("Fågeln flyger.")

# Implementera en konkret klass som ärver från Fågel
class Papegoja(Fågel):
    def __init__(self, art) -> None:
        super().__init__()
        self._art = art

    @property
    def art(self):
        return self._art
    
    # @art.setter
    # def art(self, art):
    #     if len(art) > 10:
    #         return
    #     else:
    #         self._art = art

    # Implementera den abstrakta metoden
    def ljud(self):
        print("Papegojan säger hej!")

# Instansiera en konkret klass
papegoja = Papegoja('Underlat')
papegoja.ljud()  # Output: Papegojan säger hej!
papegoja.flyg()  # Output: Fågeln flyger.
print(papegoja.art)
papegoja.art = "Anka"

# class Pingvin(Fågel):
#     def ljud(self):
#         pass

#     def gå(self):
#         print("Pingvinen går!")

# pingvin = Pingvin()
# pingvin.flyg()
# pingvin.gå()
