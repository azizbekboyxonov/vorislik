class Computer:
    def __init__(self, brand, processor):
        self.brand = brand
        self.processor = processor

    def display_info(self):
        return f"Brand: {self.brand}, Processor: {self.processor}"


class Laptop(Computer):
    def __init__(self, brand, processor, battery_life):
        super().__init__(brand, processor)
        self.battery_life = battery_life

    def display_info(self):
        return super().display_info() + f", Battery Life: {self.battery_life} hours"


class Desktop(Computer):
    def __init__(self, brand, processor, gpu):
        super().__init__(brand, processor)
        self.gpu = gpu

    def display_info(self):
        return super().display_info() + f", GPU: {self.gpu}"


class GamingPC(Laptop, Desktop):
    def __init__(self, brand, processor, battery_life, gpu, ram):
        Laptop.__init__(self, brand, processor, battery_life)
        Desktop.__init__(self, brand, processor, gpu)
        self.ram = ram

    def display_info(self):
        return super().display_info() + f", RAM: {self.ram}GB"


# Ob'ekt yaratish
gaming_pc = GamingPC("Asus", "Ryzen 9", 8, "RTX 4080", 32)

# Ma'lumotlarni chiqarish
print(gaming_pc.display_info())
