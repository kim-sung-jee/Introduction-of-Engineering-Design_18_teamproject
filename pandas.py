from pickle import NONE
import pandas as pd

df=pd.read_excel('costum.xlsx')

i=3
outer=[]
clothes=[]
bb=[]
print(len(df))
while i<len(df):
    if df.iloc[i][0] == '아우터':
        outer.append({df.iloc[i][1]:df.iloc[i][2]})
    elif df.iloc[i][0]=='상의':
        clothes.append({df.iloc[i][1]:df.iloc[i][2]})
    else :
        bb.append({df.iloc[i][1]:df.iloc[i][2]})
    i+=1


#asdf

