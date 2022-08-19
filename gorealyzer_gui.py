import tkinter as tk
from tkinter import messagebox

class Gorealyzer_GUI():
	
	def __init__(self, master):
		self.master = master
		self.main_window = master.root		
		
		self.main_window.geometry('480x240')
		self.main_window.title('Review Analyzer by Ashardalon78, Version 1.0')
		
		self.texts = []
		
		self.__add_label('Enter URL here:', row=0, column=1, sticky=tk.E, pady=4)
		self.__add_text_field(40, row=0, column=2, sticky=tk.W, pady=4)
		self.__add_button('Load Reviews from web', self.__ana_pipeline, row=0, column=0, sticky=tk.W, pady=4)
		
		self.__add_button('Plot unmodified data', self.__plot_unmod, row=1, column=0, sticky=tk.W, pady=4)
		
		self.__add_label('Enter number of bins:', row=2, column=1, sticky=tk.E, pady=4)
		self.__add_text_field(5, text=8, row=2, column=2, sticky=tk.W, pady=4)
		self.__add_button('Plot binned data', self.__plot_binned, row=2, column=0, sticky=tk.W, pady=4)
		
		self.__add_label('Enter downsampling ratio:', row=3, column=1, sticky=tk.E, pady=4)
		self.__add_text_field(5, text=3, row=3, column=2, sticky=tk.W, pady=4)
		self.__add_button('Plot downsampled data', self.__plot_ds, row=3, column=0, sticky=tk.W, pady=4)
		
	
	def __add_button(self, name, function, **kwargs):	
		tk.Button(self.main_window, text=name, command=function).grid(kwargs)
		
	def __add_text_field(self, width, text=None, **kwargs):		
		self.texts.append(tk.Text(self.main_window, width=width, height=1))
		self.texts[-1].grid(kwargs)
		if text is not None: self.texts[-1].insert(tk.END, str(text))
		
	def __add_label(self, text, **kwargs):
		tk.Label(self.main_window, text=text).grid(kwargs)
		
	def __ana_pipeline(self):
		url = self.texts[0].get('1.0',tk.END).rstrip()
		#self.scraper.get_reviews(url)
		self.master.scraper.get_reviews(url)
		self.master.ana.analyze(self.master.scraper.rev_dict)
		
	def __plot_unmod(self):
		self.master.ana.plot_data(self.master.ana.df_revs_grouped['Rel Time'], self.master.ana.df_revs_grouped['Review Rate'], title='Unmodified time data')

	def __plot_binned(self):
		n_bins = int(self.texts[1].get('1.0',tk.END)) + 1
		self.master.ana.bin_data(n_bins=n_bins)
		self.master.ana.plot_data(self.master.ana.df_revs_binned['Time Bin'], self.master.ana.df_revs_binned['Review Rate'], 
		errors=self.master.ana.df_revs_binned['Review Rate err'], title='Binned time data')
	
	def __plot_ds(self):
		ds =  int(self.texts[2].get('1.0',tk.END))
		self.master.ana.downsample_data(downsample = ds)
		self.master.ana.plot_data(self.master.ana.df_revs_ds['Rel Time Mean'], self.master.ana.df_revs_ds['Review Rate Mean'], 
		errors=self.master.ana.df_revs_ds['Review Rate err'], title='Downsampled time data')
		
	
	