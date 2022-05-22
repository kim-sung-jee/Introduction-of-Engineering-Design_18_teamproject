from distutils.command.config import config
import recalgorithm
from tkinter import ttk
import sqlite3
from datetime import date, datetime
import tkinter
import tkinter.messagebox as msgbox
from tkinter import *
from datetime import datetime
from turtle import back
from selenium import webdriver
import time
from PIL import Image





def getImage(weatherData):
    # init
    options=webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')

    # 날씨 정보
    
    # 지역 정보
    driver = webdriver.Chrome(options=options)

    #
    # c
    #
    driver.get("https://search.naver.com/search.naver?query=%EB%82%A0%EC%94%A8&ie=utf8&sm=whl_nht")

    # 뜰때 까지 기다림
    time.sleep(3)

    # 현재 위치 파싱하기
    global location
    location=driver.find_element_by_class_name("title").text
    # 문자열 조작
    sensible = driver.find_element_by_class_name("summary_list")

    print(sensible)

    

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


## 선택창 맨밑 실행버튼 클릭시 호출되는 메서드
def out(configList):
    ## sqllite3 디비에 커넥트하기
    conn = sqlite3.connect("weatherWear.db",isolation_level=None)
    
    # 커서 획득
    c=conn.cursor()

    

    # 쿼리문 날리기 테이블 없으면 생성함
    c.execute("SELECT name,color FROM clothes")

    Cob = c.fetchall()
    topList=[]
    bottomList=[]
    outerList=[]
    list=["긴팔 티셔츠","긴팔 셔츠","체크 셔츠","반팔 셔츠","반팔 티셔츠","카라 셔츠","민소매 티셔츠","니트","후드","터틀넥 스웨터"]
    list3=["청바지","바지","반바지","얇은 치마","치마"]
    
    for i in Cob:
        if i[0] in list:
            topList.append([i[0],i[1]])
        elif i[0] in list3:
            bottomList.append([i[0],i[1]])
        else:
            outerList.append([i[0],i[1]])
    

    
    #### 날씨 정보
    weatherData=[]

    # 크롤링한다 
    getImage(weatherData)

    recalgorithm.algo(configList[0],configList[1],topList,bottomList,outerList)
    # app 꺼짐
    app.destroy()



# 옷을 추가하는 메서드
def adding(c,tkddml,tkddmlcolor,listbox):
    # 테스트 변수
    uname=tkddml.get()
    ucolor2=tkddmlcolor.get()
    # 쿼리문 날려서 cursor에 결과 담기
    c.execute("SELECT id FROM 'clothes' ORDER BY id DESC LIMIT 1")
    # 옷장속에 아무옷도 없으면 그냥 넣기
   
    
    ## 전체 행 개수 조회
    num=c.fetchall()
    if(num==[]):
        # 비엇으면 그냥 넣기
        c.execute("INSERT INTO clothes VALUES"+'('+str(1)+',\''+uname+"\',\'"+ucolor2+"\');")
    else:
        # 안비엇으면 id 계산해서 넣기
        num2=num[0][0]
        num2+=1
        c.execute("INSERT INTO clothes VALUES"+'('+str(num2)+',\''+uname+"\',\'"+ucolor2+"\');")

    refresh(listbox,c)

## 하의 추가
def adding2(c,tkddml,tkddmlcolor,listbox):
    # 테스트 변수
    uname=tkddml.get()
    ucolor2=tkddmlcolor.get()
    # 쿼리문 날려서 cursor에 결과 담기
    c.execute("SELECT id FROM 'clothes' ORDER BY id DESC LIMIT 1")
    # 옷장속에 아무옷도 없으면 그냥 넣기
   
    
    ## 전체 행 개수 조회
    num=c.fetchall()
    if(num==[]):
        # 비엇으면 그냥 넣기
        c.execute("INSERT INTO clothes VALUES"+'('+str(1)+',\''+uname+"\',\'"+ucolor2+"\');")
    else:
        # 안비엇으면 id 계산해서 넣기
        num2=num[0][0]
        num2+=1
        c.execute("INSERT INTO clothes VALUES"+'('+str(num2)+',\''+uname+"\',\'"+ucolor2+"\');")

    refresh(listbox,c)

