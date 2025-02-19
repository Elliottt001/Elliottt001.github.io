[八大排序CSDN](https://blog.csdn.net/Edward_Asia/article/details/121419975)

## 插入排序

```c
#include <assert.h>

void InsertSort(int* array, int size)
{
    assert(array);

    // 遍历未排序的部分
    for (int sortedEndIndex = 0; sortedEndIndex < size - 1; ++sortedEndIndex) // 已排序部分的最后一个下标
    {
        int unsortedElement = array[sortedEndIndex + 1]; // 需要插入到已排序部分的元素
        int currentIndex = sortedEndIndex; // 当前比较的已排序元素下标

        // 单趟插入过程：从已排序部分的末尾向前遍历
        while (currentIndex >= 0 && array[currentIndex] > unsortedElement)
        {
            array[currentIndex + 1] = array[currentIndex]; // 将较大的已排序元素向后移动
            --currentIndex; // 向前比较
        }

        // 将未排序元素插入到正确位置
        array[currentIndex + 1] = unsortedElement;
    }
}
```

**插入排序算法解释**

1. **算法概述**：
   插入排序的核心思想是：将数组划分为“已排序部分”和“未排序部分”。从未排序部分逐个取出元素，插入到已排序部分的正确位置，直到整个数组有序。

   已排序部分：从1遍历增加。

   未排序部分：已排序部分的后面一个。

2. **步骤**：
   - 初始状态时，数组的第一个元素视为“已排序部分”，剩余部分是“未排序部分”。
   - 遍历未排序部分，取当前元素（`unsortedElement`，即已排序部分后面一个），在已排序部分从后向前扫描：
     - 如果扫描到的已排序元素比当前元素大，则将其后移。
     - 如果找到比当前元素小的元素或扫描到已排序部分的起始位置，则停止。
   - 将当前元素插入到已排序部分的正确位置。

3. **时间复杂度**：
   - 最好情况：已排序数组，时间复杂度为 $(O(n))$。
   - 最坏情况：逆序数组，时间复杂度为 $(O(n^2))$。

## 希尔排序

```c
#include <assert.h>

void ShellSort(int* array, int size)
{
    assert(array);

    int gap = size; // 初始化间隔

    // 不断缩小间隔，直到间隔为 1
    while (gap > 1)
    {
        // 缩小间隔的策略，可以使用 gap /= 2 或 gap = gap / 3 + 1
        gap = gap / 3 + 1;

        // 对每组间隔为 gap 的子数组进行插入排序
        for (int i = 0; i < size - gap; ++i)
        {
            int sortedEndIndex = i; // 已排序部分的最后一个下标
            int unsortedElement = array[sortedEndIndex + gap]; // 需要插入的元素

            // 在当前组内从后向前插入排序
            while (sortedEndIndex >= 0 && array[sortedEndIndex] > unsortedElement)
            {
                array[sortedEndIndex + gap] = array[sortedEndIndex]; // 向后移动较大元素
                sortedEndIndex -= gap; // 按间隔向前比较
            }

            // 插入未排序元素到正确位置
            array[sortedEndIndex + gap] = unsortedElement;
        }
    }
}
```


**核心思想**

希尔排序是一种基于插入排序的改进算法，通过逐步减少比较和移动的距离（称为**间隔**或**步长** `gap`），最终对整个数组进行插入排序，从而提高效率。

**算法步骤**

1. **初始化间隔**：
   - 从一个较大的间隔开始，将数组分为若干子组（每组元素间隔为 `gap`）。
   - 通常间隔的缩减公式是 `gap = gap / 3 + 1` 或 `gap /= 2`。

2. **组内插入排序**：
   - 对每组中的元素进行插入排序。
   - 按照间隔比较，逐步将较小的元素插入到正确位置。

3. **逐步缩小间隔**：
   - 当 `gap` 缩减到 1 时，整个数组会被按插入排序方式完全排序。

**代码说明**

2. **逻辑调整**：
   - 使用 `gap = gap / 3 + 1` 缩减间隔，比传统 `gap /= 2` 更接近希尔原始设计思路，能够在实际数据上提供更好的性能。

**时间复杂度**

- 最好情况（接近有序）：\( O(n) \)
- 最坏情况：\( O(n^{2}) \)（取决于 `gap` 的选择）
- 平均时间复杂度：\( O(n^{1.3 \sim 2}) \)

希尔排序在小型数组或接近有序的数据上表现较好，但其时间复杂度并不适合处理特别大的数据集。