#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Created: 2023-05-15 01:42:51

# Import
import sys
import os
import numpy
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def main():
  URL = "https://www.click-sec.com/corp/guide/fxneo/rate/"
  CHROMEDRIVER = "/usr/bin/chromedriver"
  options = Options()
  options.add_argument('--headless')
  driver = webdriver.Chrome(CHROMEDRIVER, options=options)
  driver.get(URL)
  dollar_yen_buy = driver.find_element_by_id("fxneorate_bid_0").text
  driver.quit()
  print(f"USD/JPY={dollar_yen_buy}")

if __name__ == '__main__':
  main()
