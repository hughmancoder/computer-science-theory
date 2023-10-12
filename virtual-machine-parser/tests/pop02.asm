// pop local 1
@1
D=A

@LCL
D=M+D
@R13

@R13
M=D
@SP
AM=M-1
D=M
@R13
A=M
M=D
// pop argument 1
@1
D=A

@ARG 
D=M+D 

@R13
M=D
@SP
AM=M-1
D=M
@R13
A=M
M=D
// pop this 2
@2
D=A

@THIS 
D=M+D

@R13
M=D
@SP
AM=M-1
D=M
@R13
A=M
M=D
// pop that 2
@2
D=A

@THAT 
D=M+D

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