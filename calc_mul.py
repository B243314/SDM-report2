#!/usr/bin/python3

import re
                
#After Modifing     
def calc(A, B):
    # AとBが数値（intまたはfloat）かどうかをチェック
    if not isinstance(A, (int, float)) or not isinstance(B, (int, float)):
        return -1

    # A, B の範囲チェック（0 < A < B < 1000）
    if 0 < A < B < 1000:
        return round(A * B, 10)  # 浮動小数点誤差を防ぐために丸める
    else:
        return -1
                
def main ():
	matchstring = ''
	while matchstring != 'end':
                A = input ('input A: ')
                B = input ('input B: ')
                print ('input A * input B = ', calc(A,B))

if __name__ == '__main__':
	main()
