
'''
Import the necessary packages required for execution
'''
from selenium import webdriver

''' Chrome web driver interface
'''
hyperlink = "http://lambdatest.com"
driver = webdriver.Chrome(executable_path="C:\\Users\shree\desktop\driver\Driver_Notes\chromedriver.exe")
driver.get(hyperlink)

''' Use Navigation Timing  API to calculate the timings that matter the most '''

navigationStart = driver.execute_script("return window.performance.timing.navigationStart")
responseStart = driver.execute_script("return window.performance.timing.responseStart")
domComplete = driver.execute_script("return window.performance.timing.domComplete")

''' Calculate the performance'''
backendPerformance_calc = responseStart - navigationStart
frontendPerformance_calc = domComplete - responseStart

print("Back End: %s" % backendPerformance_calc)
print("Front End: %s" % frontendPerformance_calc)

driver.quit()

with open('Page time logged.txt','w+') as f:
    f.write(str("Back End: %s" % backendPerformance_calc))
    f.write('\n')
    f.write(str("Front End: %s" % frontendPerformance_calc))