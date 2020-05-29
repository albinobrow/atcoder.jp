#!/usr/bin/env python
# coding: UTF-8

import sys
if sys.version_info[0]<3: input=raw_input

class StandardInput:

    def stdin_string(self):
        self.s=str(input().rstrip())
        return self.s

    def stdin_integer(self):
        self.n=int(input().rstrip())
        return self.n

    def stdin_array(self):
        self.arr=input().rstrip().split()
        return self.arr

    def stdin_integer_array(self):
        self.arr=list(map(int,input().rstrip().split()))
        return self.arr

def test(n):
    if n==3:
        return 'bon'
    elif n==0 or n==1 or n==6 or n==8:
        return 'pon'
    else:
        return 'hon'

def main():
    obj=StandardInput()
    n=int(obj.stdin_string()[-1])
    print(test(n))
        
if __name__ == '__main__':
    main()
