# 남여,상의,하의,아우터,개개인추위관련
# morw =0 남자 
# morw =1 여자
# flag =0 
# flag = 1
# flag= 2 
def algo(morw,flag,toplist,bottomlist,outerlist,weatherdata): 
    

    ## 체감온도 받아온거 사용
    temperatures=int(weatherdata[0][:-3])
    resultList=[]
    

    ##  27도 이상일 때,
    if temperatures>=27:
        # 남자일 때
        if morw == 0:
            ## 먼저 상의 기준으로 순회하기
            for i in toplist:
                if "반팔 티셔츠" in i[0]:
                    
                    for j in bottomlist:
                        
                        if "반바지" in j[0]:
                            if checkColor(i[1],j[1])==True:
                                resultList.append([i,j])
                            

                        elif "긴바지" in j[0]:
                            if checkColor(i[1],j[1])==True:
                                resultList.append([i,j])

                elif "반팔 셔츠" in i[0]:
                    for j in bottomlist:
                        if "반바지" in j[0]:
                            if checkColor(i[1],j[1])==True:
                                resultList.append([i,j])
                        elif "긴바지" in j[0]:
                            if checkColor(i[1],j[1])==True:
                                resultList.append([i,j])
                

        # 여자일 때
        elif morw==1:
            ## 상의 기준으로 순회하기
            for i in toplist:
                if "반팔 티셔츠" in i[0]:
                    
                    for j in bottomlist:
                        
                        if "반바지" in j[0]:
                            if checkColor(i[1],j[1])==True:
                                resultList.append([i,j])
                            

                        elif "긴바지" in j[0]:
                            if checkColor(i[1],j[1])==True:
                                resultList.append([i,j])

                elif "반팔 셔츠" in i[0]:
                    for j in bottomlist:
                        if "반바지" in j[0]:
                            if checkColor(i[1],j[1])==True:
                                resultList.append([i,j])
                        elif "긴바지" in j[0]:
                            if checkColor(i[1],j[1])==True:
                                resultList.append([i,j])
                elif "반팔 원피스" in  i[0]:
                    resultList.append([i,i])
                elif "민소매 원피스" in i[0]:
                    resultList.append([i,i])
                elif "민소매 티" in i[0]:
                    for j in bottomlist:
                        if "긴바지" in j[0]:
                            if checkColor(i[1],j[1])==True:
                                resultList.append([i,j])
                elif "반팔 티셔츠" in i[0]:
                    for j in bottomlist:
                        if "긴바지" in j[0]:
                            if checkColor(i[1],j[1])==True:
                                resultList.append([i,j])
                elif "반팔 셔츠" in i[0]:
                    for j in bottomlist:
                        if "긴바지" in j[0]:
                            if checkColor(i[1],j[1])==True:
                                resultList.append([i,j])

    elif 23<=temperatures and temperatures<=26:
        
         # 남자일 때
        if morw == 0:
            ## 먼저 상의 기준으로 순회하기
            for i in toplist:
                if "반팔 티셔츠" in i[0]:
                    
                    for j in bottomlist:
                        
                        if "긴바지" in j[0]:
                            if checkColor(i[1],j[1])==True:
                                resultList.append([i,j])
                        
                elif "반팔 셔츠" in i[0]:
                    for j in bottomlist:
                        if "긴바지" in j[0]:
                            if checkColor(i[1],j[1])==True:
                                resultList.append([i,j])
                        
                elif "긴팔 티셔츠":
                    for j in bottomlist:
                        if "긴바지" in j[0]:
                            if checkColor(i[1],j[1])==True:
                                resultList.append([i,j])
                elif "긴팔 셔츠":
                    for j in bottomlist:
                        if "긴바지" in j[0]:
                            if checkColor(i[1],j[1])==True:
                                resultList.append([i,j])
        elif morw == 1:
            for i in toplist:
                if "반팔 티셔츠" in i[0]:
                    
                    for j in bottomlist:
                        
                        if "긴바지" in j[0]:
                            if checkColor(i[1],j[1])==True:
                                resultList.append([i,j])
                        
                elif "반팔 셔츠" in i[0]:
                    for j in bottomlist:
                        if "긴바지" in j[0]:
                            if checkColor(i[1],j[1])==True:
                                resultList.append([i,j])
                        
                elif "긴팔 티셔츠"in i[0]:
                    for j in bottomlist:
                        if "긴바지" in j[0]:
                            if checkColor(i[1],j[1])==True:
                                resultList.append([i,j])
                elif "긴팔 셔츠"in i[0]:
                    for j in bottomlist:
                        if "긴바지" in j[0]:
                            if checkColor(i[1],j[1])==True:
                                resultList.append([i,j])
                elif "반팔 티셔츠"in i[0]:
                    for j in bottomlist:
                        if "치마" in j[0]:
                            if checkColor(i[1],j[1])==True:
                                resultList.append([i,j])
                elif "반팔 셔츠"in i[0]:
                    for j in bottomlist:
                        if "치마" in j[0]:
                            if checkColor(i[1],j[1])==True:
                                resultList.append([i,j])
                elif "긴팔 티셔츠"in i[0]:
                    for j in bottomlist:
                        if "치마" in j[0]:
                            if checkColor(i[1],j[1])==True:
                                resultList.append([i,j])
                elif "긴팔 셔츠"in i[0]:
                    for j in bottomlist:
                        if "치마" in j[0]:
                            if checkColor(i[1],j[1])==True:
                                resultList.append([i,j])
                elif "반팔 원피스"in i[0]:
                    resultList.append([i,j])
                elif "민소매 원피스"in i[0]:
                    for t in outerlist:
                        if "얇은 가디건" in t[0]:
                            if checkoutercolor(i[1],j[1],t[1])==True:
                                resultList.append([i,j,t])
    elif 20<=temperatures and temperatures<=22:
        if morw==0:
            for i in toplist:
                if "긴팔 티셔츠" in i[0]:
                    for j in bottomlist:
                        if "긴바지" in j[0]:
                            if checkColor(i[1],j[1]) == True:
                                resultList.append([i,j])
                elif "반팔 티셔츠" in i[0]:
                    for j in bottomlist:
                        if "긴바지" in j[0]:
                            for t in outerlist:
                                if "얇은 가디건" in outerlist:
                                    if checkoutercolor(i[1],j[1],t[1])==True:
                                        resultList.append([i,j,t])
                elif "반팔 셔츠" in i[0]:
                    for j in bottomlist:
                        if "긴바지" in j[0]:
                            for t in outerlist:
                                if "얇은 가디건" in outerlist:
                                    if checkoutercolor(i[1],j[1],t[1])==True:
                                        resultList.append([i,j,t])
                elif "긴팔 셔츠" in i[0]:
                    for j in bottomlist:
                        if "긴바지" in j[0]:
                            if checkColor(i[1],j[1]) == True:
                                resultList.append([i,j])
                elif "후드티" in i[0]:
                    for j in bottomlist:
                        if "긴바지" in j[0]:
                            if checkColor(i[1],j[1]) == True:
                                resultList.append([i,j])
                elif "맨투맨" in i[0]:
                    for j in bottomlist:
                        if "긴바지" in j[0]:
                            if checkColor(i[1],j[1]) == True:
                                resultList.append([i,j])
        elif morw==1:
            for i in toplist:
                if "긴팔 티셔츠" in i[0]:
                    for j in bottomlist:
                        if "긴바지" in j[0]:
                            if checkColor(i[1],j[1]) == True:
                                resultList.append([i,j])
                elif "반팔 티셔츠" in i[0]:
                    for j in bottomlist:
                        if "긴바지" in j[0]:
                            for t in outerlist:
                                if "얇은 가디건" in outerlist:
                                    if checkoutercolor(i[1],j[1],t[1])==True:
                                        resultList.append([i,j,t])
                elif "반팔 셔츠" in i[0]:
                    for j in bottomlist:
                        if "긴바지" in j[0]:
                            for t in outerlist:
                                if "얇은 가디건" in outerlist:
                                    if checkoutercolor(i[1],j[1],t[1])==True:
                                        resultList.append([i,j,t])
                elif "긴팔 셔츠" in i[0]:
                    for j in bottomlist:
                        if "긴바지" in j[0]:
                            if checkColor(i[1],j[1]) == True:
                                resultList.append([i,j])
                elif "후드티" in i[0]:
                    for j in bottomlist:
                        if "긴바지" in j[0]:
                            if checkColor(i[1],j[1]) == True:
                                resultList.append([i,j])
                elif "맨투맨" in i[0]:
                    for j in bottomlist:
                        if "긴바지" in j[0]:
                            if checkColor(i[1],j[1]) == True:
                                resultList.append([i,j])
                elif "반팔 원피스" in i[0]:
                    for j in bottomlist:
                        if "치마" in j[0]:
                            for t in outerlist:
                                if "얇은 가디건" in outerlist:
                                    if checkoutercolor(i[1],j[1],t[1])==True:
                                        resultList.append([i,j,t])
                elif "긴팔 티셔츠" in i[0]:
                    for j in bottomlist:
                        if "치마" in j[0]:
                            if checkColor(i[1],j[1])==True:
                                resultList.append([i,j])
                elif "반팔 티셔츠" in i[0]:
                    for j in bottomlist:
                        if "치마" in j[0]:
                            for t in outerlist:
                                if "얇은 가디건" in outerlist:
                                    if checkoutercolor(i[1],j[1],t[1])==True:
                                        resultList.append([i,j,t])
                elif "반팔 셔츠" in i[0]:
                    for j in bottomlist:
                        if "치마" in j[0]:
                            for t in outerlist:
                                if "얇은 가디건" in outerlist:
                                    if checkoutercolor(i[1],j[1],t[1])==True:
                                        resultList.append([i,j,t])
                elif "긴팔 셔츠" in i[0]:
                    for j in bottomlist:
                        if "치마" in j[0]:
                            if checkColor(i[1],j[1])==True:
                                resultList.append([i,j])
                elif "후드티" in i[0]:
                    for j in bottomlist:
                        if "치마" in j[0]:
                            if checkColor(i[1],j[1])==True:
                                resultList.append([i,j])
                elif "맨투맨" in i[0]:
                    for j in bottomlist:
                        if "치마" in j[0]:
                            if checkColor(i[1],j[1])==True:
                                resultList.append([i,j])
    elif 17<=temperatures and temperatures<=19:
        print()
    elif 12<=temperatures and temperatures<=16:
        print()
    elif 10<=temperatures and temperatures<=11:
        print()
    elif 6<=temperatures and temperatures<=9:
        print()
    elif temperatures<=5:
        print()


    for i in resultList:
        print(i)

