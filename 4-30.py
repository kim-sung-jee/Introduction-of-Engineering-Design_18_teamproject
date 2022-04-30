from cProfile import label
from datetime import datetime
import tkinter
import tkinter.messagebox as msgbox
from tkinter import *
from datetime import datetime
from click import option
from numpy import imag
from selenium import webdriver
import time
from PIL import Image





# init
options=webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')

# 날씨 정보
weather_data=[]
# 지역 정보
driver = webdriver.Chrome(options=options)

#
# c
#
driver.get("https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EB%84%A4%EC%9D%B4%EB%B2%84+%EB%82%A0%EC%94%A8&oquery=%EA%B8%B0%EC%83%81%EC%B2%AD&tqi=hElw2lp0JywssaJrew0ssssssZN-337365")

# 뜰때 까지 기다림
time.sleep(3)

# 현재 위치 파싱하기
location=driver.find_element_by_class_name("title").text
# 문자열 조작



# 스크린샷 하기
driver.maximize_window()

driver.execute_script("window.scrollTo(0,300)")

# save w_image
driver.save_screenshot("save1.png")

driver.quit()

# load image
image1=Image.open('save1.png')


croppedImage=image1.crop((389,334,1030,970))

croppedImage.save("save1.png")
img=Image.open("save1.png")

img_resize=img.resize((int(img.width/2),int(img.height/2)))
img_resize.save("save1.png")


vWindow=Tk()
vWindow.title('윈도우창 타이틀')
vWindow.geometry('1280x640')
vWindow.resizable(0,0)
vWindow.option_add('*Font','돋음 20')

image1=tkinter.PhotoImage(file="save1.png")
lable_1=tkinter.Label(vWindow,image=image1)
lable_1.place(x=850,y=150)

label_2=tkinter.Label(vWindow,text=location,background='#2f3640'
,width=17,height=12)
label_2.place(x=490,y=150)

label_3=tkinter.Label(vWindow,text="hello,world!",background='#2f3640'
,width=17,height=12)
label_3.place(x=100,y=150)

label_4=tkinter.Label(vWindow,text="hello,world!",background='#2f3640'
,width=40,height=2)
label_4.place(x=300,y=550)
# drawing ...


# fill blank

clothes=[]
pants=[]
outer=[]






vWindow.mainloop()
