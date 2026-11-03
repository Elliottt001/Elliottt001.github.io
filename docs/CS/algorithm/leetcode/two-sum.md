# 两数之和

[题目](https://leetcode.cn/problems/two-sum/)

给一个数组 `nums` 和一个 `target`，找两个数，加起来等于 target，返回它们的**下标**。

例如 `[2, 7, 11, 15]`，target = 9，返回 `[0, 1]`。题目保证恰好有一组解，同一个元素不能用两次。

## 先想暴力

固定一个数，再找后面的数：两层循环。

```cpp
for (int i = 0; i < nums.size(); ++i) {
    for (int j = i + 1; j < nums.size(); ++j) {
        if (nums[i] + nums[j] == target) {
            return {i, j};
        }
    }
}
```

`j` 从 `i + 1` 开始，避免自己加自己，也不用把同一对重复比较。

时间 $O(n^2)$，额外空间 $O(1)$。

## 空间换时间

看到一个数 x，要找的另一个数其实已经确定：`target - x`。

不必每次从头找，用哈希表记住**前面出现过的数 → 它的下标**。

```cpp
#include <unordered_map>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> seen;
        for (int i = 0; i < static_cast<int>(nums.size()); ++i) {
            auto it = seen.find(target - nums[i]);
            if (it != seen.end()) {
                return {it->second, i};
            }
            seen[nums[i]] = i;
        }
        return {};
    }
};
```

例如 target = 9：

- 看到 2，要找 7，表里没有，先存 `2 → 0`。
- 看到 7，要找 2，表里有，得到 `[0, 1]`。

注意**先查，再存当前元素**。否则 `[3, 3]`、target = 6 时，第一个 3 就可能匹配到自己。

哈希表查询平均 $O(1)$，总时间平均 $O(n)$，额外空间 $O(n)$。
