#如果遇到符號就pop兩個值出來做計算，普通數字就存stack
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for n in tokens:
            if n in ("+","-","*","/"):
                n1 = stack.pop()
                n2 = stack.pop()
                if n == "+":
                    stack.append(n2 + n1)
                elif n == "-":
                    stack.append(n2 - n1)
                elif n == "*":
                    stack.append(n2 * n1)
                elif n == "/":
                    stack.append(int(n2 / n1))
            else :
                stack.append(int(n))
        return stack.pop()
# tokens = ["1","2","+","3","*","4","-"],stack=[]
# n = "1"-> not in oper ->stack=[1]
# n = "2"-> not in oper ->stack=[1,2]
# n = "+"-> in oper -> n1=2,n2=1 stack=[2+1,]
# n = "3"-> not in oper -> stack=[3,3]
# n = "*"-> in oper -> n1=3,n2=3 stack=[3*3]
# n = "4"-> not in oper -> stack=[9,4]
# n = "-"-> in oper -> n1=4,n2=9 stack=[9-4]

