
from asyncio.windows_events import NULL
from tkinter import ttk
import sqlite3
from datetime import date, datetime
import tkinter
import tkinter.messagebox as msgbox
from tkinter import *
from datetime import datetime
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

def algorithm(clothesList,clothesColorList):
    for i in clothesList:
        print(i)
    
    for i in clothesColorList:
        print(i)


## 선택창 맨밑 실행버튼 클릭시 호출되는 메서드
def out():
    ## sqllite3 디비에 커넥트하기
    conn = sqlite3.connect("weatherWear.db",isolation_level=None)
    
    # 커서 획득
    c=conn.cursor()

    # 쿼리문 날리기 테이블 없으면 생성함
    c.execute("CREATE TABLE IF NOT EXISTS clothes \
        (id integer PRIMARY KEY,name text,color text)")

    global clothesList # 옷종류
    clothesList = []
    global clothesColorList # 옷 색깔
    clothesColorList=[]
    c.execute("SELECT name,color FROM clothes")
    Cob=c.fetchall()
    #cob=[['종류','색깔']<<1번째,["종류2","색깔2"]<<2번째,[]<<3번째,[],[]...]
    for i in Cob:
        clothesList.append(i[0])

    for i in Cob:
        clothesColorList.append(i[1])


    ## 이부분을 짜야함 
    algorithm(clothesList,clothesColorList)
    ####


    # 크롤링한다 
    getImage()
    # app 꺼짐
    app.destroy()

## 남자 선택시 호출되는 메서드
def change2man():
    global isMan
    isMan=TRUE

## 여자 선택시 호출되는 메서드
def change2woman():
    global isWoman
    isWoman=TRUE

# 옷을 추가하는 메서드
def adding(c,combo,combo2):
    # 테스트 변수
    name=combo.get()
    name2=combo2.get()
    # 쿼리문 날려서 cursor에 결과 담기
    c.execute("SELECT id FROM 'clothes' ORDER BY id DESC LIMIT 1")
    # 옷장속에 아무옷도 없으면 그냥 넣기
   

    ## 전체 행 개수 조회
    num=c.fetchall()
    if(num==[]):
        # 비엇으면 그냥 넣기
        c.execute("INSERT INTO clothes VALUES"+'('+str(1)+',\''+name+"\',\'"+name2+"\');")
    else:
        # 안비엇으면 id 계산해서 넣기
        num2=num[0][0]
        num2+=1
        c.execute("INSERT INTO clothes VALUES"+'('+str(num2)+',\''+name+"\',\'"+name2+"\');")

   
    
    
# 옷 삭제하는 메서드
def deleteOne():
    # 옷장속 내용물들 출력하기
    wd=Toplevel(app)
    wd.title("옷장")
    wd.geometry('540x640')
    wd.resizable(0,0)
    ## sqllite3 디비에 커넥트하기
    conn = sqlite3.connect("weatherWear.db",isolation_level=None)
    # 커서 획득
    c=conn.cursor()
    c.execute("SELECT name,color FROM clothes")
    Cob=c.fetchall()
    
    listbox=tkinter.Listbox(wd,selectmode="extended",height=0)
    t=0
    for i in Cob:
        listbox.insert(t,i[1]+" "+i[0])
        t+=1
    listbox.place(x=100,y=100)
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
    clothe2=string_list[1]
   

    c.execute("DELETE FROM clothes WHERE name = \'"+clothe2+"\'AND color = \'"+clothe1
    +"\'")
    


# "옷 추가하기" 선택버튼 
def addClothes():
    # 창 환경설정
    
    newWindow=Toplevel(app)
    newWindow.title("옷 추가하기")
    newWindow.geometry('540x640')
    newWindow.resizable(0,0)
    ## sqllite3 디비에 커넥트하기
    conn = sqlite3.connect("weatherWear.db",isolation_level=None)
    
    # 커서 획득
    c=conn.cursor()

    # 쿼리문 날리기 테이블 없으면 생성함
    c.execute("CREATE TABLE IF NOT EXISTS clothes \
        (id integer PRIMARY KEY,name text,color text)")

    ## 버튼
    addingButton=tkinter.Button(newWindow,background="white",text="추가하기",width=30,height=3,
    command=lambda: adding(c,comboExample,comboExample2))
    
    addingButton.place(x=160,y=550)

    ## 콤보박스1
    list=["패딩점퍼","가디건","후드집업","코트","재킷","긴팔티셔츠",
    "긴팔셔츠","체크셔츠","반팔셔츠","반팔티셔츠","카라셔츠","민소매티셔츠","니트",
    "후드","니트조끼","터틀넥스웨터","긴치마","청바지","바지","반바지","짧은치마"] #여기에 옷종류
    comboExample=ttk.Combobox(newWindow,values=list,height=10)
    
    comboExample.place(x=100,y=100)
    comboExample.current(0)
    
    ## 콤보박스2
    list2=["흰색","빨강","핑크","주황","노랑","초록","파랑","네이비","보라","회색","검정",
    "연청색","진청색","베이지","카키","차콜"]#여기에 옷 색깔
    comboExample2=ttk.Combobox(newWindow,values=list2,height=10)

    comboExample2.place(x=100,y=300)
    comboExample2.current(0)


## 버튼,기본배경이미지,
## 앱의 시작점##
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

selectClothes=tkinter.Button(app,background="white",text="옷추가하기",width=60,height=3,command=addClothes)

# 옷장 정리하기
clear=tkinter.Button(app,background="white",text="옷장정리하기",width=60,height=3,
command=deleteOne)


man.place(x=50,y=100)
woman.place(x=300,y=100)
selectClothes.place(x=50,y=450)
clear.place(x=50,y=350)

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



vWindow.mainloop()
