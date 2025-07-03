import torch
from ogb.nodeproppred import PygNodePropPredDataset

# Fix for PyTorch 2.6+
original_torch_load = torch.load
def patched_torch_load(*args, **kwargs):
    if 'weights_only' not in kwargs:
        kwargs['weights_only'] = False
    return original_torch_load(*args, **kwargs)
torch.load = patched_torch_load

def load_ogb_node_data(dataset_name='ogbn-arxiv'):
    """
    Load OGB node dataset and return processed data
    
    Args:
        dataset_name: OGB dataset name (e.g., 'ogbn-arxiv', 'ogbn-products')
    
    Returns:
        dataset: Original dataset object
        data: Graph data object
        num_nodes: Number of nodes
        train_mask: Boolean mask for training nodes
        val_mask: Boolean mask for validation nodes  
        test_mask: Boolean mask for test nodes
        x0: Initial node features
    """
    # Load dataset
    dataset = PygNodePropPredDataset(name=dataset_name)
    data = dataset[0]
    split_idx = dataset.get_idx_split()
    
    num_nodes = data.num_nodes
    
    # Create boolean masks from indices
    train_mask = torch.zeros(num_nodes, dtype=torch.bool)
    val_mask = torch.zeros(num_nodes, dtype=torch.bool)
    test_mask = torch.zeros(num_nodes, dtype=torch.bool)
    
    train_mask[split_idx['train']] = True
    val_mask[split_idx['valid']] = True
    test_mask[split_idx['test']] = True
    
    x0 = data.x  # Initial node features
    
    return dataset, data, num_nodes, train_mask, val_mask, test_mask, x0

# Example usage
if __name__ == "__main__":
    dataset, data, num_nodes, train_mask, val_mask, test_mask, x0 = load_ogb_node_data('ogbn-arxiv')
    
    print(f"Dataset: {dataset}")
    print(f"Data x shape: {data.x.shape}")
    print(f"Data y shape: {dataset.y.shape}")
    print(f"Num nodes: {num_nodes}")
    print(f"Train nodes: {train_mask.sum().item()}")
    print(f"Val nodes: {val_mask.sum().item()}")  
    print(f"Test nodes: {test_mask.sum().item()}")
    print(f"Feature shape: {x0.shape}")
