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

#### Heap / Priority Queue
Tree ベースの data structure。
maximum, minimum value を取得するときに使う。

Heapは、Heapプロパティを満たす特殊なツリーベースの構造データ構造です。
AがBの親ノードの場合、ノードAのキー(値)は、同じ順序付けがHeap全体にわたって、適用されてノードBのキーに対して順序付けされます。
ノードのキーは重複があっても良い。
Heapは、さらに「Max Heap」または「Min Heap」に分類できます。 


Heap構造を保つには下記に従う必要がある。
1. Structure property
    Min Heap は Complete binary tree(Last level以外ではノードで埋まっている。但し、Last level は左から埋める必要がある。)
2. Order property
    Max Heapでは、親ノードのキーは常に子ノードのキー以上であり、最も高いキーはルートノードにあります。
    Min Heapでは、親ノードのキーは子ノードのキー以下であり、最も低いキーはルート ノードにあります。

parent = i // 2
left child = i * 2
right child = i * 2 + 1

push で値を入れた時、親よりも小さい間、スワップする。

pop は、
1. leaf level の一番右の要素を root node に設定する。
2. 1.で設定した値が所定の位置になるまで、次の level の小さい値とスワップする。


| Operation | Time Complexity |
| :-: | :-: |
| Heapify | O(n) |
| push | O(log(n)) |
| pop | O(log(n)) |
| get min/max | O(1) |



#### Hashing

#### Graph

### Algorithms

