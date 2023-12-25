import textwrap
class VMTranslator:

    count = 0; # static variable
    def vmLineToAsm(line):
        return VMTranslator.vmToAsm(line.strip().lower().split())

    def vmToAsm(tokens):
        if(len(tokens)==1):
            if(tokens[0]=='add'):
                return VMTranslator.vm_add()
            elif(tokens[0]=='sub'):
                return VMTranslator.vm_sub()
            elif(tokens[0]=='neg'):
                return VMTranslator.vm_neg()
            elif(tokens[0]=='eq'):
                return VMTranslator.vm_eq()
            elif(tokens[0]=='gt'):
                return VMTranslator.vm_gt()
            elif(tokens[0]=='lt'):
                return VMTranslator.vm_lt()
            elif(tokens[0]=='and'):
                return VMTranslator.vm_and()
            elif(tokens[0]=='or'):
                return VMTranslator.vm_or()
            elif(tokens[0]=='not'):
                return VMTranslator.vm_not()
            elif(tokens[0]=='return'):
                return VMTranslator.vm_return()
        elif(len(tokens)==2):
            if(tokens[0]=='label'):
                return VMTranslator.vm_label(tokens[1])
            elif(tokens[0]=='goto'):
                return VMTranslator.vm_goto(tokens[1])
            elif(tokens[0]=='if'):
                return VMTranslator.vm_if(tokens[1])
        elif(len(tokens)==3):
            if(tokens[0]=='push'):
                return VMTranslator.vm_push(tokens[1],int(tokens[2]))
            elif(tokens[0]=='pop'):
                return VMTranslator.vm_pop(tokens[1],int(tokens[2]))
            elif(tokens[0]=='function'):
                return VMTranslator.vm_function(tokens[1],int(tokens[2]))
            elif(tokens[0]=='call'):
                return VMTranslator.vm_call(tokens[1],int(tokens[2]))

    def vm_push(segment, offset):
        """Generate Hack Assembly code for a VM push operation assessed in Practical Assignment 6"""
        
        res = """\
            """

        if segment == "constant":

            return textwrap.dedent("""\
                    @{offset} // push constant {offset}
                    D=A
                    @SP
                    A=M
                    M=D
                    @SP
                    M=M+1
                    """).format(offset=offset)

        elif segment == "static":
            return textwrap.dedent("""\
                @{offset} // push static {offset}
                D=M
                @SP
                A=M
                M=D
                @SP
                M=M+1
            """).format(offset = int(offset) + 16) # static has base address 16

        else:
            res += textwrap.dedent("""
                @{offset}
                D=A
            """).format(offset=offset)
            
            if segment == "this":
                res += textwrap.dedent("""
                    @THIS 
                    A=M+D
                    """)
            elif segment == "that":
                res += textwrap.dedent("""            
                    @THAT
                    A=M+D
                    """)
            elif segment == "argument":
                res += textwrap.dedent("""            
                    @ARG
                    A=M+D
                    """)
            elif segment == "local":
                res += textwrap.dedent("""            
                    @LCL
                    A=M+D
                    """)
            elif segment == "temp":
                res += textwrap.dedent("""            
                    @5
                    A=A+D
                    """)
            elif segment == "pointer":
                res += textwrap.dedent("""            
                    @3
                    A=A+D
                    """)
    
            res += textwrap.dedent("""
            D=M
            @SP
            A=M
            M=D
            @SP
            M=M+1
            """)
        return res

    def vm_pop(segment, offset):
        """Generate Hack Assembly code for a VM pop operation assessed in Practical Assignment 6"""

        res = "// pop "+segment+" "+str(offset)  

        if segment == "static":
            res +=  """
                    @SP 
                    AM=M-1
                    D=M
                    @{offset}
                    M=D
            """.format(offset = int(offset) + 16)
            return res;

        else:
            res += textwrap.dedent("""
            @{offset}
            D=A
            """).format(offset = offset);

            if segment == "argument":
                res += textwrap.dedent("""
                        @ARG 
                        D=M+D 
                    """)

            elif segment == "local":
                res += textwrap.dedent("""
                    @LCL
                    D=M+D
                    @R13
                """)
            elif segment == "this":
                res += textwrap.dedent("""
                        @THIS 
                        D=M+D
                    """)
            
            elif segment == "that":
                res += textwrap.dedent("""
                        @THAT 
                        D=M+D
                    """)
            elif segment == "pointer":
                 res += textwrap.dedent("""
                        @3 
                        D=A+D
                    """)
            elif segment == "temp":
                 res += textwrap.dedent("""
                        @5 
                        D=A+D
                    """)

            res += textwrap.dedent("""
            @R13
            M=D
            @SP
            AM=M-1
            D=M
            @R13
            A=M
            M=D
            """)
        return res;
          
    def vm_add():
        """Generate Hack Assembly code for a VM add operation assessed in Practical Assignment 6"""
        return textwrap.dedent("""\
        // add
        @SP
        M=M-1
        A=M
        D=M
        A=A-1
        D=D+M
        M=D
        """)

    def vm_sub():
        """Generate Hack Assembly code for a VM sub operation assessed in Practical Assignment 6"""
        return textwrap.dedent("""
        // sub
        @SP
        M=M-1
        A=M
        D=M
        A=A-1
        D=M-D
        M=D
        """)

    def vm_neg():
        """Generate Hack Assembly code for a VM neg operation assessed in Practical Assignment 6"""
        return textwrap.dedent("""
        // neg
        @SP
        A=M-1
        M=-M
        """)

    def vm_eq():
        """Generate Hack Assembly code for a VM eq operation assessed in Practical Assignment 6"""
        VMTranslator.count += 1 # assign a unique label
        return textwrap.dedent("""
        // eq {count}
        @SP
        AM=M-1 
        D=M
        @SP
        A=M-1
        D=M-D
        M=-1
        @EQ_{count}
        0;JEQ
        @SP
        A=M-1
        M=0
        (EQ_{count})
        """).format(count=VMTranslator.count)

    def vm_gt():
        """Generate Hack Assembly code for a VM gt operation assessed in Practical Assignment 6"""
        VMTranslator.count += 1
        return textwrap.dedent("""
        // gt {count}
        @SP
        AM=M-1 
        D=M
        @SP
        A=M-1
        D=M-D
        M=-1
        @GT_{count}
        D;JGT
        @SP
        A=M-1
        M=0
        (GT_{count})
        """).format(count=VMTranslator.count)


    def vm_lt():
        """Generate Hack Assembly code for a VM lt operation assessed in Practical Assignment 6"""
        VMTranslator.count += 1
        return textwrap.dedent("""
        // gt {count}
        @SP
        AM=M-1 
        D=M
        @SP
        A=M-1
        D=M-D
        M=-1
        @LT_{count}
        D;JLT
        @SP
        A=M-1
        M=0
        (LT_{count})
        """).format(count=VMTranslator.count)

    def vm_and():
        """Generate Hack Assembly code for a VM and operation assessed in Practical Assignment 6"""
        return textwrap.dedent("""
        // and 
        @SP
        AM=M-1
        D=M
        A=A-1
        M=D&M
        """)

    def vm_or():
        """Generate Hack Assembly code for a VM or operation assessed in Practical Assignment 6"""
        return textwrap.dedent("""
        // OR
        @SP
        AM=M-1
        D=M
        A=A-1
        M=D|M
        """)

    def vm_not():
        """Generate Hack Assembly code for a VM not operation assessed in Practical Assignment 6"""
        return textwrap.dedent("""
        // not
        @SP
        A=M-1
        M=!M
        """)

    # == NOT ASSESSED ==

    def vm_label(label):
        """Generate Hack Assembly code for a VM label operation assessed in Practical Assignment 7"""
        return ""

    def vm_goto(label):
        """Generate Hack Assembly code for a VM goto operation assessed in Practical Assignment 7"""
        return ""

    def vm_if(label):
        """Generate Hack Assembly code for a VM if-goto operation assessed in Practical Assignment 7"""
        return ""

    def vm_function(function_name, n_vars):
        """Generate Hack Assembly code for a VM function operation assessed in Practical Assignment 7"""
        return ""

    def vm_call(function_name, n_args):
        """Generate Hack Assembly code for a VM call operation assessed in Practical Assignment 7"""
        return ""

    def vm_return():
        """Generate Hack Assembly code for a VM return operation assessed in Practical Assignment 7"""
        return ""

