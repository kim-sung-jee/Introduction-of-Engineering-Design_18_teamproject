import requests
from bs4 import BeautifulSoup
import pandas
import matplotlib as mpl
import matplotlib.pyplot as plt
 
 
source = requests.get('https://www.weather.go.kr/weather/observation/currentweather.jsp')
soup = BeautifulSoup(source.content,"html.parser")
 
table = soup.find('table',{'class':'table-col'})
data = []
tbody=table.tbody
tr=tbody.find_all('tr')
# 사용자로부터 입력 받을 것임
location = "서울"
# 시간은 기상청 사이트에서 알아서 현재시간 설정해줌
for i in tr:
    if(i.td.contents[0].get_text()==location):
        print(i.td.contents[0].get_text())
        tds=i.find_all('td')
        
        print(tds[5].get_text(),"기온")
        print(tds[1].get_text(),"구름의양?")




# # 강릉의 tr = tr[0]
# tds=tr[0].find_all('td')
# # 태그 내부의 값 읽기
# l_name=tds[0].get_text()
# print(l_name)