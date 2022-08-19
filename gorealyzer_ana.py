import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings("ignore", "(?s).*MATPLOTLIBDATA.*", category=UserWarning)
import matplotlib
warnings.filterwarnings("ignore", category=matplotlib.cbook.MatplotlibDeprecationWarning)
warnings.simplefilter('ignore', category=FutureWarning)
import matplotlib.pyplot as plt

class Gorealyzer_Ana():
	time_map = {'Jahr': 365, 'Jahren': 365, 'Monat': 30, 'Monaten': 30, 'Tag': 1, 'Tagen': 1, 'Woche': 7, 'Wochen': 7}

	def analyze(self, data_dict):
		self.__set_data(data_dict)
		self.__group_data()
		#self.__bin_data()
		#self.__downsample_data(downsample=3)
	
		# self.__plot_data(self.df_revs_grouped['Rel Time'], self.df_revs_grouped['Review Rate'], title='Unmodified time data')
		# self.__plot_data(self.df_revs_binned['Time Bin'], self.df_revs_binned['Review Rate'], errors=self.df_revs_binned['Review Rate err'], title='Binned time data')
		# self.__plot_data(self.df_revs_ds['Rel Time Mean'], self.df_revs_ds['Review Rate Mean'], errors=self.df_revs_ds['Review Rate err'], title='Downsampled time data')
		
	def plot_data(self, time, reviews, errors=None, title=None):
		fig, ax = plt.subplots()

		x_max=max(time)

		ax.set_xlim(x_max*1.2,0.5)
		ax.set_xscale('log')
		ax.set_xlabel('Time Past [Days]')
		ax.set_ylabel('Average Review Rate')		
		if errors is not None: ax.errorbar(time,reviews,errors,capsize=3,marker='x')
		else: ax.plot(time, reviews,marker='x')
		#ax.plot(time, reviews,marker='x')

		x_tick_max=pow(10,int(np.log10(x_max)+1))
		xticks = np.logspace(0,np.log10(x_tick_max),int(np.log10(x_tick_max))+1)
		ax.set_xticks(xticks)
		ax.set_xticklabels(["$%.d$" % x for x in xticks])
		if title is not None: ax.set_title(title)
		
		fig.show()
		
	def bin_data(self, n_bins=9):
		bin_mins = np.logspace(np.log10(self.df_revs['Rel Time'].min()*0.999),np.log10(self.df_revs['Rel Time'].max()*1.001),num=n_bins)
		self.df_revs['Time Bin'] = pd.cut(self.df_revs['Rel Time'],bins=bin_mins,right=False).apply(lambda x: x.left)

		bin_means = np.convolve(bin_mins,np.ones(2),'valid')/2
		dict_revs_binned = {'Time Bin': bin_means,
                    'Review Rate': list(self.df_revs['Review Rate'].groupby(self.df_revs['Time Bin']).mean()),
                   'Review Rate err': list(self.df_revs['Review Rate'].groupby(self.df_revs['Time Bin']).sem(ddof=1))}
		
		self.df_revs_binned = pd.DataFrame(dict_revs_binned)
		
	def downsample_data(self, downsample=3):
		mult_rev = (self.df_revs_grouped['Review Rate'] * self.df_revs_grouped['Count']).rolling(downsample).sum().shift(-(downsample-1)).iloc[::downsample].dropna()
		mult_time = (self.df_revs_grouped['Rel Time'] * self.df_revs_grouped['Count']).rolling(downsample).sum().shift(-(downsample-1)).iloc[::downsample].dropna()
		sumcount = self.df_revs_grouped['Count'].rolling(downsample).sum().shift(-(downsample-1)).iloc[::downsample].dropna()


		minlen = len(np.repeat(mult_rev/sumcount,downsample))
		difsqwt = ((np.array(self.df_revs_grouped['Review Rate'])[:minlen] - np.repeat(mult_rev/sumcount,downsample))**2) * np.array(self.df_revs_grouped['Count'])[:minlen]
		difsqwtsum = difsqwt.rolling(downsample).sum().shift(-(downsample-1)).iloc[::downsample].dropna()
		errwt = np.sqrt(difsqwtsum/sumcount/(downsample-1))

		dict_revs_ds = {'Rel Time Mean': mult_time/sumcount,
						'Review Rate Mean': mult_rev/sumcount,
						'Review Rate err': errwt
					   }
		self.df_revs_ds = pd.DataFrame(dict_revs_ds)
					

	def __set_data(self, data_dict):
		self.df_revs = pd.DataFrame(data_dict)
		
		self.df_revs['Rel Time'] = pd.to_numeric(self.df_revs['Review Time'].str.split().str[1].replace('eine.', '1', regex=True))		
		
		for key, value in self.time_map.items():
			self.df_revs['Rel Time'] = np.where(self.df_revs['Review Time'].str.split().str[-1]==key,\
			self.df_revs['Rel Time']*value,self.df_revs['Rel Time'])
		
		self.df_revs.sort_values('Rel Time', inplace=True)
				
	def __group_data(self):
		dict_revs_grouped = {'Rel Time': np.array(np.sort(self.df_revs['Rel Time'].unique())),
                    'Review Rate': self.df_revs.groupby(['Rel Time']).mean()['Review Rate'],
                    'Review Rate err': self.df_revs.groupby(['Rel Time']).sem(ddof=1)['Review Rate'],
					'Count': self.df_revs.groupby(['Rel Time']).count()['Review Rate']}
		self.df_revs_grouped = pd.DataFrame(dict_revs_grouped)	

	
		
		
		