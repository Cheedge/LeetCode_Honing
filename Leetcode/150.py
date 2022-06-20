"""
Medium
￼
3293
￼
647
￼
Add to List
￼
Share
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, and /. Each operand may be an integer or another expression.

Note that division between two integers should truncate toward zero.

It is guaranteed that the given RPN expression is always valid. That means the expression would always evaluate to a result, and there will not be any division by zero operation.

 

Example 1:

Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
Example 2:

Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
Example 3:

Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
 

Constraints:

1 <= tokens.length <= 104
tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200].

"""
def evalRPN(tokens):
    """
    :type tokens: List[str]
    :rtype: int
    """
    import math
    # 1. find operator (+,-,*,/) at i, eval(t[i-2]+t[i-1]+t[i]) -> int -> tokens[:i-2] + [int] + tokens[i+1:]
    # t = tokens
    if len(tokens)==1: return int(tokens[0])
    op = {'+', '-', '*', '/'}
    # use stack to store
    store = list()
    for i in range(len(tokens)):
        if tokens[i] in op:
            it1 = store.pop()
            it2 = store.pop()
            #这里"."很重要!!!!!!!!!!!!!!!!!!!!!!!!!!!111111
            it = int(eval(it2+tokens[i]+it1+'.'))
            store.append(str(it))
        else:
            store.append(tokens[i])
    return int(it)