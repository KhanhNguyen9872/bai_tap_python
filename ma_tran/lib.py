from os import system,name
from sys import exit
def clear():
    if name=='nt':
        system('cls')
    else:
        system('clear')

def matrix_initialization(m,n):
    global matrix
    matrix=[]
    for i in range(0,int(m),1):
        temp_matrix=[]
        for j in range(0,int(n),1):
            temp_matrix.append(int(0))
        matrix.append(temp_matrix)
    return True

def head_matrix(m,n):
    print(" 0 | max column: {0} | max row: {1}".format(str(n),str(m)))

def left_matrix(i):
    print(f" {i} | ",end="")

def print_matrix(m,n):
    head_matrix(m,n)
    count=0
    for i in range(0,int(m),1):
        left_matrix(i+1)
        for j in matrix[i]:
            print(str(j),end=" ")
        print()

def input_matrix(m,n):
    passk=0
    count=1
    temp_matrix=[]
    head_matrix(m,n)
    while 1:
        left_matrix(count)
        try:
            temp_input=str(input())
            temp_input=[round(float(x),2) for x in temp_input.split()]
            if (len(temp_input)==n):
                passk=1
        except KeyboardInterrupt:
            print("Exiting...")
            exit()
        except:
            passk=0
        if (passk==1):
            temp_matrix.append(temp_input)
            count+=1
        elif (passk==0):
            continue
        if (count==m+1):
            break
    return temp_matrix

def trapezoid(e,m,n):
    exec(f"""global matrix
matrix={e}""")
    one=-1
    for i in range(0,len(matrix[0]),1):
        if int(matrix[0][i])==0:
            continue
        else:
            one=int(i+1)
            break
    if one==-1:
        print("The first row of the matrix does not contain the first non-zero element")
        exit()
    else:
        loop_calc=1
        for row in range(1,len(matrix),1):
            for num in range(0,len(matrix[row]),1):
                if int(num)<int(one):
                    if int(matrix[row][num])==0:
                        continue
                    else:
                        for i in range(0,len(matrix),1):
                            if (int(i)==int(row)) or (int(matrix[i][num])==0) or (int(matrix[row][num])==0):
                                continue
                            else:
                                up=float(matrix[row][num])
                                down=float(matrix[i][num])
                                print("\n({4}) h{0} -> h{0} - ({1}/{2}) * h{3}".format(str(row+1),str(up),str(down),str(i+1),str(loop_calc)))
                                for j in range(0,len(matrix[row]),1):
                                    matrix[row][j]=float(matrix[row][j])-float(up/down)*float(matrix[i][j])
                                print_matrix(m,n)
                                loop_calc+=1
                else:
                    one=int(num+1)
                    break