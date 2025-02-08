class Asus:
    def __init__(self, model, processor, ram):
        self.model = model
        self.processor = processor
        self.ram = ram

    def display_info(self):
        return f"Model: {self.model}, Processor: {self.processor}, RAM: {self.ram}GB"


class Tuf(Asus):
    def __init__(self, model, processor, ram, battery_life):
        super().__init__(model, processor, ram)
        self.battery_life = battery_life

    def display_info(self):
        return super().display_info() + f", Battery Life: {self.battery_life} hours"


class Gaming(Asus):
    def __init__(self, model, processor, ram, gpu):
        super().__init__(model, processor, ram)
        self.gpu = gpu

    def display_info(self):
        return super().display_info() + f", GPU: {self.gpu}"


# Ob'ekt yaratish
tuf_laptop = Tuf("TUF A14", "Ryzen 7", 16, 10)
gaming_laptop = Gaming("TUF A14 Gaming", "Ryzen 9", 32, "RTX 4060")

# Ma'lumotlarni chiqarish
print(tuf_laptop.display_info())
print(gaming_laptop.display_info())
