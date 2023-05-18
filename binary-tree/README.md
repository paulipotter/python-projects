# binary tree coding-questions

Note: Any time you have a binary tree problem, it's a good idea to see if there's a recursive solution; all you need to do is to be able to define what you should at a random node and then ask if that holds true for all nodes.

I practice different coding questions then post them here for posterity!

|Graphs (non binary tree)|Binary Tree|
|---|---|
|✅ non-linear data-structure|✅ non-linear data-structure|
|vertices (or nodes) connected by edges|vertices (or nodes) connected by edges|
|network-like|useful to represent a relationship between the nodes with hierarchy|
|no root node|exactly one root node|
|more complex|less complex|
|nodes can be connected to any number of vertices|only one unique conection between nodes<br>no standalone nodes|
|edges (aka lines) can be bidirected, directed and weighted|lines are top-down and not|

```
                graph                       binary tree
                ---  a                           a
                |   / \                         / \
                | b --- c                      /   \
                |/ \ / /                      b     \
                d   e-f                      / \     c
                                            d   e   / 
                                                   f 
```

## Binary tree

- also a non linear data-structure
- useful to represent a relationship between the nodes with hierarchy
- nodes must be connected (no standalone nodes)
- must not have loops

```
     a
    / \
   /   \
  b     \
 / \     c
d   e   / 
       f   
```

### Parts of the 🌳

- Root: node at the very top
- Left sub-tree: subset at the left of the root
- Right sub-tree: subset at the right of the root
- Leaf node 🍃: null left sub-tree `AND` right sub-tree

### Depth First Search

Visit nodes from the leaves 🍃

#### Time Complexity

- All 4 traversals require O(n) - visit every node exactly once
- **DFS**: O(h) where h is the max height of the binary tree
-

##### Pre-order

 root →  left sub-tree → right sub-tree
`a → b → d → e → c → f`
or
`a → b → d → null → null → e → null → null → c → f → null`

##### In-order

left sub-tree → root → right sub-tree
`d → b → e → a → f → c`
or
`d`

##### Post-order

left sub-tree → right sub-tree → root
`d → e → b → f → c → a`
or
`null → null → d → null → null → e → b → null → null → f → null → c → a`
