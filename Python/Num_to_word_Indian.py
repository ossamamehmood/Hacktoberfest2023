# This code will convert any whole number to word in Indian number system
def num_to_wds_indi(num):
    d = {0 : 'zero', 1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four', 5 : 'five',
          6 : 'six', 7 : 'seven', 8 : 'eight', 9 : 'nine', 10 : 'ten',
          11 : 'eleven', 12 : 'twelve', 13 : 'thirteen', 14 : 'fourteen',
          15 : 'fifteen', 16 : 'sixteen', 17 : 'seventeen', 18 : 'eighteen',
          19 : 'nineteen', 20 : 'twenty',
          30 : 'thirty', 40 : 'forty', 50 : 'fifty', 60 : 'sixty',
          70 : 'seventy', 80 : 'eighty', 90 : 'ninety'}
    th = 1000
    lk = th * 100
    cr = lk * 100

    assert(0<=num)

    if(num<20):
        return d[num]
    if(num<100):
        if(num % 10 == 0): return d[num]
        else: return d[num//10*10] + ' ' + d[num%10]
    if(num<th):
        if(num % 100 == 0): return d[num//100] + ' hundred'
        else: return d[num//100] + ' hundred and ' + num_to_wds_indi(num%100)
    if(num<lk):
        if(num % th == 0): return num_to_wds_indi(num//th) + ' thousand'
        else: return num_to_wds_indi(num//th) + ' thousand, ' + num_to_wds_indi(num%th)
    if(num<cr):
        if(num % lk == 0): return num_to_wds_indi(num//lk) + ' lakh'
        else: return num_to_wds_indi(num//lk) + ' lakh, ' + num_to_wds_indi(num%lk)
    
    if(num % cr == 0): return num_to_wds_indi(num//cr) + ' crore'
    else: return num_to_wds_indi(num//cr) + ' crore, ' + num_to_wds_indi(num%cr)
    raise AssertionError('num is too large: %s' % str(num))

num = int(input())
print(num_to_wds_indi(num))
