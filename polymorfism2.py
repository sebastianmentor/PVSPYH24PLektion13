class Anka:
    def kvacka(self):
        print("Ankan kvackar.")

class Person:
    def kvacka(self):
        print("Personen försöker kvacka som en anka.")

# Polymorfism via duck typing
def låt_kvacka(djur):
    djur.kvacka()

# Skapa objekt
anka = Anka()
person = Person()

# Samma metod, olika objekt
låt_kvacka(anka)   # Output: Ankan kvackar.
låt_kvacka(person)  # Output: Personen försöker kvacka som en anka.
