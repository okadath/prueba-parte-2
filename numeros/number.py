class NumberSet:
    def __init__(self):
        self.numbers = set(range(0, 101))
        self.extracted_number = None

    def extract(self, number):
        if not (0 <= number <= 100):
            raise ValueError("El número debe estar entre 1 y 100.")
        if number in self.numbers:
            self.numbers.remove(number)
            self.extracted_number = number
        else:
            raise ValueError(f"El número {number} ya fue extraído o no está en el conjunto.")

    def find_missing_number(self):
        if self.extracted_number is None:
            return "No se ha extraído ningún número aún."
        return self.extracted_number
