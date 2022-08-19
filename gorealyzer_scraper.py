from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import os 

class Gorealyzer_Scraper():
	def get_reviews(self, url):
		self.__load_reviews(url)
		self.__extract_reviews()
		
	def __load_reviews(self, url):
		options = Options()
		options.add_argument('--headless')
		options.add_argument('--disable-gpu')
		options.add_argument('--disk-cache-size=209715200')
		driverpath = os.getcwd() + '/resources/chromedriver.exe'
		driver = webdriver.Chrome(driverpath,chrome_options=options)
		driver.get(url)
		driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div/div/div[2]/div[1]/div[3]/div[1]/div[1]/form[2]/div/div/button/span').click()
		time.sleep(3) 
		
		total_number_of_reviews = driver.find_element(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]/div/div[2]/div[2]').text.split(" ")[0]
		total_number_of_reviews = int(total_number_of_reviews.replace('.','')) if '.' in total_number_of_reviews else int(total_number_of_reviews)
		print(f'Total number of reviews: {total_number_of_reviews}')

		scrollable_div = driver.find_element(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]')
		
		if total_number_of_reviews < 1000: sleeptime = 0.2
		elif total_number_of_reviews >= 10000: sleeptime = 0.05
		else: sleeptime = 0.1
		loopcount = 0
		lenrev = 0
		while(lenrev < 2*total_number_of_reviews and lenrev < 1860 and loopcount<10):
			loopcount+=1
			for i in range(0,(round(total_number_of_reviews/10 - 1))):
				driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', scrollable_div)
				if i!=0 and i % 100==0: print(f'Scraping reviews. {i*10} of {total_number_of_reviews} attempted to read.')
				time.sleep(sleeptime)			
			
			response = BeautifulSoup(driver.page_source, 'html.parser')
			
			self.reviews = response.find_all('div', class_='GHT2ce')
			lenrev = len(self.reviews)
			print(f'Scraping itertaion no {loopcount} finished. {lenrev//2} reviews of {total_number_of_reviews} processed successfully.')
		print(f'Scraping reviews finished.')		
		
	def __extract_reviews(self):		
		self.rev_dict = {'Review Rate': [],
        'Review Time': [],
        'Review Text' : []}

		for result in self.reviews:
			subrev = result.find('div', class_='DU9Pgb')
			if subrev: 
				review_rate = subrev.find('span', class_='kvMYJc')["aria-label"]
				review_rate = [int(x) for x in review_rate.split() if x.isdigit()][0]
				review_time = subrev.find('span',class_='rsqaWe').text
				
				subrev2 = result.find('div', class_='MyEned')
				if subrev2: review_text = subrev2.text
				else: review_text = ''
				   
				self.rev_dict['Review Rate'].append(review_rate)
				self.rev_dict['Review Time'].append(review_time)
				self.rev_dict['Review Text'].append(review_text)
		
		