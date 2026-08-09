# -*- coding: utf-8 -*-
"""
Created on Aug 9 2026

@author: Lee, Pin-Hua
"""

height = eval( input("請輸入身高 ( cm ) : ") )          # 轉為數值 eval()
weight = eval( input("請輸入體重 ( kg ) : ") )

bmi = weight / ( ( height / 100 ) ** 2 )

print( "此人的 BMI 為 : ", bmi )                       # BMI = 體重 ( kg ) / ( 身高 ( m ) ** 2 )
