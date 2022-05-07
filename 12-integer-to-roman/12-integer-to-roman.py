class Solution:
    def intToRoman(self, num: int) -> str:
        SingleVal = {1:"I",5:"V",10:"X",50:"L",100:"C",500:"D",1000:"M"}
        DoubleVal = {4:"IV",9:"IX",40:"XL",90:"XC",400:"CD",900:"CM"}
        
        Result = ""
        
        Number = num
        
        while Number > 0:
            if Number >= 1000:
                Result += SingleVal[1000]
                Number -= 1000
                
            elif Number >= 900:
                Result += DoubleVal[900]
                Number -= 900
                
            elif Number >= 500:
                Result += SingleVal[500]
                Number -= 500
                
            elif Number >= 400:
                Result += DoubleVal[400]
                Number -= 400
            
            elif Number >= 100:
                Result += SingleVal[100]
                Number -= 100
            
            elif Number >= 90:
                Result += DoubleVal[90]
                Number -= 90
            
            elif Number >= 50:
                Result += SingleVal[50]
                Number -= 50
            
            elif Number >= 40:
                Result += DoubleVal[40]
                Number -= 40
                
            elif Number >= 10:
                Result += SingleVal[10]
                Number -= 10
                    
            elif Number >= 9:
                Result += DoubleVal[9]
                Number -= 9
            
            elif Number >= 5:
                Result += SingleVal[5]
                Number -= 5
            
            elif Number >= 4:
                Result += DoubleVal[4]
                Number -= 4
            
            elif Number >= 1:
                Result += SingleVal[1]
                Number -= 1
            
        return Result