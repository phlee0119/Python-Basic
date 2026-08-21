# -*- coding: utf-8 -*-
"""
Created on Aug 21 2026

@author: Lee, Pin-Hua
"""

score = 98

if score >= 95 :                    # if 判斷式 ( 單向 )
    print("帶你去歐洲玩")
    print("***********")



score1 = int( input("你的成績是多少 : ") )

if score1 >= 95 :                    # if 判斷式 ( 雙向 )
    print("帶你去歐洲玩")
    
else :
    print("哪兒都不去")
    
    
    
score2 = int( input("你的成績是多少 : ") )

if score2 >= 95 :                    # if 判斷式 ( 多向 )
    print("帶你去歐洲玩")
    
elif score2 >= 85 :
    print("帶你去日本玩")
    
elif score2 >= 70 :
    print("帶你去台灣玩")
    
else :
    print("哪兒都不去")
    
    
    
sex = input("請問你的性別是 ( M / F ) : ")
height = eval( input("請問你的身高是 ( cm ) : ") )
weight = eval( input("請問你的體重是 ( kg ) : ") )

bmi = weight / ( ( height / 100 ) ** 2 )

if sex == 'M' :                      # if 判斷式 ( 巢狀 )
    
    if bmi > 25 :
        print("體重過重")
        
    elif bmi < 20 :
        print("體重過輕")
        
    else :
        print("身材適中")
    
else :
    
    if bmi > 22 :
        print("體重過重")
    
    elif bmi < 18 :
        print("體重過輕")
        
    else :
        print("身材適中")
