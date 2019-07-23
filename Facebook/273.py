class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return 'Zero'
        one_to_nine = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
        ten_to_nineteen = ['Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
        twenty_to_ninety = ['Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
        thousand_to_billion = ['Thousand', 'Million', 'Billion']
        res = ''
        i = 0
        while num > 0:
            cur = num % 10
            if i % 3 == 0:
                if num % 1000 > 0 and i > 0:
                    res = thousand_to_billion[(i//3) - 1] + ' ' + res
                if (num // 10) % 10 == 1:
                    res = ten_to_nineteen[cur] + ' ' + res
                    num = num // 10
                    i += 1
                else:
                    if cur > 0:
                        res = one_to_nine[cur-1] + ' '+ res
            elif i % 3 == 1:
                if cur >= 2:
                    res = twenty_to_ninety[cur-2] + ' ' + res
            else:
                if cur > 0:
                    res = one_to_nine[cur-1] + ' Hundred ' + res
            num = num // 10
            i += 1
        return ' '.join(res.split())
    def numberToWords2(self, num: int) -> str:
        if num == 0:
            return 'Zero'
        one_to_nineteen = 'One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'.split()
        tens = ['Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
        
        def words(num):
            if num == 0:
                return []
            elif num <= 19:
                return [one_to_nineteen[num-1]]
            elif num < 100:
                return [tens[num//10 - 2]] + words(num % 10)
            elif num < 1000:
                return [one_to_nineteen[num//100 - 1]] + ['Hundred'] + words(num % 100)
            else:
                for i, yo in enumerate(['Thousand', 'Million', 'Billion'], 1):
                    if num < 1000 ** (i+1):
                        return words(num // (1000**i)) + [yo] + words(num % (1000**i))
        return ' '.join(words(num))
