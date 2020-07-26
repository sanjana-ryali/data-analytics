import tkinter as tk

class App(tk.Tk):
	def __init__(self):
		super().__init__()
		vcmd = self.register(self.validate_username)
		self.username = tk.Entry(self, validate="focusout", validatecommand=vcmd)
		self.btn = tk.Button(self, text="Click me!", command=self.say_hello)

		self.username.pack()
		self.btn.pack(padx=120, pady=30)

	def say_hello(self):
		print("Hello")

	def validate_username(char):
		print("check check")

if __name__ == "__main__":
	app = App()
	app.title("My App")
	app.mainloop()