# A quick-and-dirty parser when run as a standalone script.
if __name__ == "__main__":
    import sys
    import os
    if(len(sys.argv) > 1):
        with open(sys.argv[1], "r") as a_file:
            for line in a_file:
                print(VMTranslator.vmLineToAsm(line))

"""
# A quick-and-dirty parser when run as a standalone script.
if __name__ == "__main__":
    import sys
    import os

    if len(sys.argv) > 1:
        with open(sys.argv[1], "r") as a_file:
            for line in a_file:
                tokens = line.strip().lower().split()
                if len(tokens) == 1:
                    if tokens[0] == "add":
                        print(VMTranslator.vm_add())
                    elif tokens[0] == "sub":
                        print(VMTranslator.vm_sub())
                    elif tokens[0] == "neg":
                        print(VMTranslator.vm_neg())
                    elif tokens[0] == "eq":
                        print(VMTranslator.vm_eq())
                    elif tokens[0] == "gt":
                        print(VMTranslator.vm_gt())
                    elif tokens[0] == "lt":
                        print(VMTranslator.vm_lt())
                    elif tokens[0] == "and":
                        print(VMTranslator.vm_and())
                    elif tokens[0] == "or":
                        print(VMTranslator.vm_or())
                    elif tokens[0] == "not":
                        print(VMTranslator.vm_not())
                    elif tokens[0] == "return":
                        print(VMTranslator.vm_return())
                elif len(tokens) == 2:
                    if tokens[0] == "label":
                        print(VMTranslator.vm_label(tokens[1]))
                    elif tokens[0] == "goto":
                        print(VMTranslator.vm_goto(tokens[1]))
                    elif tokens[0] == "if":
                        print(VMTranslator.vm_if(tokens[1]))
                elif len(tokens) == 3:
                    if tokens[0] == "push":
                        print(VMTranslator.vm_push(tokens[1], int(tokens[2])))
                    elif tokens[0] == "pop":
                        print(VMTranslator.vm_pop(tokens[1], int(tokens[2])))
                    elif tokens[0] == "function":
                        print(VMTranslator.vm_function(tokens[1], int(tokens[2])))
                    elif tokens[0] == "call":
                        print(VMTranslator.vm_call(tokens[1], int(tokens[2])))
"""
