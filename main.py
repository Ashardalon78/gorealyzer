import tkinter as tk
from gorealyzer_gui import Gorealyzer_GUI
from gorealyzer_scraper import Gorealyzer_Scraper
from gorealyzer_ana import Gorealyzer_Ana

class Gorealyzer():
	def __init__(self):
		self.root = tk.Tk()
	
		self.scraper = Gorealyzer_Scraper()
		self.ana = Gorealyzer_Ana()		
		self.gui = Gorealyzer_GUI(self)
		
		self.root.mainloop()
	

if __name__ == '__main__':
	#root = tk.Tk()
	#main_window = Gorealyzer_GUI(root)
	#root.mainloop()
	main_object = Gorealyzer()
	