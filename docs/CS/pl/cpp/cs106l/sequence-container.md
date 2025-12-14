The data in sequence containers are sequential, which is different from associative containers.

The most commonly used sequence containers are:
- `vector`: Dynamic array, the most commonly used container.
- `deque`: Double-ended queue, allows fast insertion and deletion at both ends.
- `list`: Doubly linked list, allows fast insertion and deletion at any position, but slow random access.
- `forward_list`: Singly linked list, allows fast insertion and deletion at any position, but slow random access and only forward traversal.
- `array`: Fixed-size array,

## Vector

![alt text](res/images/image-9.png)

```cpp
std::vector<int> vecInt; // vector of int
std::vector<std::string> vecStr; // vector of string
std::vector<myStruct> vecStruct; // vector of user-defined struct
std::vector<std::vector<int>> vec2D; // 2D vector(vector of vector<int>)
```

### Member Functions

![alt text](res/images/image-6.png)

![alt text](res/images/image-10.png)
![alt text](res/images/image-11.png)

关于 `.at(index)` 在越界时的报错：

![alt text](res/images/image-8.png)

## Deque

Double ended queue 双端队列

![alt text](res/images/image-7.png)

![alt text](res/images/image-12.png)
![alt text](res/images/image-13.png)

## Container Adaptors

![alt text](res/images/image-14.png)

cpp 中的 stack 和 queue 实际是阉割版的 deque 和 vector。

![alt text](res/images/image-16.png)

有 deque & vector 还要用 stack & queue 的原因：

![alt text](res/images/image-15.png)
