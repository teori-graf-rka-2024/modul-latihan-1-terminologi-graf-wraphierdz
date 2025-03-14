[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/UuQ9jMmq)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=18604664&assignment_repo_type=AssignmentRepo)
# Latihan Teori Graf dengan NetworkX
Deadline : Senin, 17 Maret 23.59 WIB
## Deskripsi Soal

Dalam latihan ini, Anda diminta untuk mengimplementasikan beberapa fungsi terkait teori graf menggunakan pustaka `networkx`. Soal ini mencakup beberapa aspek penting, seperti:

1. **Membuat Graf**
2. **Degree Counting**
3. **Path Finding / Traversal**
4. **Shortest Path**
5. **Visualisasi Graf**

Anda harus mengimplementasikan fungsi-fungsi berikut:
### Untuk soal nomor 1 -- 5 buat di dalam file bernama `graph.py`
### 1. `create_graph(edges: list[tuple[int, int]]) -> nx.Graph`

- **Deskripsi**: Membuat graf tidak berarah berdasarkan daftar sisi yang diberikan.
- **Parameter**:
  - `edges` (list of tuple[int, int]): Daftar sisi yang menghubungkan dua simpul.
- **Output**:
  - `nx.Graph`: Objek graf dari `networkx`.

### 2. `get_degree(G: nx.Graph, node: int) -> int`

- **Deskripsi**: Menghitung derajat dari simpul tertentu.
- **Parameter**:
  - `G` (nx.Graph): Graf yang telah dibuat.
  - `node` (int): Simpul yang ingin dihitung derajatnya.
- **Output**:
  - `int`: Derajat dari simpul tersebut.

### 3. `dfs_traversal(G: nx.Graph, start: int) -> list[int]`

- **Deskripsi**: Melakukan pencarian secara Depth-First Search (DFS) mulai dari simpul tertentu.
- **Parameter**:
  - `G` (nx.Graph): Graf yang telah dibuat.
  - `start` (int): Simpul awal.
- **Output**:
  - `list[int]`: Urutan traversal berdasarkan DFS.

### 4. `bfs_traversal(G: nx.Graph, start: int) -> list[int]`

- **Deskripsi**: Melakukan pencarian secara Breadth-First Search (BFS) mulai dari simpul tertentu.
- **Parameter**:
  - `G` (nx.Graph): Graf yang telah dibuat.
  - `start` (int): Simpul awal.
- **Output**:
  - `list[int]`: Urutan traversal berdasarkan BFS.

### 5. `find_shortest_path(G: nx.Graph, source: int, target: int) -> list[int]`

- **Deskripsi**: Mencari jalur terpendek antara dua simpul dalam graf.
- **Parameter**:
  - `G` (nx.Graph): Graf yang telah dibuat.
  - `source` (int): Simpul awal.
  - `target` (int): Simpul tujuan.
- **Output**:
  - `list[int]`: Urutan simpul yang membentuk jalur terpendek dari `source` ke `target`.

### 6. `visualize_graph(G: nx.Graph) -> None`

- **Deskripsi**: Memvisualisasikan graf menggunakan `matplotlib`.
- **Parameter**:
  - `G` (nx.Graph): Graf yang telah dibuat.
- **Output**:
  - Tidak ada (hanya menampilkan visualisasi graf).
  - Export hasil visualisasi ke file .png kemudian tambahkan ke direktori project anda!
---

## 7. Buat sebuah file `tutorial.py`
File ini nantinya berisikan uji coba fungsi yang sudah anda buat sebelumnya!

Pastikan semua fungsi bekerja dengan benar dan sesuai spesifikasi!

---


