**Uppgift: Utveckla ett Bibliotekshanteringssystem med OOP i Python**

Du ska skapa ett enkelt bibliotekshanteringssystem som använder sig av objektorienterad programmering i Python. Systemet ska kunna hantera böcker, medlemmar och lån.

---

### **Kravspecifikation:**

#### **1. Klasser att implementera:**

- **Bok**
  - **Attribut:**
    - `titel` (str)
    - `författare` (str)
    - `isbn` (str)
    - `tillgänglig` (bool)
  - **Metoder:**
    - `visa_info()` - Skriver ut information om boken.

- **Medlem**
  - **Attribut:**
    - `namn` (str)
    - `medlems_id` (int)
    - `lånade_böcker` (lista över Bok-objekt)
  - **Metoder:**
    - `låna_bok(bok)` - Lånar en bok om den är tillgänglig.
    - `lämna_tillbaka_bok(bok)` - Lämnar tillbaka en bok.
    - `visa_lånade_böcker()` - Visar alla böcker som medlemmen har lånat.

- **Bibliotek**
  - **Attribut:**
    - `böcker` (lista över Bok-objekt)
    - `medlemmar` (lista över Medlem-objekt)
  - **Metoder:**
    - `lägg_till_bok(bok)` - Lägger till en ny bok i biblioteket.
    - `ta_bort_bok(bok)` - Tar bort en bok från biblioteket.
    - `registrera_medlem(medlem)` - Lägger till en ny medlem.
    - `ta_bort_medlem(medlem)` - Tar bort en medlem.
    - `sök_bok_titel(titel)` - Söker efter böcker baserat på titel.
    - `sök_bok_författare(författare)` - Söker efter böcker baserat på författare.
    - `visa_tillgängliga_böcker()` - Visar alla tillgängliga böcker.

---

#### **2. Funktionalitet:**

- **Hantera Böcker:**
  - Lägga till och ta bort böcker i biblioteket.
  - Söka efter böcker baserat på titel eller författare.
  - Visa alla tillgängliga böcker.

- **Hantera Medlemmar:**
  - Registrera och ta bort medlemmar.
  - Visa en medlems lånade böcker.

- **Lånefunktioner:**
  - Medlemmar kan låna och lämna tillbaka böcker.
  - När en bok lånas ut ska den markeras som otillgänglig.
  - När en bok lämnas tillbaka ska den markeras som tillgänglig igen.

---

#### **3. Extra Utmaningar (Valfritt):**

- **Undantagshantering:**
  - Hantera fall där en medlem försöker låna en bok som inte är tillgänglig.
  - Hantera fall där en medlem försöker lämna tillbaka en bok som inte är lånad.

- **Arv och Polymorfism:**
  - Skapa en **Person**-klass som förälder till **Medlem** och eventuell **Anställd**-klass.
  - **Person** kan ha gemensamma attribut som `namn` och `personnummer`.

- **Uthyrningshistorik:**
  - Spåra historiken av lån för varje bok och medlem.

- **Grafiskt Gränssnitt:**
  - Implementera ett enkelt GUI med bibliotek som Tkinter.

---

#### **4. Testning:**

- Skapa testfall för att verifiera att alla metoder fungerar korrekt.
- Använd några exempeldata för att demonstrera systemets funktionalitet.

---

### **Instruktioner:**

- **Kodstruktur:**
  - Använd korrekta OOP-principer som inkapsling, arv och polymorfism.
  - Följ PEP 8-stilguiden för kodningsstandarder i Python.
  - Lägg till kommentarer för att förklara koden där det behövs.

- **Dokumentation:**
  - Skriv en README-fil som förklarar hur man kör programmet.
  - Beskriv vilka funktioner som är implementerade och hur de används.

---

### **Leverans:**

- Python-filer med all källkod.
- En README-fil med instruktioner och beskrivningar.
- Eventuella testfiler eller data som används för att demonstrera funktionaliteten.

---

**Lycka till med uppgiften!** Om du har några frågor eller behöver hjälp med specifika delar, tveka inte att be om hjälp.