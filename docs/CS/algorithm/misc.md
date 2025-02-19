- 必须要当一个循环完整执行结束才知道的东西用flag

    注意对数组中元素用flag记录时，循环结束flag重新置0

- `return` 作用是返回 + 结束，因此，可以这样：
	```c
	int inarry(int* arr, int size, int a)
	{
		int i, flag = 0;
		for(i = 0; i < size; i++){
			if(arr[i] == a){
				return 1;
			}
		}
		return 0;
	}
	```
