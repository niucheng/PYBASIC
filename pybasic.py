#!/usr/bin/env python
# coding: utf-8

'''PYBASIC: a really simple BASIC interpreter in Python based on uBASIC.

The (non-interactive) uBASIC interpreter supports only the most basic BASIC
functionality:
    if/then/else,
    for/next,
    let,
    goto,
    gosub,
    print,
    and mathematical expressions.
There is only support for integer variables and the variables can only have
single character names.
'''

import ctypes

def run(program=None):
    ubasic = ctypes.cdll.LoadLibrary('./ubasic.so')
    #
    ubasic_init = ubasic.ubasic_init
    ubasic_init.argtypes = [ctypes.c_char_p]
    ubasic_init.restype = ctypes.c_void_p
    ubasic_run = ubasic.ubasic_run
    ubasic_run.argtypes = [ctypes.c_void_p]
    ubasic_run.restype = ctypes.c_void_p
    ubasic_finished = ubasic.ubasic_finished
    ubasic_finished.argtypes = [ctypes.c_void_p]
    ubasic_finished.restype = ctypes.c_int
    #
    ubasic_init(program)
    ubasic_run(None)
    while not ubasic_finished(None):
        ubasic_run(None)

if __name__ == "__main__":
    s = '''\
10 gosub 100
20 for i = 1 to 9
25     for j = 1 to i
30         print j;"*";i;"=";i*j,
35     next j
37     print
40 next i
50 print "Have a lot of fun!"
60 end
100 print "Multiplication Table"
110 return
'''
    run(s)

