import tkinter as tk
from tkinter import ttk
from generator import generate_password


class App:
	def __init__(self):
		self.window = tk.Tk()
		self.window.title("Password Generator")
		self.window.geometry("320x140")
		self.window.resizable(False, False)

		self.frame = ttk.Frame(self.window, name='frame', padding=10)
		self.frame.grid()
		self.frame.columnconfigure(0, weight=1)
		self.frame.columnconfigure(1, weight=1)

		self.min_length = tk.StringVar()
		self.has_numbers = tk.IntVar()
		self.has_special = tk.IntVar()

		# password length
		self.lbl_min_length = tk.Label(self.frame, text="Minimum Length: ").grid(row=0, column=0)
		self.txt_min_length = tk.Entry(self.frame)
		self.txt_min_length.grid(row=0, column=1)
		self.txt_min_length.insert(0, "10")

		# has numbers
		self.lbl_has_numbers = tk.Label(self.frame, text="Has numbers?: ").grid(row=1, column=0)
		self.inp_has_numbers = tk.Checkbutton(self.frame, variable=self.has_numbers)
		self.inp_has_numbers.grid(row=1, column=1)
		self.inp_has_numbers.select()

		# has special characters
		self.lbl_has_special = tk.Label(self.frame, text="Has special characters?: ").grid(row=2, column=0)
		self.inp_has_special = tk.Checkbutton(self.frame, variable=self.has_special)
		self.inp_has_special.grid(row=2, column=1)
		self.inp_has_special.select()

		# buttons
		self.confirm_btn = tk.Button(self.frame, text="Generate", command=self.generate)
		self.confirm_btn.grid(row=4, column=0, sticky='e')
		self.exit_btn = tk.Button(self.frame, text="Exit", command=self.exit)
		self.exit_btn.grid(row=4, column=1, sticky='n')

		# output
		self.lbl_output = tk.Label(self.frame, text="Generated Password: ").grid(row=5, column=0)
		self.txt_output = tk.Entry(self.frame, name='pwd_output').grid(row=5, column=1)

	def __call__(self):
		self.window.mainloop()

	def generate(self):
		min_length = int(self.txt_min_length.get())
		has_numbers = self.has_numbers.get() == 1 # 1 means box is checked
		has_special = self.has_special.get() == 1

		password = generate_password(min_length, has_numbers, has_special)
		output = self.window.nametowidget("frame.pwd_output")
		output.delete(0, tk.END)
		output.insert(0, password)

	def exit(self):
		self.window.destroy()


app = App()
app()
