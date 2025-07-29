'''
This code builds approximate k-nearest neighbor (kNN) graphs using HNSW (Hierarchical Navigable Small World) for a given set of node embeddings, and combines them with an existing directed edge set. 
The purpose is to augment or compare graph connectivity using embedding-based similarity rather than only relying on the original graph structure.

'''
import torch
import hnswlib
import numpy as np
from tqdm import tqdm

# Load embeddings and edge set
embeddings = torch.load("initial_embeddings.pt").cpu().numpy().astype('float32')
n, dim = embeddings.shape
print(f"Loaded embeddings: n = {n}, dim = {dim}")

directed_edge_index = torch.load("directed_edge_index_dedup.pt")
edge_set = set((int(s), int(d)) for s, d in zip(directed_edge_index[0], directed_edge_index[1]))

# Build HNSW index once
index = hnswlib.Index(space='l2', dim=dim)
index.init_index(max_elements=n, ef_construction=200, M=16)
index.add_items(embeddings)
index.set_ef(50)
print("HNSW index built.")

# Query with max k only once
max_k = 40
all_labels, _ = index.knn_query(embeddings, k=max_k)

# For each k, build and save edge sets
k_list = [1, 2, 5, 10, 20, 40]

for k in k_list:
    labels_k = torch.tensor(all_labels[:, :k])
    hnsw_edges_k = set(
        (i, int(j))
        for i, neighbors in enumerate(labels_k)
        for j in neighbors[1:]  # skip self-loop
        if i != int(j)
    )
    union_edges_k = edge_set.union(hnsw_edges_k)

    # Save
    torch.save(torch.tensor(list(hnsw_edges_k), dtype=torch.long).T, f"edge_hnsw_{k}.pt")
    torch.save(torch.tensor(list(union_edges_k), dtype=torch.long).T, f"edge_union_{k}.pt")

    # Print stats
    print(f"k={k}: HNSW-only edges = {len(hnsw_edges_k)}, Union edges = {len(union_edges_k)}")
