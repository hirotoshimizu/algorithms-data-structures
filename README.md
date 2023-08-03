# Algorithms and Data Structures

## Data Structures

### Array

Static Arrays

最初や、真ん中の値を削除する際は、削除した以降の値をシフトする必要があるので、O(n) になる。

| Operation | Time Complexity | Note |
| :-: | :-: | :-: |
| Access | O(1) | |
| Insert | O(n) | arrayの最後にinsertする場合は O(1) |
| Remove | O(n) | arrayの最後をremoveする場合は O(1)|

Dynamic Arrays
String
Insert をする際、次の空きスペースを探す。
しかし、スペースが空いていない場合、元のサイズの2倍の新しい配列に値をコピーして配列の容量不足を解消する。この処理は O(n) になる。
その際メモリ内のアドレスには新しいアドレスが割り当てられる。

| Operation | Time Complexity | Note |
| :-: | :-: | :-: |
| Access | O(1) | |
| Insert | O(n) | arrayの最後にinsertする場合は O(1) |
| Remove | O(n) | arrayの最後をremoveする場合は O(1)|


Access が O(1)な理由
Address of ith Index = Base address + offset = Address of 0th Index + i × (size of one element)

### String

| Operation | Time Complexity | Note |
| :-: | :-: | :-: |
| Access | O(1) | |
| Search | O(n) | |
| Insert | O(n) | |
| Remove | O(n) | |

### Linked List
Linked List は連続した nodes を表現するデータ構造。
Node には value と next ポインタが含まれる。
next ポインタは次の Node のレファレンス。

Arrayとは異なり、memoryに連続して配置されていない。

最後の Node は next ポインタが NULL なので、Linked List の最後と判断出来る。
- Singly-linked list それぞれの node は次の node にポインタを向けている。
- Doubly-linked list それぞれの node は previous node と next node にポインタを持っている。

| Operation | Time Complexity | Note |
| :-: | :-: | :-: |
| Access | O(n) | |
| Search | O(n) | |
| Insert | O(1) | 目的の位置にノードへの参照があると仮定した場合 |
| Remove | O(1) | 目的の位置にノードへの参照があると仮定した場合 |


### Stack
Stackは、要素を追加する push と 一番最後に追加された要素を削除する pop というオペレーションから成り立つ、要素のコレクション。
Stackは、LIFO(last-in first-out)の順で要素の順序となる。

| Operation | Time Complexity | Note |
| :-: | :-: | :-: |
| Access | O(n) | |
| Search | O(n) | |
| Push | O(1) | |
| Pop | O(1) | |
| Peek/Top | O(1) | 一番上の要素のレファレンスを返す |

### Queue
Queueは、要素を追加する Enqueue と 最初に追加された要素から削除する Dequeue から成り立つ、要素のコレクション。
Queueは、FIFO(first-in first-out)の順で要素の順序となる。

Queueの実装には Array, Stack, Linked List が使われる。


| Operation | Time Complexity |
| :-: | :-: |
| Access | O(n) |
| Search | O(n) |
| Enqueue | O(1) |
| Dequeue | O(1) |

### Tree

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
また、Binary Search Tree では値の重複はないとされるのが一般的。
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


### Heap / Priority Queue
Tree ベースの data structure。
max, min value を取得するときに使う。

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



### Hashing

Hashmap は内部で配列を使用して実装されるのが最も一般的。

```Python
hashmap["fish"] = "Tuna"
```

hash function によって keyである、 fish を integer に変換し、
Hash map にセットする。

Hash map から値を取得する時も、 hash function を使い、fish を integer に変換し、
Hash map から該当の integer を探し、値を取得する。

<table>
  <tr>
    <th colspan="2">HashMap</th>
  </tr>
  <tr>
    <td>Index</td>
    <td>key, Value</td>
  </tr>
  <tr>
    <td>0</td>
    <td></td>
  </tr>
  <tr>
    <td>1</td>
    <td>{fish: Tune}</td>
  </tr>
</table>

Hash collision が発生した場合、
- [Chaining](https://en.wikipedia.org/wiki/Hash_table#Separate_chaining)
    Linked listを使うことにより、複数の key-value ペアを同じ index 内に保存できる。
- [Open Addressing](https://en.wikipedia.org/wiki/Open_addressing)
    オープン アドレッシングの背後にある考え方は、1 つのインデックスに複数のキーと値のペアを格納しないように、次に利用可能なスロットを見つけることです。 この手法は、衝突の数が少ない場合、チェーン化と比較してより効率的です。 ただし、ここでの制限は、テーブル内のエントリの総数が配列のサイズによって制限されることです。


| Operation | Time Complexity |
| :-: | :-: |
| Insert | O(1) |
| Remove | O(1) |
| Search | O(1) |

### Graph
Tree はグラフの一種である。しかし、全てのグラフが Tree ではない。
Tree はサイクルのない connected graphである。

グラフは nodes の集合で、それらの間には edges がある。

グラフは directed か undirected のどちらかのグラフになる。
directed edges は一方通行の道のようなもので、
undirected edges は双方向道路のようなもの。

E <= V^2


| Operation | Time Complexity |
| :-: | :-: |
| DFS | O(&#124;V&#124; + &#124;E&#124;) |
| BFS | O(&#124;V&#124; + &#124;E&#124;) |
| Topological Sort | O(&#124;V&#124; + &#124;E&#124;) |
| Dijkstra's Algorithm | O(&#124;V&#124;^2) |

## Algorithms

### Sorting

### Graph Algorithms

#### Depth-First Search(DFS)

深さを優先した探索。

探索の仕方には3つある。
- Inorder
- Preorder
- Postorder

| Operation | Time Complexity |
| :-: | :-: |
| Traversal | O(n) |

#### Breadth-First-Search(BFS)

Queueを使い、階層ごとに横断する。

| Operation | Time Complexity |
| :-: | :-: |
| Traversal | O(n) |