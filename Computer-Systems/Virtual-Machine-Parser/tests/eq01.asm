
// eq 1
@SP
AM=M-1 
D=M
@SP
A=M-1
D=M-D
M=-1
@EQ_1
0;JEQ
@SP
A=M-1
M=0
(EQ_1)

// eq 2
@SP
AM=M-1 
D=M
@SP
A=M-1
D=M-D
M=-1
@EQ_2
0;JEQ
@SP
A=M-1
M=0
(EQ_2)

(END)
@END
0;JMP