def checkColor(top,bottom):
    if bottom == "연청색":
        if top =="흰색":
            return True
        elif top=="핑크":
            return True
        elif top=="흰색계열":
            return True
    elif bottom =="진청색":
        if top =="흰색":
            return True
    elif bottom == "베이지":
        if top =="흰색":
            return True
        elif top =="흰색계열":
            return True
    elif bottom =="흰색":
        if top =="파랑":
            return True
        elif top =="네이비":
            return True
    elif bottom =="검은색":
        if top =="흰색":
            return True
        elif top =="흰색계열":
            return True
        elif top =="노랑":
            return True
    elif bottom =="카키":
        if top =="네이비":
            return True
    elif bottom == "차콜":
        if top =="네이비":
            return True
    else :
        return False

def checkoutercolor(top,bottom,outer):
    if bottom == "연청색":
        if top =="흰색":
            if outer == "흰색계열":
                return True
            elif outer == "네이비":
                return True
            elif outer == "회색":
                return True
            elif outer == "검정":
                return True
        elif top=="핑크":
            
            if outer == "네이비":
                return True
            elif outer == "회색":
                return True
            elif outer == "검정":
                return True
        elif top=="흰색계열":
            if outer == "흰색계열":
                return True
            elif outer == "네이비":
                return True
            elif outer == "회색":
                return True
            elif outer == "검정":
                return True
    elif bottom =="진청색":
        if top =="흰색":
            if outer == "흰색계열":
                return True
            elif outer == "네이비":
                return True
            elif outer == "회색":
                return True
            elif outer == "검정":
                return True
    elif bottom == "베이지":
        if top =="흰색":
            if outer == "흰색계열":
                return True
            elif outer == "네이비":
                return True
            elif outer == "회색":
                return True
            elif outer == "검정":
                return True
        elif top =="흰색계열":
            if outer == "흰색계열":
                return True
            elif outer == "네이비":
                return True
            elif outer == "회색":
                return True
            elif outer == "검정":
                return True
    elif bottom =="흰색":
        if top =="파랑":
            if outer == "흰색계열":
                return True
            elif outer == "네이비":
                return True
            elif outer == "회색":
                return True
            elif outer == "검정":
                return True
        elif top =="네이비":
            return True
    elif bottom =="검은색":
        if top =="흰색":
            if outer == "흰색계열":
                return True
            elif outer == "네이비":
                return True
            elif outer == "회색":
                return True
            elif outer == "검정":
                return True
        elif top =="흰색계열":
            if outer == "흰색계열":
                return True
            elif outer == "네이비":
                return True
            elif outer == "회색":
                return True
            elif outer == "검정":
                return True
        elif top =="노랑":
            if outer == "흰색계열":
                return True
            elif outer == "네이비":
                return True
            elif outer == "회색":
                return True
            elif outer == "검정":
                return True
    elif bottom =="카키":
        if top =="네이비":
            if outer == "흰색계열":
                return True
            elif outer == "네이비":
                return True
            elif outer == "회색":
                return True
            elif outer == "검정":
                return True
    elif bottom == "차콜":
        if top =="네이비":
            if outer == "흰색계열":
                return True
            elif outer == "네이비":
                return True
            elif outer == "회색":
                return True
            elif outer == "검정":
                return True
    else :
        return False
    

    
