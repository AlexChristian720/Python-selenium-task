from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\shree\desktop\driver\Driver_Notes\chromedriver.exe")
driver.get(' https://www.atg.party/')

js = '''
// arguements at index 0
let callback = arguments[0];

//XMLHttpRequest is an API in the form of an object 
//whose methods transfer data between a web browser and a web server.

let xhr = new XMLHttpRequest();
xhr.open('GET', ' https://www.atg.party/', true);
xhr.onload = function () {
    if (this.readyState === 4) {
        callback(this.status);
    }
};
xhr.onerror = function () {
    callback('error');
};
xhr.send(null);
'''

status_code = driver.execute_async_script(js)
print(status_code) # this will return the status code of the web page

driver.close()

with open('response code.txt','w+') as f:
    f.write('The Status code is:  Ok')

    f.write(str(status_code))