## 아우터 추가
def adding3(c,tkddml,tkddmlcolor,listbox):
    # 테스트 변수
    uname=tkddml.get()
    ucolor2=tkddmlcolor.get()
    # 쿼리문 날려서 cursor에 결과 담기
    c.execute("SELECT id FROM 'clothes' ORDER BY id DESC LIMIT 1")
    # 옷장속에 아무옷도 없으면 그냥 넣기
   
    
    ## 전체 행 개수 조회
    num=c.fetchall()
    if(num==[]):
        # 비엇으면 그냥 넣기
        c.execute("INSERT INTO clothes VALUES"+'('+str(1)+',\''+uname+"\',\'"+ucolor2+"\');")
    else:
        # 안비엇으면 id 계산해서 넣기
        num2=num[0][0]
        num2+=1
        c.execute("INSERT INTO clothes VALUES"+'('+str(num2)+',\''+uname+"\',\'"+ucolor2+"\');")   
    refresh(listbox,c)
    
# 옷 삭제하는 메서드
def deleteOne(background2):
    # 옷장속 내용물들 출력하기
    wd=Toplevel(app)
    wd.title("옷장")
    wd.geometry('540x640')
    wd.resizable(0,0)
    ##배경화면
    # background2=PhotoImage(file="closet.png")
    b_label2=tkinter.Label(wd,image=background2)
    b_label2.place(x=0,y=0)
    

    ## sqllite3 디비에 커넥트하기
    conn = sqlite3.connect("weatherWear.db",isolation_level=None)
    # 커서 획득
    c=conn.cursor()
    c.execute("SELECT name,color FROM clothes")
    Cob=c.fetchall()
    
    frame=Frame(wd)
    frame.place(x=100,y=100)
    
    
    listbox=tkinter.Listbox(frame,selectmode="extended",height=10,width=20)
    listbox.pack(side="left",fill="y")


    scrollbar=Scrollbar(frame,orient="vertical")
    scrollbar.config(command=listbox.yview)
    scrollbar.pack(side="right",fill="y")
    

    listbox.config(yscrollcommand=scrollbar.set)
    t=0
    for i in Cob:
        listbox.insert(t,i[1]+" "+i[0])
        t+=1
    
    deleteButton=tkinter.Button(wd,background="white",text="삭제하기",width=10,height=3,
    command=lambda:delButtonListner(listbox,c))
    deleteButton.place(x=100,y=500)
    
    
#######
def delButtonListner(listbox,c):
    # curselection은 인덱스를 반환
    index=listbox.curselection()
    # listbox.get 을 통해서 value 찾기
    strl=listbox.get(index[0])
    # 문자열 조작하기..
    string_list=strl.split()
    clothe1=string_list[0]

    if len(string_list)>=3:
        clothe2=string_list[1]+" "+string_list[2]
    else:
        clothe2=string_list[1]

    c.execute("DELETE FROM clothes WHERE name = \'"+clothe2+"\'AND color = \'"+clothe1
    +"\'")
    c.execute("SELECT name,color FROM clothes")
    Cob=c.fetchall()
    end=len(Cob)
    listbox.delete(0,end)
    t=0
    for i in Cob:
        listbox.insert(t,i[1]+" "+i[0])
        t+=1

def refresh(listbox,c):
    c.execute("SELECT name,color FROM clothes")
    Cob=c.fetchall()
    end=len(Cob)
    listbox.delete(0,end)
    t=0
    for i in Cob:
        listbox.insert(t,i[1]+" "+i[0])
        t+=1



