class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    def make_computations(self, operation, value):
        if operation == '+':
            result = self.__cpu + self.__memory
        elif operation == '-':
            result = self.__cpu - self.__memory
        elif operation == '*':
            result = self.__cpu * self.__memory
        elif operation == '/':
            if self.__memory != 0:
                result = self.__cpu / self.__memory
            else:
                result = "Division by zero is not allowed"
        else:
            result = "Invalid operation"
        return f"Result of {self.__cpu} {operation} {self.__memory} is {result}"
    
    def get_cpu(self):
        return self.__cpu

    def set_cpu(self, cpu):
        self.__cpu = cpu

    def get_memory(self):
        return self.__memory

    def set_memory(self, memory):
        self.__memory = memory

    def info(self):
        return f"Computer - CPU: {self.__cpu}, Memory: {self.__memory}"


class Laptop(Computer):
    def __init__(self, cpu, memory, memory_card):
        super().__init__(cpu, memory)
        self.__memory_card = memory_card

    def get_memory_card(self):
        return self.__memory_card

    def set_memory_card(self, memory_card):
        self.__memory_card = memory_card

    def info(self):
        return f"Laptop - CPU: {self.get_cpu()}, Memory: {self.get_memory()}, Memory Card: {self.__memory_card}"


comp = Computer(4, 8)
laptop = Laptop(2, 16, 256)


print(comp.info())
print(laptop.info())

print(comp.make_computations('+', 3))
print(laptop.make_computations('-', 5))


comp.set_cpu(6)
laptop.set_memory(32)
laptop.set_memory_card(512)


print(comp.info())
print(laptop.info())
