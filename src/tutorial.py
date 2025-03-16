import graph as g

# Edge = garis penyusun rasi sagittarius
garisRasi = [
    (1, 9), (2, 9), (9, 10), (10, 20),
    (20, 19), (19, 18), (19, 6), (18, 8),
    (18, 14), (14, 15), (15, 16), (16, 17),
    (6, 8), (6, 5), (8, 11), (8, 4),
    (5, 4), (5, 3), (5, 7), (11, 12), 
    (4, 11), (4, 3), (3, 13)
]

# Membuat graf rasi bintang sagittarius
sagittarius = g.create_graph(garisRasi)
print('# Membuat graf')
print(f'Sagittarius is now a {sagittarius},\nor {len(sagittarius.nodes)} stars and {len(garisRasi)} lines\n')

# Degree bintang keenam pada rasi sagittarius (Ascella)
print('# Degree counting')
print(f'Ascella terhubung dengan {g.get_degree(sagittarius, 6)} bintang')

# DFS dari bintang pertama (Rukbat)
print('# Depth-First Search')
print(f'Menelusuri semua bintang Sagittarius dari Rukbat (DFS):\n{g.dfs_traversal(sagittarius, 1)}')

# BFS dari posisi Nunki (bintang ke-18)
print('# Breadth-First Search')
print(f'Menelusuri semua bintang Sagittarius dari Nunki (BFS):\n{g.dfs_traversal(sagittarius, 1)}')

# Jarak terpendek dari bintang ke-13 menuju bintang kedua (Arkab Posterior)
print('# Shortest Path')
print('Jalur terpendek dari bintang ke-13 menuju Arkab Posterior:')
print(g.find_shortest_path(sagittarius, source=13, target=2))

# Visualisasi graf konstelasi Sagittarius
g.visualize_graph(sagittarius)
