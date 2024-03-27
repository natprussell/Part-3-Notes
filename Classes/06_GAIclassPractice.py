import tkinter as tk

class TranslatorApp:
    def __init__(self, master):
        self.master = master
        master.title("Translator App")

        self.label = tk.Label(master, text="Translate Here", font=("Helvetica", 16))
        self.label.pack()

        self.english_button = tk.Button(master, text="English", command=self.translate_english)
        self.english_button.pack(side=tk.LEFT, padx=5)

        self.spanish_button = tk.Button(master, text="Spanish", command=self.translate_spanish)
        self.spanish_button.pack(side=tk.LEFT, padx=5)

        self.french_button = tk.Button(master, text="French", command=self.translate_french)
        self.french_button.pack(side=tk.LEFT, padx=5)

        self.german_button = tk.Button(master, text="German", command=self.translate_german)
        self.german_button.pack(side=tk.LEFT, padx=5)

    def translate_english(self):
        self.label.config(text="Hello")

    def translate_spanish(self):
        self.label.config(text="Hola")

    def translate_french(self):
        self.label.config(text="Bonjour")

    def translate_german(self):
        self.label.config(text="Hallo")

if __name__ == "__main__":
    root = tk.Tk()
    app = TranslatorApp(root)
    root.mainloop()
