class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        return (lambda S=[]:any(S.append([lambda S,t:S.pop()+S.pop(),lambda S,t:-S.pop()+S.pop(),lambda S,t:S.pop()*S.pop(),lambda S,t:int(1/S.pop()*S.pop()),lambda S,t:int(t)]["+-*/".find(t)](S,t))for t in tokens)or S[0])()
