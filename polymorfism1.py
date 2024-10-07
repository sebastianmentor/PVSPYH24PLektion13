class Djur:
    def ljud(self):
        pass  # Abstrakt metod som ska överlagras

class Hund(Djur):
    def ljud(self):
        return "Voff!"

class Katt(Djur):
    def ljud(self):
        return "Mjau!"
    
class Person:
    def skrik(self):
        return "Vrålar!!"
    
    def ljud(self):
        return "Viskar försiktigt"

# Använda polymorfism
def gör_ljud(djur):
    print(djur.ljud())

# Skapa objekt
hund = Hund()
katt = Katt()
sebastian = Person()

# Samma metod, olika beteende beroende på objektets typ
gör_ljud(hund)  # Output: Voff!
gör_ljud(katt)  # Output: Mjau!
gör_ljud(sebastian)  # Output: ????
