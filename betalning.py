from abc import ABC, abstractmethod

class Betalning(ABC):
    @abstractmethod
    def bearbeta_betalning(self, belopp):
        pass

class Kortbetalning(Betalning):
    def bearbeta_betalning(self, belopp):
        print(f"Bearbetar kortbetalning på {belopp} SEK.")

class PayPalBetalning(Betalning):
    def bearbeta_betalning(self, belopp):
        print(f"Bearbetar PayPal-betalning på {belopp} SEK.")

class StripeBetalning(Betalning):
    def bearbeta_betalning(self, belopp):
        print(f"Enkelt implementerat allt för att kunna göra en betalning med stripe!")
        print(f"Bearbetar Stripe-betalning på {belopp} SEK.")

# Använd betalningsklasserna
kort = Kortbetalning()
kort.bearbeta_betalning(500)

paypal = PayPalBetalning()
paypal.bearbeta_betalning(300)

stripe = StripeBetalning()
stripe.bearbeta_betalning(400)
