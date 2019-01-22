# -*- coding: utf-8 -*-
from __future__ import division

####################导入时间模块
import time
###############计算当前时间
start_time=time.time()
'''
算法：马青公式

π/4=4arctan1/5-arctan1/239

这个公式由英国天文学教授约翰·马青于1706年发现。他利用这个公式计算到了100位的圆周率。马青公式每计算一项可以得到1.4位的十进制精度。因为它的计算过程中被乘数和被除数都不大于长整数，所以可以很容易地在计算机上编程实现。
'''
number = int(input('请输入想要计算到小数点后的位数n:'))

# 多计算10位，防止尾数取舍的影响
number1 = number+10

# 算到小数点后number1位
b = 10**number1

# 求含4/5的首项
x1 = b*4//5
# 求含1/239的首项
x2 = b// -239

# 求第一大项
he = x1+x2
#设置下面循环的终点，即共计算n项
number *= 2

#循环初值=3，末值2n,步长=2
for i in range(3,number,2):
    # 求每个含1/5的项及符号
    x1 //= -25
    # 求每个含1/239的项及符号
    x2 //= -57121
    # 求两项之和
    x = (x1+x2) // i
    # 求总和
    he += x

# 求出π
pai = he*4
#舍掉后十位
pai //= 10**10

############ 输出圆周率π的值
paistring=str(pai)
result=paistring[0]+str('.')+paistring[1:len(paistring)]
print (result)

end_time=time.time()
print('计算'+str(int(number/2))+'位π，总共耗时：' + str(end_time - start_time) + 's')
