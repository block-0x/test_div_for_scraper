import os
# from time import sleep
# import pandas as pd
# from bs4 import BeautifulSoup
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys
# import re
import pandas as pd
import numpy as np


# data = pd.read_csv('sample.csv', sep=",")
# print(data)
# 予め列を挿入しておく必要がある。
# data['new_column'] = ''

# # 列に値を代入
# for index, row in data.iterrows():
#     data['new_column'][index] = 'hoge'

# data.to_csv('sample.csv', index=False)

# print(open('sample.csv').read())
class ChannelCountryScraper(object):

	def run(self):
		self.read_youtube_urls()
		# self.get_page_source()
		# self.channel_country_data_save_as_csv_file()


	def read_youtube_urls(self):
		channel_url_data = pd.read_csv('sample.csv',index_col='channel_url')
		channel_urls_ndarray = channel_url_data.index.values
		channel_urls = channel_urls_ndarray.tolist()
		for i in channel_urls:
			self.youtube_url = "https://www.youtube.com"
			self.channel_url = ("%s" % i)
			self.open_channel_url = os.path.join(self.youtube_url, self.channel_url, 'about')
			print(self.open_channel_url)

	# def get_page_source(self):
	# 	self.driver = webdriver.Chrome()
	# 	self.driver.get(self.channel_about_url)
	# 	self.current_html = self.driver.page_source
	# 	element = self.driver.find_element_by_xpath('//*[@class="style-scope ytd-page-manager"]')
	# 	actions = ActionChains(self.driver)
	# 	actions.move_to_element(element)
	# 	actions.perform()
	# 	actions.reset_actions()
	# 	while True:
	# 		for j in range(100):
	# 			actions.send_keys(Keys.PAGE_DOWN)
	# 		actions.perform()
	# 		sleep(2.5)
	# 		html = self.driver.page_source
	# 		if self.current_html != html:
	# 			self.current_html=html
	# 		else:
	# 			break


if __name__ == "__main__":
    channel_country = ChannelCountryScraper()
    channel_country.run()
