from selenium import webdriver
import time

path = "C:/chromedriver.exe" # 웹드라이버 경로
driver = webdriver.Chrome(path) # 웹드라이버 경로 지정
driver.get("http://zzzscore.com/1to50/") # 브라우저 열기

for i in range (1, 51): # 눌러야 할 버튼의 수는 50개
    for j in range (1, 26): # 버튼(div)의 개수는 25개
        index = driver.find_element_by_xpath("//*[@id='grid']/div[" + str(j) + "]") # div의 text를 추출하여 index에 저장

        if (index.text == str(i)): # div가 i와 같을 경우 버튼 클릭
            btn = index
            btn.click()
            break

    print(str(i) + " 클릭")
