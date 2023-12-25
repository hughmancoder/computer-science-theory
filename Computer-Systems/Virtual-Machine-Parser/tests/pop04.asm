// pop static 10
                    @SP 
                    AM=M-1
                    D=M
                    @26
                    M=D
            // pop temp 7
@7
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