import random
wordList = ["lingo"]
import sqlite3

sql = sqlite3.connect("lingo.sqlite3")

class Lingo():
    def __init__(self):
        self._build_db()

        self.woord = self.dynamic_word()
        self.min_len = 5
        self.attempts = 5
        self.current_attempts = 0

    # Console player, voor testing (deprecated)
    def player(self):
        for i in range(self.attempts):
            inp = input("Raad het woord: ")
            print(self.guess(inp))
            if self.attempts == i:
                print("5 beurten gebruikt, het woord was: " + self.woord)
                break

    # Init db
    def _build_db(self):
        print("BUILDING DB")
        cur = sql.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS words (word TEXT)")
        with open("words.txt") as f:
            for line in f:
                # check if word is already in db
                i = cur.execute("SELECT * FROM words WHERE word = ?", (line,))

                if i.fetchone() is None:
                    cur.execute("INSERT INTO words VALUES (?)", (line,))

        sql.commit()
        cur.close()
        print("DB BUILT")

    # Pakt een random woord uit de db
    def dynamic_word(self): 
        cur = sql.cursor()
        # get random word from `words`
        cur.execute("SELECT word FROM words ORDER BY RANDOM() LIMIT 1")
        word = cur.fetchone()[0]

        print(word)
        return word

    # Deze code moest ik te vaak gebruiken
    def win_msg(self):
        print("WOORD GEVONDEN")
        return {
            "m": "Gewonnen!",
            "e": False,
            "f": True,
            "c": self.woord,
            "b": self.attempts - self.current_attempts
        }

    # Logica voor een 'guess'
    def guess(self, inp):
        inp = inp.lower()
        if len(inp) < self.min_len:
            return {
                "m": f"Woorden moeten {self.min_len} karakters lang zijn",
                "e": True
            }
        elif len(inp) > self.min_len:
            return {
                "m": f"Woorden moeten {self.min_len} karakters lang zijn",
                "e": True
            }

        if self.attempts == self.current_attempts:
            return {
                "m": f"Het woord was: {self.woord}",
                "e": True
            }

        self.current_attempts += 1

        correct_word = None

        if self.current_attempts == self.attempts:
            correct_word = self.woord

        print(inp, self.woord)
        print(inp!=self.woord)


        if inp is self.woord:
            print("WOORD GEVONDEN")
            return self.win_msg()

        if inp != self.woord:
            output = ""
            for i in range(len(inp)):
                if inp[i] == self.woord[i]:
                    output += inp[i]
                elif inp[i] in self.woord:
                    output += inp[i]
                else:
                    output += "_"
            # check if output contains no _
            if "_" not in output:
                return self.win_msg()

            return {
                "m": output,
                "e": False,
                "f": False,
                "b": self.attempts - self.current_attempts,
                "c": correct_word
            }

        else: 
            print("WOORD GEVONDEN")
            return self.win_msg()