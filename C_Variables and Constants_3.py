# -*- coding: utf-8 -*-
"""
Created on Aug 8 2026

@author: Lee, Pin-Hua
"""

x = 8 / 5                       # 算數運算子 除 ( / )
print( x )
x1 = 8 // 5                     # 算數運算子 求商 ( // )
print( x1 )
x2 = 8 % 5                      # 算數運算子 求餘 ( % )
print( x2 )

y = 5 > 3                       # 比較運算子 大於 ( > )
print( y )
y1 = 3 > 9
print( y1 )
y2 = 3 == 3                     # 比較運算子 等於 ( == )
print( y2 )
y3 = 3 != 3                     # 比較運算子 不等於 ( != )
print( y3 )

z = 5 > 3 and 8 > 2             # 邏輯運算子 且 ( and )
print( z )
z1 = not 5 > 3                  # 邏輯運算子 非 ( not )
print( z1 )

a = 5
a = a + 5
print( a )
a1 = 5
a1 += 5                         # 指派運算子 同理 a1 = a1 + 5 
print( a1 )
a2 = a1
a2 /= 2                         # 指派運算子 同理 a2 = a2 / 2
print(a2)

b = -5
b1 = abs( b )                   # 取絕對值 abs()
print( b1 )

c1, c2 = divmod( 10, 7 )        # 取商與餘 divmod()
print( c1, c2 )

d1 = max( 1, 2, 3, 4, 5 )       # 取最大值 max()
print( d1 )
d2 = min( 1, 2, 3, 4, 5 )       # 取最小值 min()
print( d2 )

e = 2 ** 5                      # 算數運算子 指數次方 ( ** )
print( e )
e1 = pow( 2, 5 )                # 取指數次方 pow() 同理 2 ** 5
print( e1 )

f = round( 3.14159 )            # 四捨五入 round() 預設到小數點第0位
print( f )
f1 = round( 3.14159, 3 )        # 四捨五入到小數點第三位
print( f1 )

import math                     # 匯入 : import, 數學模組 : math

g1 = math.ceil( 3.14159 )       # 無條件進位 ceil()
print( g1 )
g2 = math.gcd( 12, 8 )          # 取最大公因數 gcd()
print( g2 )

r = 10
C = math.pi * r * r             # 數學常數 圓周率 pi
print( C )

h1 = math.sin( 0 )              # 三角函數 正弦 sin()
print( h1 )
h2 = math.sin( 90 )             # sin( 弳度 )
print( h2 )
h3 = math.sin( 90 * math.pi / 180 )  # 弳度 = 角度 * ( pi / 180 )
print( h3 )
