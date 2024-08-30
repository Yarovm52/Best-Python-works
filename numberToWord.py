def numberToWords(num):
        if num == 0:
            return 'Zero'
        ones = {'0':'','1':'One','2':'Two','3':'Three','4':'Four','5':'Five','6':'Six','7':'Seven','8':'Eight','9':'Nine'}
        tens = {'0':'','10':'Ten','11':'Eleven','12':'Twelve','13':'Thirteen','14':'Fourteen','15':'Fifteen','16':'Sixteen','17':'Seventeen','18':'Eighteen','19':'Nineteen','2':'Twenty','3':'Thirty','4':'Forty','5':'Fifty','6':'Sixty','7':'Seventy','8':'Eighty','9':'Ninety'}
        num = list(str(num))
        num = list('0' * (10 - len(num))) + num
        result = []
        while len(num) != 0:
            if len(num) == 10:
                if num[0] != '0':
                    result.append(ones[num[0]])
                    if ones[num[0]] != '2':
                        result.append('Billion')
                    else:
                        result.append('Billions')
                num.pop(0)
            elif len(num) == 9:
                if num[0] != '0':
                    result.append(ones[num[0]])
                    result.append('Hundred')
                    if num[1] + num[2] == '00':
                        result.append('Million')
                if num[1]+num[2] in tens:
                    result.append(tens[num[1]+num[2]])
                    result.append('Million')
                elif tens[num[1]] + ones[num[2]] != '':
                    result.append(tens[num[1]])
                    result.append(ones[num[2]])
                    result.append('Million')
                num.pop(0)
                num.pop(0)
                num.pop(0)
            elif len(num) == 6:
                if num[0] != '0':
                    result.append(ones[num[0]])
                    result.append('Hundred')
                    if num[1] + num[2] == '00':
                        result.append('Thousand')
                if num[1]+num[2] in tens:
                    result.append(tens[num[1]+num[2]])
                    result.append('Thousand')
                elif tens[num[1]] + ones[num[2]] != '':
                    result.append(tens[num[1]])
                    result.append(ones[num[2]])
                    result.append('Thousand')
                num.pop(0)
                num.pop(0)
                num.pop(0)
            elif len(num) == 3:
                if num[0] != '0':
                    result.append(ones[num[0]])
                    result.append('Hundred')
                if num[1]+num[2] in tens:
                    result.append(tens[num[1]+num[2]])
                elif tens[num[1]] + ones[num[2]] != '':
                    result.append(tens[num[1]])
                    result.append(ones[num[2]])
                num = ''
        summary = ''
        for idx, number in enumerate(result):
            if number != '':
                summary += ' ' + number
        summary = list(summary)
        summary.pop(0)
        return ''.join(summary)
    
    
print(numberToWords(2**16-1))