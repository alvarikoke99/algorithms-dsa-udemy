# 🧠 Algorithms & Data Structures

> Python exercises based on Daniel Blanco's Udemy course — *Algoritmos y Estructuras de Datos para Entrevistas*

---

## 📚 What's Inside

A curated collection of **DSA problem stubs** ready for you to solve, organized by topic. Each folder contains:
- 📝 A **problem definition** with description and examples
- 🧪 A **pytest test file** to validate your solution

---

## 🗂️ Structure

| # | Category | Topics |
|---|----------|--------|
| 03 | [Arrays, Strings & Hash Tables](./03-ArraysStringsHashTables/) | Uniqueness, Two Sum, Anagrams, Matrix |
| 04 | [Linked Lists](./04-LinkedLists/) | Remove dups, Merge, Nth node, Add numbers |
| 05 | [Stacks & Queues](./05-StacksQueues/) | Queue with stacks, Valid parenthesis, Sort stack, Stack min |
| 06 | [Trees](./06-Trees/) | Invert, List of depths, Max depth, Validate BST, Subtree, LCA |
| 07 | [Graphs](./07-Graphs/) | BFS/DFS, Route between nodes, Clone graph, Build order |
| 08 | [Heaps](./08-Heaps/) | Min heap, Kth largest, Top K frequent, Relative ranks |
| 09 | [Tries](./09-Tries/) | Trie implementation, Title suggestions, Word search |
| 10 | [Sorting](./10-Sorting/) | Bubble, Merge, Quick, Selection sort |
| 11 | [Searching](./11-Searching/) | Binary search (recursive & iterative) |
| 12 | [Dynamic Programming](./12-DynamicProgramming/) | Robot in grid, Set subsets, Parenthesis, Max subarray |
| 13 | [Bit Manipulation](./13-BitManipulation/) | One bits, Reverse int, Number conversion, Sum integers |
| 14 | [Extra Problems](./14-ExtraProblems/) | Merge K lists, Word break, Reverse K-group, House robber |

---

## 🚀 Getting Started

**Prerequisites:** Python 3.8+

```bash
# Install pytest
pip install pytest

# Run tests for a specific problem (will fail until you implement — that's the point!)
cd 03-ArraysStringsHashTables/_01_is_unique
pytest test_is_unique.py

# Run all tests across the repo
pytest
```

---

## 💡 How to Use

1. Navigate to any problem folder
2. Open the problem file (e.g., `is_unique.py`) — read the docstring for the description and examples
3. Implement the method(s) — replace `raise NotImplementedError("Not implemented yet")`
4. Run the tests to verify your solution

```python
# Before
def is_unique(self, s: str) -> bool:
    raise NotImplementedError("Not implemented yet")

# After — your implementation here!
def is_unique(self, s: str) -> bool:
    return len(set(s)) == len(s)
```
---

*GG, and may your time complexity always be O(1). 🎮*
