
// gt 3
@SP
AM=M-1 
D=M
@SP
A=M-1
D=M-D
M=-1
@LT_3
D;JLT
@SP
A=M-1
M=0
(LT_3)

// gt 4
@SP
AM=M-1 
D=M
@SP
A=M-1
D=M-D
M=-1
@LT_4
D;JLT
@SP
A=M-1
M=0
(LT_4)

(END)
@END
0;JMP