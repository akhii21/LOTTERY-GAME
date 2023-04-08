import tkinter as tk
import random

class LotteryGame(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Lottery Game")
        self.pack()
        self.create_widgets()
        self.lottery_numbers = []

    def create_widgets(self):
        self.label = tk.Label(self, text="Select 6 numbers between 1 and 49:", bg="#e6f7ff")
        self.label.pack()

        self.entry_frame = tk.Frame(self, bg="#e6f7ff")
        self.entry_frame.pack()

        self.number_entries = []
        for i in range(6):
            entry = tk.Entry(self.entry_frame, width=3)
            entry.pack(side=tk.LEFT, padx=5, pady=5)
            self.number_entries.append(entry)

        self.button = tk.Button(self, text="Play", command=self.play_lottery, bg="#99c2ff", fg="blue")
        self.button.pack(pady=10)

    def play_lottery(self):
        try:
            user_numbers = []
            for entry in self.number_entries:
                number = int(entry.get())
                if number < 1 or number > 49:
                    raise ValueError("Number must be between 1 and 49.")
                user_numbers.append(number)
        except ValueError as e:
            self.label.config(text=str(e))
            return

        self.lottery_numbers = random.sample(range(1, 50), 6)
        matching_numbers = set(self.lottery_numbers).intersection(user_numbers)
        if matching_numbers:
            prize = 1000 * len(matching_numbers)
            self.label.config(text=f"The lottery numbers are: {self.lottery_numbers}\n"
                                   f"Your numbers are: {user_numbers}\n"
                                   f"Matching numbers: {matching_numbers}\n"
                                   f"Congratulations, you won {prize} dollars!", bg="#b3ffb3")
        else:
            self.label.config(text=f"The lottery numbers are: {self.lottery_numbers}\n"
                                   f"Your numbers are: {user_numbers}\n"
                                   f"No matching numbers, better luck next time!", bg="#ffe6e6")

root = tk.Tk()
root.configure(bg="#e6f7ff")
app = LotteryGame(master=root)
app.mainloop()
