# -*- coding: utf-8 -*-
"""
Created on Aug 11 2026

@author: Lee, Pin-Hua
"""

x1 = eval( input("輸入 A 點的 x 座標 : ") )
y1 = eval( input("輸入 A 點的 y 座標 : ") )

x2 = eval( input("輸入 B 點的 x 座標 : ") )
y2 = eval( input("輸入 B 點的 y 座標 : ") )

distance = ( ( ( x1 - x2 ) ** 2 ) + ( ( y1 - y2 ) ** 2 ) ) ** 0.5     # 座標距離 = ( ( ( x1 - x2 ) ** 2 ) + ( ( y1 - y2 ) ** 2 ) ) ** 0.5

print("A 點座標為 ( {}, {} )".format( x1, y1 ))
print("B 點座標為 ( {}, {} )".format( x2, y2 ))
print("兩點距離為 {:.4f}".format( distance ))
