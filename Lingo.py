import random
wordList = ["lingo"]


class Lingo():
    def __init__(self):
        self.woord = random.choice(wordList).lower()
        self.min_len = 5
        self.attempts = 5

    def player(self):
        for i in range(self.attempts):
            inp = input("Raad het woord: ")
            print(self.guess(inp))
            if self.attempts == i:
                print("5 beurten gebruikt, het woord was: " + self.woord)
                break
    def guess(self, inp):
        inp = inp.lower()
        if len(inp) < self.min_len:
            return f"Woorden moeten {self.min_len} karakters lang zijn"
        elif len(inp) > self.min_len:
            return f"Woorden moeten {self.min_len} karakters lang zijn"

        if inp != self.woord:
            output = ""
            for i in range(len(inp)):
                if inp[i] == self.woord[i]:
                    output += inp[i]
                elif inp[i] in self.woord:
                    output += inp[i]
                else:
                    output += "_"
            return output

        else: 
            return "Gewonnen!"

lin = Lingo()
lin.player()