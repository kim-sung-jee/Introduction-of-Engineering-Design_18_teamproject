from cProfile import label
from datetime import datetime
from pickle import GLOBAL
import tkinter
import tkinter.messagebox as msgbox
from tkinter import *
from datetime import datetime
from click import option
from numpy import imag
from selenium import webdriver
import time
from PIL import Image




def getImage():
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
    global location
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

## 선택창 버튼 클릭시 호출되는 메서드
def out():
    getImage()
    app.destroy()

## 남자 선택시 호출되는 메서드

def change2man():
    global isMan
    isMan=TRUE
    aa.insert(1.0,"남")
    aa.delete(1.0,"여")
def change2woman():
    global isWoman
    isWoman=TRUE
    aa.insert(1.0,"여")
    aa.delete(1.0,"남")

############################################## 시작점
# 선택창 시작
app=Tk()

app.title("선택창입니다")

app.geometry('540x640')

app.resizable(0,0)

startButton=tkinter.Button(app,background="white",text="실행버튼",width=30,height=3,
command=out)

startButton.place(x=160,y=550)

# 남/녀, 옷입력, 추위/더위
man=tkinter.Button(app,background="white",text="남",width=30,height=3,command=change2man)
woman=tkinter.Button(app,background="white",text="여",width=30,height=3,command=change2woman)
isMan=FALSE
isWoman=FALSE
aa=tkinter.Text(app,height=2)



aa.place(x=0,y=0)

man.place(x=100,y=100)
woman.place(x=300,y=100)



app.mainloop()



###############################################################
# 여기 까지 선택창(창1)                                        #
###############################################################



   




vWindow=Tk()
vWindow.title('윈도우창 타이틀')
vWindow.geometry('1280x640')
vWindow.resizable(0,0)
vWindow.option_add('*Font','돋음 20')
# 객체 
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
