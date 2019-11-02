# 递归（Recursive）

**一种除for和while之外的描述迭代的方法**

## 分析递归算法

1. 计算阶乘
* 函数从n一直减到n=0，所以一共运行了n+1次
* 操作总数是O(n)，每次调用的操作次数是O(1)

2. 绘制英式标尺
* 不会分析这个，先挂着

3. 执行二分查找
* 对含有n个有序元素的队列进行二分查找，至多进行(logn)+1次递归调用，所以时间复杂度为O(logn)

4. 计算磁盘使用情况
* 树遍历算法的一种实现，以后用就完事了

>>    os.path.getsize(path) 

>>    os.path.isdir(path)

>>    os.listdir(path)

>>    os.path.join(path,filename) 