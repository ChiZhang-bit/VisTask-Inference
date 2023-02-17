## NLTK Tree 使用文档

```python
from nltk import tree as Tree
Tree(S (NP I) (VP (V saw) (NP him)))

# 直接定位的方法，如下所示：
vp = Tree('VP', [Tree('V', ['saw']),
        		 Tree('NP', ['him'])])
s = Tree('S', [Tree('NP', ['I']), vp])
s = Tree(S (NP I) (VP (V saw) (NP him)))

>>> s[1,1]
(NP, him)

>>> len(s)
2 具有孩子节点的个数

Tree.label()
# 返回该树的第一个节点

Tree.set_label()
# 设置该树的第一个节点

Tree.leaves()
# 返回该树的全部叶子节点

Tree.flatten()
# 返回该树的标签，之后是该树的所有叶子节点

Tree.height()
# 返回该树的高度
"""
			The height of a tree
            containing no children is 1; the height of a tree
            containing only leaves is 2; and the height of any other
            tree is one plus the maximum of its children's
            heights.
"""

Tree.subtrees()
# 返回所有的subtrees：

Tree.pos()
# 返回一个pos序列， 从树中提取所有的子节点与他的标记
"""
>>> t = Tree.fromstring("(S (NP (D the) (N dog)) (VP (V chased) (NP (D the) (N cat))))")            
>>> t.pos()
[('the', 'D'), ('dog', 'N'), ('chased', 'V'), ('the', 'D'), ('cat', 'N')]
"""
```

