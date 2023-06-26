# Algorithms and Data Structures

### Data Structures

#### Linked List
Linked List は連続した nodes を表現するデータ構造
Node には value と next ポインタが含まれる。
next ポインタは次の Node のレファレンス。
最後の Node は next ポインタが NULL なので、Linked List の最後と判断出来る。
- Singly-linked list それぞれの node は次の node にポインタを向けている。
- Doubly-linked list それぞれの node は previous node と next node にポインタを持っている。

| Operation | Time Complexity |
| :-: | :-: |
| Access | O(N) |
| Search | O(N) |
| Insert / Remove from beginning | O(1) |
| Insert / Remove from middle | O(N) |
| Insert / Remove from end | O(n) |

#### Stack
Stackは、要素を追加する push と 一番最後に追加された要素を削除する pop というオペレーションから成り立つ、要素のコレクション。
Stackは、LIFO(last-in first-out)の順で要素の順序となる。

| Operation | Time Complexity |
| :-: | :-: |
| Access | O(N) |
| Search | O(N) |
| Insert | O(1) |
| Remove | O(1) |

#### Queue
Queueは、要素を追加する Enqueue と 最初に追加された要素から削除する Dequeue から成り立つ、要素のコレクション。
Queueは、FIFO(first-in first-out)の順で要素の順序となる。


| Operation | Time Complexity |
| :-: | :-: |
| Access | O(N) |
| Search | O(N) |
| Insert | O(1) |
| Remove | O(1) |

#### Tree

Tree は nodes を用いたデータ構造。
- Treeには root node が存在する
- Root node には 0 もしくは複数の子がいる。
- 子 node は 0 もしくは複数の子がいる。

Tree は cycle を含まない。
Node は特定の順序がある場合とない場合がある。また Value はどんなタイプの物にでもなりえる。

#### Binary Tree

Binary Tree は Tree データ構造で、それぞれの Node が left child と right child の最大で2つ持つ。
- Full Binary Trees
    それぞれの node が 0もしくは2つの子を持つ。1つの子しかないというのは存在しない。
- Perfect Binary Tree
    すべての内部ノードが2つの子を持ち、すべての leave nodes が同じレベルになる。
- Complete Tree
    last レベル以外では node で満たされている。 last レベルでは左から順に node が追加される。

#### Binary Search Tree
Binary Search Tree は Binary Tree で、node が特定の並び順になっている。
left descendents <= n < all right descendents
全ての node n で上記のようになる必要がある。

Balanced binary tree
| Operation | Time Complexity |
| :-: | :-: |
| Access | O(log(n)) |
| Search | O(log(n)) |
| Insert | O(log(n)) |
| Remove | O(log(n)) |

Skewed binary tree(worst case)
| Operation | Time Complexity |
| :-: | :-: |
| Access | O(n) |
| Search | O(n) |
| Insert | O(n) |
| Remove | O(n) |

#### Heap
Tree ベースの data structure。
部分的にのデータがソートされている。
maximum, minimum value を取得するときに使う。

Max Heap, Min Heap

#### Hashing

#### Graph

### Algorithms

