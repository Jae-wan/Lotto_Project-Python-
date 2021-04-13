from selenium import webdriver
import openpyxl

driver=webdriver.Chrome('./chromedriver.exe')

################# Set openpyxl #####################
wb=openpyxl.load_workbook('./Test_1.xlsx', data_only=True)
sheet = wb['Sheet1']

#################### Set selenium & Chrome Driver API ##############
url= 'https://www.dhlottery.co.kr/gameResult.do?method=byWin'

driver.get(url)

############### Main Code ####################
driver.implicitly_wait(time_to_wait=5)

data=[]

data.append(str(driver.find_element_by_xpath('//*[@id="article"]/div[2]/div/div[2]/div/div[1]/p').text))
data.append(str(driver.find_element_by_xpath('//*[@id="article"]/div[2]/div/div[2]/div/div[2]/p/span').text))

print('--------------------- 6개 번호 + 보너스번호 값 : ', end='')
print(data)


## 가장 중요한거
# https://wpscholar.com/blog/view-form-data-in-chrome/
# Form Data 확인 후 쿼리에서 https://www.dhlottery.co.kr/gameResult.do?method=byWin&drwNo=944
# 하면 944 페이지로 이동됨.
