print("Hei, velkommen til quizen")

class Spørsmål:
    def __init__(self, spørsmål_text, svar):
        self.spørsmål_text = spørsmål_text
        self.svar = svar

quiz_spørsmål = [
    Spørsmål("Question 1: Er drake fra USA eller Canada?", "Canada"),
    Spørsmål("Question 2: Hvor gammel var Kurt Cobain da han døde?", "27"),
    Spørsmål("Question 3: Hva er hovedstaden i Portugal", "Lisbon")
]

for spørsmål in quiz_spørsmål:
    print(spørsmål.spørsmål_text)
    user_input = input("Svaret ditt: ")
    if user_input.lower() == spørsmål.svar.lower():
        print("Riktig")
    else:
        print(f"Dessverre, svaret er: {spørsmål.answer}.")