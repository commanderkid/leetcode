class Solution:
    def romanToInt(self, s):
        #dic = (['I' = 1, 'II' = 2, 'III' = 3, 'IV' = 4, 'V' = 5, 'VI' = 6, 'VII' = 7, 'VIII' = 8, 'IX' = 9, 'X' = 10, 'XX' = 20, 'XXX' = 30, 'XL' = 40, 'L' = 50, 'LX' = 60, 'LXX' = 70, 'LXXX' = 80, 'XC' = 90, 'C' = 100, 'CC' = 200, 'CCC' = 300, 'CD' = 400, 'D' = 500, 'DC' = 600, 'DCC' = 700, 'DCCC' = 800, 'CM' = 900, 'M' = 1000])
        dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        mass = []
        otv = 0
        for i in s:
            mass.append(dic.get(i))
        if len(mass) == 0:
            return 0
        elif len(mass) == 1 :
            return mass[0]
        else:
            for i in range(len(mass) - 1):
                if mass[i] < mass[i+1]:
                    otv -= mass[i]
                else:
                    otv += mass[i]
            otv += mass[-1]
        return otv
