from selenium import webdriver

driver = webdriver.Firefox


city = str(input("Enter City Name: "))

driver.get("https://www.weather-forecast.com/locations/"+city+"/forecasts/latest")


print(driver.find_elements_by_class_name("b-forecast__table-description-content")[0].text)
#Test
