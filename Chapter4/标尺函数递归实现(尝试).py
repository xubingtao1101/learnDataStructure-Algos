import math


def ruler_try(total_length: int, tick_length: int, container: list):
    '''
    分析书上的例图：
        1、主刻度线为3的话，那么1/2处的刻度线长度就为2，1/4处(其余)的刻度线长度就为1；(3 -> 2 -> 1) 最小是四分之一
        2、主刻度线为4的话，那么1/2处的刻度线长度就为3，1/4处的刻度线长度为2，其余刻度为1；(4 -> 3 -> 2 -> 1) 最小是八分之一
        3、主刻度线为5的话，1/2处的刻度线长度为4，1/4处刻度线长度为3，1/8处为2，其余为1。(5 -> 4 -> 3 -> 2 -> 1) 最小是十六分之一
    '''
    minimum = 1/pow(2, (tick_length-1))
    print(minimum)


container = list()
#ruler_try(3,3, container)
#ruler_try(2,4, container)
ruler_try(1,5, container)