# "옷 추가하기" 선택버튼 
def addClothes(background):
    # 창 환경설정
    
    newWindow=Toplevel(app)
    newWindow.title("옷 추가하기")
    newWindow.geometry('540x640')
    newWindow.resizable(0,0)

    b_label2=tkinter.Label(newWindow,image=background)
    b_label2.place(x=0,y=0)


    ## sqllite3 디비에 커넥트하기
    conn = sqlite3.connect("weatherWear.db",isolation_level=None)
    
    # 커서 획득
    c=conn.cursor()

    # 쿼리문 날리기 테이블 없으면 생성함
    c.execute("CREATE TABLE IF NOT EXISTS clothes \
        (id integer PRIMARY KEY,name text,color text)")
    
    # 커서 획득
   
    c.execute("SELECT name,color FROM clothes")
    Cob=c.fetchall()

    frame=Frame(newWindow)
    frame.place(x=100,y=400)
    
    
    listbox=tkinter.Listbox(frame,selectmode="extended",height=10,width=20)
    listbox.pack(side="left",fill="y")


    scrollbar=Scrollbar(frame,orient="vertical")
    scrollbar.config(command=listbox.yview)
    scrollbar.pack(side="right",fill="y")
    

    listbox.config(yscrollcommand=scrollbar.set)


    t=0
    for i in Cob:
        listbox.insert(t,i[1]+" "+i[0])
        t+=1
   



    ## 상의추가버튼
    addingButton1=tkinter.Button(newWindow,background="white",text="추가하기",width=10,height=1,
    command=lambda: adding(c,tkddml,tkddmlcolor,listbox))
    
    addingButton1.place(x=420,y=100)

    ## 하의 추가 버튼
    addingButton2=tkinter.Button(newWindow,background="white",text="추가하기",width=10,height=1,
    command=lambda: adding2(c,gkdml,gkdmlcolor,listbox))
    
    addingButton2.place(x=420,y=150)

    ## 아우터 추가 버튼
    addingButton3=tkinter.Button(newWindow,background="white",text="추가하기",width=10,height=1,
    command=lambda: adding3(c,dkdnxj,dkdnxjcolor,listbox))
    
    addingButton3.place(x=420,y=200)

    ## 상의 종류
    list=["긴팔 티셔츠","긴팔 셔츠","체크 셔츠","반팔 셔츠","반팔 티셔츠","카라 셔츠","민소매 티셔츠","니트","후드","터틀넥 스웨터"] #여기에 옷종류
    tkddml=ttk.Combobox(newWindow,values=list,height=10)
    
    tkddml.place(x=50,y=100)
    tkddml.current(0)

    ### 상의 색깔
    list2=["흰색","흰색계열","빨강","핑크","주황","노랑","초록","파랑","네이비","보라","회색","검정"]
    tkddmlcolor=ttk.Combobox(newWindow,values=list2,height=10)
    tkddmlcolor.place(x=220,y=100)
    tkddmlcolor.current(0)
    
    ## 하의 종류
    list3=["청바지","바지","반바지","얇은 치마","치마"]
    gkdml=ttk.Combobox(newWindow,values=list3,height=10)
    
    gkdml.place(x=50,y=150)
    gkdml.current(0)

    ## 하의 색깔
    list4=["연청색","진청색","베이지","흰색","검은색","카키","차콜"]

    gkdmlcolor=ttk.Combobox(newWindow,values=list4,height=10)
    
    gkdmlcolor.place(x=220,y=150)
    gkdmlcolor.current(0)

    ## 아우터 종류
    list5=["패딩점퍼","얇은 가디건","두꺼운 가디건","후드집업","얇은 코트","두꺼운 코트","얇은 재킷","두꺼운 재킷"]
    dkdnxj=ttk.Combobox(newWindow,values=list5,height=10)
    
    dkdnxj.place(x=50,y=200)
    dkdnxj.current(0)

    ## 아우터 색깔
    list6=["흰색","흰색계열","빨강","핑크","주황","노랑","초록","파랑","네이비","보라","회색","검정"]
    dkdnxjcolor=ttk.Combobox(newWindow,values=list6,height=10)
    
    dkdnxjcolor.place(x=220,y=200)
    dkdnxjcolor.current(0)

   
