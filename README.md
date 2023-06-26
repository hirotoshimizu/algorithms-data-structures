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

#### Binary Tree

#### Binary Search Tree

#### Heap
Tree ベースの data structure。
部分的にのデータがソートされている。
maximum, minimum value を取得するときに使う。

Max Heap, Min Heap

#### Hashing

#### Graph

### Algorithms

