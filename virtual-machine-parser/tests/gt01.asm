
// gt 5
@SP
AM=M-1 
D=M
@SP
A=M-1
D=M-D
M=-1
@GT_5
D;JGT
@SP
A=M-1
M=0
(GT_5)

// gt 6
@SP
AM=M-1 
D=M
@SP
A=M-1
D=M-D
M=-1
@GT_6
D;JGT
@SP
A=M-1
M=0
(GT_6)

(END)
@END
0;JMP