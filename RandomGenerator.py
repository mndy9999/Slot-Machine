from random import randint

class Generator():
    symbols = ("Seven", "Bell", "Melon", "Plum", "Orange", "Lemon", "Cherry")
    counter = {symbols[0]:0, symbols[1]:0, symbols[2]:0, symbols[3]:0, symbols[4]:0, symbols[5]:0, symbols[6]:0}

    def generateElement(self):
        return randint(0, 99)
    
    def checkElement(self, element):
        if 0 <= element <= 9:
            self.counter[self.symbols[0]] +=1
            return self.symbols[0]
        elif 10 <= element <= 24:
            self.counter[self.symbols[1]] +=1
            return self.symbols[1]
        elif 25 <= element <= 44:
            self.counter[self.symbols[2]] +=1
            return self.symbols[2]
        elif 45 <= element <= 69:
            self.counter[self.symbols[3]] +=1
            return self.symbols[3]
        elif 70 <= element <= 84:
            self.counter[self.symbols[4]] +=1
            return self.symbols[4]
        elif 85 <= element <= 94:
            self.counter[self.symbols[5]] +=1
            return self.symbols[5]
        elif 95 <= element <= 99:
            self.counter[self.symbols[6]] +=1
            return self.symbols[6]

    def getCountNumber(self):
        for i in range(0, len(self.symbols)):
            print(self.symbols[i], ": ", self.counter[self.symbols[i]])


def main():
    gen = Generator()
    for i in range(0, 15):
        element = gen.generateElement()
        print(gen.checkElement(element))
    gen.getCountNumber();

main()