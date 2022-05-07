class Solution:
    def romanToInt(self, s: str) -> int:
        Single_Sym_Val = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        Double_Sym_Val = {"IV":4 , "IX":9 , "XL":40,"XC":90,"CD":400,"CM":900}
        Res = 0
        i = 0
        while i < len(s):
            if i < len(s)-1:
                Duo = s[i]+s[i+1]
            else:
                Duo = 0
            Uno = s[i]
            if Duo in Double_Sym_Val.keys():
                Res += Double_Sym_Val[Duo]
                i += 2
            else:
                Res += Single_Sym_Val[Uno]
                i += 1
        
        return Res
        