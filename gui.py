import tkinter as tk
from Timer import Timer

from attr import s
from Lingo import Lingo

import tkinter as tk

class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()
        self.ronde = Lingo()
        self.timer = None

        # Labels
        self.score_entry = tk.Label()
        self.score_entry.pack()

        self.status = tk.Label()
        self.status.pack()

        self.beurten = tk.Label()
        self.beurten.pack()
        self.woord = ""

        # Vars
        # Create the application variable.
        self.contents = tk.StringVar()
        self.status_txt = tk.StringVar()
        self.status_txt.set("Start met raden!")
        self.status["textvariable"] = self.status_txt

        self.score = tk.StringVar()
        self.score.set("Geen vorige score...")
        self.score_entry["textvariable"] = self.score

        # Set it to some value.
        self.contents.set("Beurten over: 5")
        # Tell the entry widget to watch this variable.
        self.beurten["textvariable"] = self.contents

        # wide entry
        self.inp1 = tk.StringVar()
        self.inp2 = tk.StringVar()
        self.inp3 = tk.StringVar()
        self.inp4 = tk.StringVar()
        self.inp5 = tk.StringVar()

        self.entry1 = tk.Entry(width=100, textvariable=self.inp1)
        self.entry2 = tk.Entry(width=100, textvariable=self.inp2)
        self.entry3 = tk.Entry(width=100, textvariable=self.inp3)
        self.entry4 = tk.Entry(width=100, textvariable=self.inp4)
        self.entry5 = tk.Entry(width=100, textvariable=self.inp5)
        self.entry1.pack()
        self.entry2.pack()
        self.entry3.pack()
        self.entry4.pack()
        self.entry5.pack()
        # Dit kon waarschijnlijk VEEL makkelijker hahahahhahhahahahhahahahahhahhahahahhahahahahhahhahahahhahahahahhahhahahahhahahahahhahhahahahhahahahahhahhahahahhahahahahhahhahahahhahahahahhahhahahahhahahahahhahhahahahhahahahahhahhahahahhahahahahhahhahahahhahahahahhahhahahahhahahahahhahhahahahhahahahahhahhahahahha
        self.entry1.bind("<Return>", self.check1)
        self.entry2.bind("<Return>", self.check2)
        self.entry3.bind("<Return>", self.check3)
        self.entry4.bind("<Return>", self.check4)
        self.entry5.bind("<Return>", self.check5)

        # Create a button.
        self.button = tk.Button(text="Reset", command=self.reset)
        self.button.pack()
        
        self.reset()

    # Check inputs van fields
    def check1(self, event):
        i = self.inp1.get()
        self.entry1.config(state="disabled")
        print(i)
        status = self.check(i)
        print(status)

        self.status_txt.set(status["m"])

        if status["e"]:
            self.entry1.config(state="normal")
        else: 
            self.contents.set(f"Beurten over: {status['b']}")

            if status["f"]:
                print(self.kill_timer_and_get_time())
            
            if status["c"] and status["f"] == False:
                self.status_txt.set(f"Het correcte woord was: {status['c']}")

    # Check inputs van fields
    def check2(self, event):
        i = self.inp2.get()
        self.entry2.config(state="disabled")
        print(i)
        status = self.check(i)
        print(status)

        self.status_txt.set(status["m"])

        if status["e"]:
            self.entry2.config(state="normal")
        else: 
            self.contents.set(f"Beurten over: {status['b']}")

            if status["f"]:
                print(self.kill_timer_and_get_time())
            
            print(status)

            if status["c"] and status["f"] == False:
                self.status_txt.set(f"Het correcte woord was: {status['c']}")

    # Check inputs van fields
    def check3(self, event):
        i = self.inp3.get()
        self.entry3.config(state="disabled")
        print(i)
        status = self.check(i)
        print(status)

        self.status_txt.set(status["m"])

        if status["e"]:
            self.entry3.config(state="normal")
        else: 
            self.contents.set(f"Beurten over: {status['b']}")

            if status["f"]:
                print(self.kill_timer_and_get_time())
            
            if status["c"] and status["f"] == False:
                self.status_txt.set(f"Het correcte woord was: {status['c']}")

    # Check inputs van fields
    def check4(self, event):
        i = self.inp4.get()
        self.entry4.config(state="disabled")
        print(i)
        status = self.check(i)
        print(status)

        self.status_txt.set(status["m"])

        if status["e"]:
            self.entry4.config(state="normal")
        else: 
            self.contents.set(f"Beurten over: {status['b']}")

            if status["f"]:
                print(self.kill_timer_and_get_time())
            
            if status["c"] and status["f"] == False:
                self.status_txt.set(f"Het correcte woord was: {status['c']}")

    # Check inputs van fields
    def check5(self, event):
        i = self.inp5.get()
        self.entry5.config(state="disabled")
        print(i)
        status = self.check(i)
        print(status)

        self.status_txt.set(status["m"])

        if status["e"]:
            self.entry5.config(state="normal")
        else: 
            self.contents.set(f"Beurten over: {status['b']}")

            if status["f"]:
                print(self.kill_timer_and_get_time())
            
            if status["c"] and status["f"] == False:
                self.status_txt.set(f"Het correcte woord was: {status['c']}")

    # Check inputs van fields
    def check(self, inp):
        return self.ronde.guess(inp)

    def calc_score(self, time, beurten):
        t = beurten * time

        print(t, time, beurten)

        return t

    # Hahahahahhaha VERMOORD de timer en pak score :)
    def kill_timer_and_get_time(self):
        if self.timer:
            t = self.timer.time_elapsed
            self.timer.stop()
            self.timer.reset()
            self.timer = None
            print(self.ronde.current_attempts)
            score = self.calc_score(t, self.ronde.current_attempts)
            print(f"SCORE: {score}")
            self.score.set(f"Jou score: {score}")

            return score
        else:
            return 0

    # Reset de ronde
    def reset(self):
        print("Reset")

        if self.timer is not None:
            self.kill_timer_and_get_time()

        self.timer = Timer()
        self.timer.start()

        self.ronde = Lingo()
        self.contents.set("Beurten over: 5")
        self.status_txt.set("Start met raden!")
        self.entry1.config(state="normal")
        self.entry2.config(state="normal")
        self.entry3.config(state="normal")
        self.entry4.config(state="normal")
        self.entry5.config(state="normal")

        self.inp5.set("")
        self.inp4.set("")
        self.inp3.set("")
        self.inp2.set("")
        self.inp1.set("")

        print("KLAAR OM TE SPELEN")

        print(f"WOORD OM TE RADEN IS: {self.ronde.woord}")

root = tk.Tk()
myapp = App(root)
myapp.mainloop()