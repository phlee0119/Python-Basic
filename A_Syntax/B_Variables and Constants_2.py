# -*- coding: utf-8 -*-
"""
Created on Aug 7 2026

@author: Lee, Pin-Hua
"""

x = 5                                    # ( = ) 指定運算子
print( x )
x1 = 5 * 6
print( x1 )

y = x1 + 5
print( y )

x2 = y2 = z2 = 3                          # 連續賦值
print( x2 )
print( y2 )
print( z2 )

x3, y3, z3 = 2, 5.8, "Hello"              # 多重賦值
print( x3 )
print( y3 )
print( z3 )

x4 = input()                              # 輸入 input()
print( x4 )
print( type( x4 ) )                       # input() 進來的值預設為字串
score = input("請輸入您的成績 : ")          # input() 內可放入提示文字
print( score )
print( type( score ) )
score1 = int( input("請輸入您的成績 : ") )  # 轉為整數 int()
print( score1 )
print( type( score1 ) )

print( score, y3, z3 )

print( score, y3, z3, sep = ' ' )         # sep = ' ' 選擇性參數，隔開各值間的字串
print( score, y3, z3, sep = '|' )
print( score, y3, z3, sep = "__" )

print( score, y3, z3, end = '\n' )        # end = '\n' 選擇性參數，結束後要印出的字串
print( score, y3, z3, end = ' ' )
