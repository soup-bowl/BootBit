import tkinter as tk
from tkinter.constants import CENTER, N

class App:
	def __init__(self, root):

		root.title("Choose an Operating System")

		width=640
		height=480
		screenwidth = root.winfo_screenwidth()
		screenheight = root.winfo_screenheight()
		alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
		root.geometry(alignstr)
		root.resizable(False, False)

		msgWelcome=tk.Label(root)
		msgWelcome.config(
			justify=CENTER,
			text="Choose an Operating System to start."
		)
		msgWelcome.place(x=175,y=100)

		frmDashboard = tk.Frame(root)
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


	def boot_mac(self):
		print("command")


	def boot_dos(self):
		print("command")

if __name__ == "__main__":
	root = tk.Tk()
	app = App(root)
	root.mainloop()
