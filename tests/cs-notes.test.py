"""Run with python3 tests/cs-notes.test.py; requires clang and clang++."""
import re
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def blocks(path, language):
    text = (ROOT / 'docs' / path).read_text()
    return re.findall(rf'^```{language}\n(.*?)^```\s*$', text, re.M | re.S)


def run(directory, name, code, compiler, standard):
    source = directory / name
    binary = directory / (name + '.out')
    source.write_text(code)
    subprocess.run([compiler, standard, '-Wall', '-Wextra', '-Werror',
                    '-fsanitize=address', str(source), '-o', str(binary)], check=True)
    subprocess.run([str(binary)], check=True)


with tempfile.TemporaryDirectory(prefix='cs-note-examples-') as temporary:
    directory = Path(temporary)
    two_sum = next(b for b in blocks('CS/algorithm/leetcode/two-sum.md', 'cpp')
                   if 'class Solution' in b)
    run(directory, 'two-sum.cpp', two_sum + r'''
#include <cassert>
int main() {
    Solution solution;
    std::vector<std::vector<int>> inputs = {
        {2, 7, 11, 15}, {3, 3}, {-3, 4, 3, 90}, {0, 4, 3, 0}
    };
    int targets[] = {9, 6, 0, 0};
    for (int k = 0; k < 4; ++k) {
        auto answer = solution.twoSum(inputs[k], targets[k]);
        assert(answer.size() == 2);
        assert(answer[0] != answer[1]);
        assert(inputs[k][answer[0]] + inputs[k][answer[1]] == targets[k]);
    }
}
''', 'clang++', '-std=c++17')

    tree_blocks = blocks('CS/algorithm/fds/chap4.md', 'c')
    tree = '\n'.join(b for b in tree_blocks if b.startswith('tree_ptr '))
    assert all(name in tree for name in ['findMax(', 'findMin(', 'deleteNode('])
    run(directory, 'bst.c', r'''
#include <stdlib.h>
#include <assert.h>
typedef struct TreeNode {
    int Element;
    struct TreeNode *Left, *Right;
} TreeNode, *tree_ptr;
''' + tree + r'''
static tree_ptr insert(tree_ptr tree, int value) {
    if (!tree) {
        tree = malloc(sizeof *tree);
        assert(tree);
        *tree = (TreeNode){value, NULL, NULL};
    } else if (value < tree->Element) tree->Left = insert(tree->Left, value);
    else if (value > tree->Element) tree->Right = insert(tree->Right, value);
    return tree;
}
static int count(tree_ptr tree) {
    return tree ? 1 + count(tree->Left) + count(tree->Right) : 0;
}
static void check(tree_ptr tree, int low, int high) {
    if (!tree) return;
    assert(low < tree->Element && tree->Element < high);
    check(tree->Left, low, tree->Element);
    check(tree->Right, tree->Element, high);
}
int main(void) {
    assert(findMin(NULL) == NULL && findMax(NULL) == NULL);
    assert(deleteNode(1, NULL) == NULL);
    tree_ptr root = NULL;
    int values[] = {5, 3, 8, 2, 4, 7, 9, 6};
    for (int i = 0; i < 8; ++i) root = insert(root, values[i]);
    assert(findMin(root)->Element == 2 && findMax(root)->Element == 9);
    root = deleteNode(100, root);  /* absent */
    assert(count(root) == 8);
    int removed[] = {2, 7, 5, 3, 4, 6, 8, 9};  /* leaf, one child, two children */
    for (int i = 0; i < 8; ++i) {
        root = deleteNode(removed[i], root);
        assert(count(root) == 7 - i);
        check(root, -1000, 1000);
    }
    assert(root == NULL);
}
''', 'clang', '-std=c11')

print('Two Sum and BST note examples passed with AddressSanitizer.')
