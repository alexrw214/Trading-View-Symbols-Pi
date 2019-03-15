def get_values(symbol):
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.common.exceptions import TimeoutException
    

    # example option: add 'incognito' command line arg to options
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    options.add_argument("--headless")
    options.add_argument("--hide-scrollbars")
    options.add_argument("--disable-gpu")
    options.add_argument("--log-level=3")
    options.add_argument("--disable-extensions")

    # create new instance of chrome in incognito mode
    browser = webdriver.Chrome('C:/Users/Alex/Downloads/chromedriver_win32/chromedriver.exe',options=options)
    
    # go to website of interest
    browser.get('https://www.tradingview.com/symbols/'+symbol.upper()+'/')

    # get all of the titles for the financial values
    value = browser.find_element_by_class_name('tv-symbol-header-quote__value').text
    
    browser.quit()
    return float(value)
