# -*- coding: utf-8 -*-
"""
Created on Aug 6 2026

@author: Lee, Pin-Hua
"""

a = 5                    # 整數 ( int )
print( a )
print( type( a ) )       # 資料型別 type()

b = 5.5                  # 浮點數 ( float )
print( b )
print( type( b ) )

c = True                 # 布林值 ( bool )
print( c )
print( type( c ) )

d = "I Love Python"      # 字串型態 ( str )
print( d )
print( type( d ) )
d1 = 'I Love Python'
print( d1 )
print( type( d1 ) )
d2 = "123"
print( d2 )
print( type( d2 ) )
d3 = "5.5"
print( d3 )
print( type( d3 ) )
d4 = '''asd asasd as     
asdkjashjd asd asd
asdj kajsd asd
asd asd'''               # 連續三個單引號或雙引號亦可跨行形成字串
print( d4 )
print( type( d4 ) )

print("c:\note\temp")    # 把結果印出於畫面上 print()
                         # \n 換行字元
                         # \t Tab鍵空格
print("c:\\note\\temp")  # \\ 單純反斜線

print( "Hello! " + "Python." )     # ( + ) 字串串接
print( "Hello! " * 3 )             # ( * ) 重複字串

print( ord( '1' ) )      # 字元轉成 Unicode 數值 ord()
print( ord( 'A' ) )
print( ord( 'a' ) )

print( chr( 57 ) )       # Unicode 數值轉成字元 chr()
print( chr( 90 ) )
print( chr( 122 ) )