def userConfig1(configList):
    configList[0]=0
def userConfig2(configList):
    configList[0]=1
def userConfig3(configList):
    configList[1]=0
def userConfig4(configList):
    configList[1]=1
def userConfig5(configList):
    configList[1]=2

def exitcommand(newWindow):
    newWindow.destroy()



def userconfig(background,configList):
    newWindow=Toplevel(app)
    newWindow.title("옷 추가하기")
    newWindow.geometry('540x640')
    newWindow.resizable(0,0)


    b_label2=tkinter.Label(newWindow,image=background)
    b_label2.place(x=0,y=0)

    man=tkinter.Button(newWindow,background="white",text="남",width=15,height=3,command=lambda:userConfig1(configList))
    woman=tkinter.Button(newWindow,background="white",text="여",width=15,height=3,command=lambda:userConfig2(configList))
    man.place(x=100,y=100)
    woman.place(x=330, y=100)

    cnf1=tkinter.Button(newWindow,background="white",text="추위를 많이탐",width=48,height=3,command=lambda:userConfig3(configList))
    cnf2=tkinter.Button(newWindow,background="white",text="더위를 많이탐",width=48,height=3,command=lambda:userConfig4(configList))
    cnf3=tkinter.Button(newWindow,background="white",text="추위와 더위 많이탐",width=48,height=3,command=lambda:userConfig5(configList))

    cnf1.place(x=100,y=200)
    cnf2.place(x=100,y=300)
    cnf3.place(x=100,y=400)

    check=tkinter.Button(newWindow,background="white",text="설정완료!",width=15,height=3,command=lambda:exitcommand(newWindow))

    check.place(x=220,y=500)

## 버튼,기본배경이미지,
## 앱의 시작점##
# 선택창 시작
app=Tk()

app.title("선택창입니다")

app.geometry('540x640')

app.resizable(0,0)


# 배경화면
background=PhotoImage(file="closet.png")
b_label=tkinter.Label(app,image=background)
b_label.place(x=0,y=0)
#######

## 0은 남여 , 1은 추위관련 flag
configList=[]
configList.append(0)
configList.append(0)

## 버튼 이미지 ##
brown=PhotoImage(file="brown.png")


##


startButton=tkinter.Button(app,background="white",text="옷추천받기",width=30,height=3,
command=lambda:out(configList))

startButton.place(x=160,y=550)

# 남/녀, 옷입력, 추위/더위

userConfig=tkinter.Button(app,background="#F08080",text="사용자설정",width=60,height=3,
command=lambda:userconfig(background,configList))


selectClothes=tkinter.Button(app,background="#BCBFBF",text="옷추가하기",width=60,height=3,
command=lambda:addClothes(background))

# 옷장 정리하기
clear=tkinter.Button(app,background="#DCDCDC",text="옷장정리하기",width=60,height=3,
command=lambda:deleteOne(background))

userConfig.place(x=50,y=100)
selectClothes.place(x=50,y=400)
clear.place(x=50,y=250)

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
lable_1.place(x=100,y=150)

label_2=tkinter.Label(vWindow,text=location,background='#2f3640'
,width=17,height=12)
label_2.place(x=490,y=150)

label_3=tkinter.Label(vWindow,text="hello,world!",background='#2f3640'
,width=17,height=12)
label_3.place(x=850,y=150)

label_4=tkinter.Label(vWindow,text="hello,world!",background='#2f3640'
,width=40,height=2)
label_4.place(x=300,y=550)
# drawing ...


# fill blank



vWindow.mainloop()
