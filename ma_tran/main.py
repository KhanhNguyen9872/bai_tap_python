#!/bin/python3    
if (__name__=='__main__'):
    # import module
    import sys,lib
    
    # define variable
    global matrix
    matrix=[]
    
    # clear screen
    lib.clear()
    
    # input m and n
    try:
        m,n=[int(x) for x in input("Input mXn: ").replace("X","x").split("x")]
        if (m==0) or (n==0):
            print("m and n must bigger than 0")
            sys.exit()
    except ValueError:
        print("Please input mXn!\nExample: 3x5\n         4x8\n")
        sys.exit()
    sum_matrix=int(m*n)
    
    # matrix initialization
    lib.matrix_initialization(m,n)
    lib.print_matrix(m,n)
    ask=str(input("Do you want input matrix? [Y/n]: "))
    match ask:
        case ("Y"|"y"):
            print()
            matrix=lib.input_matrix(m,n)
        case ("N"|"n"):
            print("Exiting...")
            sys.exit()
    while 1:
        ask=str(input("""
Please choose calculation method:
1. Hình thang (trapezoid)
Ctrl + C -> Exit

Your choose: """))
        match ask:
            case "1":
                print()
                lib.trapezoid(str(matrix),m,n)
                break