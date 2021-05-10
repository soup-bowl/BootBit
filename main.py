import tkinter as tk
import subprocess
from tkinter.constants import CENTER, N

class App:
	def __init__(self):
		self.tk    = tk.Tk()
		self.state = False

		width        = 640
		height       = 480
		screenwidth  = self.tk.winfo_screenwidth()
		screenheight = self.tk.winfo_screenheight()
		alignstr     = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)

		self.tk.title("Choose an Operating System")
		self.tk.geometry(alignstr)
		self.tk.bind("<F11>", self.toggle_fullscreen)
		self.tk.bind("<Escape>", self.end_fullscreen)

		msgWelcome=tk.Label(self.tk)
		msgWelcome.config(
			justify=CENTER,
			text="Choose an Operating System to start."
		)
		msgWelcome.place(x=175,y=100)

		frmDashboard = tk.Frame(self.tk)
		frmDashboard.grid(sticky="NSEW", column=2, row=0)
		frmDashboard.place(x=125, y=200)

		#imgApple    = Image.open('logo-apple.png')
		#imgAppleRef = tk.PhotoImage(file='logo-apple.png') 

		btnMac=tk.Button(frmDashboard)
		btnMac["fg"] = "#000000"
		btnMac["justify"] = "center"
		btnMac["text"] = "System 9"
		btnMac["command"] = self.boot_mac
		btnMac.config(height=10,width=20)
		btnMac.grid(column=0, row=0)

		btnDOS=tk.Button(frmDashboard)
		btnDOS["fg"] = "#000000"
		btnDOS["justify"] = "center"
		btnDOS["text"] = "DOS"
		btnDOS["command"] = self.boot_dos
		btnDOS.config(height=10,width=20)
		btnDOS.grid(column=1, row=0)

	def toggle_fullscreen(self, event=None):
		self.state = not self.state  # Just toggling the boolean
		self.tk.attributes("-fullscreen", self.state)
		return "break"

	def end_fullscreen(self, event=None):
		self.state = False
		self.tk.attributes("-fullscreen", False)
		return "break"


	def boot_mac(self):
		process = subprocess.Popen("echo hello", shell=True, stdout=subprocess.PIPE)
		process.wait()
		print(process.returncode)


	def boot_dos(self):
		print("command")

if __name__ == "__main__":
	app = App()
	app.tk.mainloop()
