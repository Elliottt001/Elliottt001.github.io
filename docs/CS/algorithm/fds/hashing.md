## 概念

![alt text](res/images/image-59.png)

将 key 映射到 i

symbol table是哈希表最常用的场景

![alt text](res/images/image-60.png)

## 哈希函数

![alt text](res/images/image-61.png)

类似32进制：27就够，但是32可以用位运算（左翼5位），快

## 解决冲突

### 分离链表法

![alt text](res/images/image-62.png)
![alt text](res/images/image-63.png)
![alt text](res/images/image-64.png)
![alt text](res/images/image-65.png)
![alt text](res/images/image-66.png)
tablesize 和要插的数据量尽量相近，即 $\lambda$ 接近1

### 开放寻址法

![alt text](res/images/image-67.png)

一般要求 $\lambda < 0.5$

1. 线性查找

![alt text](res/images/image-68.png)

理论上平均探测次数见上图最下面

2. 二次探测

![alt text](res/images/image-69.png)

二次探测work的条件：一半空且tablesize为质数

![alt text](res/images/image-70.png)

![alt text](res/images/image-71.png)
![alt text](res/images/image-72.png)

这比直接算平方算的快

不直接删除而是更改元素状态的原因：如果直接删除查找的话到这里就退出了，后面的元素找不到了

![alt text](res/images/image-73.png)

3. 二次哈希

![alt text](res/images/image-74.png)

## 重哈希

$$O(N)$$

![alt text](res/images/image-75.png)

出现问题，重新建哈希表，填入原来元素，用新哈希函数填入其他

