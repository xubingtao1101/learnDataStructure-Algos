class Ruler:
    '''
        分析书上的例图：
            1、主刻度线为3的话，那么1/2处的刻度线长度就为2，1/4处(其余)的刻度线长度就为1；(3 -> 2 -> 1) 
                最小是四分之一，三减一的二次方
            
            2、主刻度线为4的话，那么1/2处的刻度线长度就为3，1/4处的刻度线长度为2，其余刻度为1；(4 -> 3 -> 2 -> 1) 
                最小是八分之一
           
            3、主刻度线为5的话，1/2处的刻度线长度为4，1/4处刻度线长度为3，1/8处为2，其余为1。(5 -> 4 -> 3 -> 2 -> 1) 
                最小是十六分之一
        好像这样分析递归写法帮助不大

    '''

    def draw(self, scale, lable=" "):
        if lable != " ":
            print('-'*scale, str(lable)) //打印刻度
        else:
            print('-'*scale)

    def recursive(self, scale):
        if scale > 0:
            self.recursive(scale-1)
            self.draw(scale)
            self.recursive(scale-1)

    def main(self, length, scale):
        '''length是尺子的长度，scale是每段间距中的小刻度数量'''
        print('-'*scale, 0)
        for num in range(1, length+1):
            self.recursive(scale-1)
            print('-'*scale, str(num))

if __name__ == "__main__":
    ruler = Ruler()
    ruler.main(2,5)

