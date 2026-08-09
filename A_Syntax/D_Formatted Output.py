# -*- coding: utf-8 -*-
"""
Created on Aug 10 2026

@author: Lee, Pin-Hua
"""

tempC = eval( input("請輸入攝氏溫度值 : ") )

tempF = tempC * ( 9 / 5 ) + 32

print("攝氏溫度", tempC, "度，相當於華氏溫度為", tempF, "度")

print("攝氏溫度 {} 度，相當於華氏溫度為 {} 度".format( tempC, tempF ))     # 格式化輸出 str.format()



intA = 3
intB = 5

result = "{} * {} = {}".format( intA, intB, intA * intB )

print( result )



intC = 123
print( "華氏溫度{}度".format( intC ) )
print( "華氏溫度{:5}度".format( intC ) )
print( "華氏溫度{:5d}度".format( intC ) )
print( "華氏溫度{:>5d}度".format( intC ) )
print( "華氏溫度{:<5d}度".format( intC ) )
print( "華氏溫度{:^5d}度".format( intC ) )



intD = 123.45678
print( "華氏溫度{:.3f}度".format( intD ) )
print( "華氏溫度{:+.3f}度".format( intD ) )
print( "華氏溫度{:.0f}度".format( intD ) )
print( "華氏溫度{:10.3f}度".format( intD ) )

print( "華氏溫度{:x>10.3f}度".format( intD ) )
print( "華氏溫度{:x<10.3f}度".format( intD ) )



intE = 1234.5678
print( "華氏溫度{:,}度".format( intE ) )
print( "華氏溫度{:.2%}度".format( intE ) )
print( "華氏溫度{:.2e}度".format( intE ) )
