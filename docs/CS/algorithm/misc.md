- 必须要当一个循环完整执行结束才知道的东西用flag

    注意对数组中元素用flag记录时，循环结束flag重新置0

- `return` 作用是返回 + 结束，因此，可以这样：
	```c
	int inarry(int* arr, int size, int a)
	{
		int i;
		for(i = 0; i < size; i++){
			if(arr[i] == a){
				return 1;
			}
		}
		return 0;
	}
	```


## 循环结束之后再下结论

找到了可以立刻 return，没找到不能在循环第一轮就 return 0：后面可能还有。

```c
int contains(const int arr[], int size, int value) {
    for (int i = 0; i < size; ++i) {
        if (arr[i] == value) return 1;
    }
    return 0;
}
```

如果还要继续做别的事，不能直接退出函数，就用 flag。比如判断一个数是不是素数，发现因子后 `is_prime = 0; break;`，最后再统一输出。

## 边界先拿小例子试

- 空数组 / 只有一个元素，循环会不会多走一步？
- `i < n` 和 `i <= n`，最后访问的是 `arr[n - 1]` 还是越界的 `arr[n]`？
- 二分查找区间是 `[left, right]` 还是 `[left, right)`，初始化和更新要配套。
- 删除链表节点，先接好前后，再 free，free 之后不能读 `node->next`。

拿 `[1, 2, 3]` 找 3 试一下，就能发现“第一轮没找到便返回”的问题。
