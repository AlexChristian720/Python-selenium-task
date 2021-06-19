# Importing webdriver from selenium
from selenium import webdriver

# Here chrome webdriver is used
driver = webdriver.Chrome(executable_path="C:\\Users\shree\Desktop\driver\Driver_Notes\chromedriver.exe")

# URL of the website
url = "https://www.atg.party/view-article/18684/this-is-the-beautiful-flower?r=83"

# Getting current URL
get_url = driver.current_url

# Printing the URL
print(get_url)

# Opening the URL
driver.get(url)

# Getting current URL
get_url = driver.current_url

# Printing the URL
print(get_url)

with open('Log.log','w+') as f:
    f.write('The Log of the new URL of the page ')
    f.write('\n')
    f.write(get_url)



