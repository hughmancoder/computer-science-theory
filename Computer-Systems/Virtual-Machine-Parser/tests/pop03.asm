// pop pointer 0
@0
D=A

@3 
D=A+D

@R13
M=D
@SP
AM=M-1
D=M
@R13
A=M
M=D
// pop temp 1
@1
D=A

@5 
D=A+D

@R13
M=D
@SP
AM=M-1
D=M
@R13
A=M
M=D

(END)
@END
0;JMP