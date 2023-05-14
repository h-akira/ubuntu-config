#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Created: 2023-05-15 01:42:51

# Import
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def get_rate():
  URL = "https://www.click-sec.com/corp/guide/fxneo/rate/"
  CHROMEDRIVER = "/usr/bin/chromedriver"
  options = Options()
  options.add_argument('--headless')
  driver = webdriver.Chrome(CHROMEDRIVER, options=options)
  driver.get(URL)
  dollar_yen_buy = driver.find_element_by_id("fxneorate_bid_0").text
  driver.quit()
  return dollar_yen_buy

def market_open():
  DIFF_JST_FROM_UTC = 9
  now = datetime.datetime.utcnow() + datetime.timedelta(hours=DIFF_JST_FROM_UTC)
  num = now.weekday()
  if 1 <= num <= 4:
    return True
  elif num == 0 and now.hour >= 7:  
    return True
  elif num == 5 and now.hour < 7:
    return True
  else:
    return False

def main():
  if market_open():
    dollar_yen_buy = get_rate()
    print(f"USD/JPY={dollar_yen_buy}")
  else:
    print("Market is not open")

if __name__ == '__main__':
  main()
