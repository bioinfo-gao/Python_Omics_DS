import h5py  
import numpy as np  
  
def explore_h5_dataset(file_path):
    \"\"\"Function to explore the structure of an HDF5 dataset\"\"\"
    with h5py.File(file_path, 'r') as f:
        print(\"File structure:\")
        print(\"=\"*50)
        print(\"Keys in the dataset:\", list(f.keys()))

        # Recursively explore the structure
        def explore_group(group, indent=0):
            for key in group.keys():
                item = group[key]
                if isinstance(item, h5py.Dataset):
                    print(\"  \" * indent + f\"Dataset: {key}\")
                    print(\"  \" * indent + f\"  Shape: {item.shape}\")
                    print(\"  \" * indent + f\"  Data type: {item.dtype}\")
                    print(\"  \" * indent + f\"  Size: {item.size}\")
                elif isinstance(item, h5py.Group):
                    print(\"  \" * indent + f\"Group: {key}\")
                    explore_group(item, indent + 1)

        explore_group(f)

        print(\"\\nDetailed information about each dataset:\")
        print(\"=\"*50)

        # Print more detailed information for each dataset
        for key in f.keys():
            dataset = f[key]
            if isinstance(dataset, h5py.Dataset):
                print(f\"\\nDataset name: {key}\")
                print(f\"Shape: {dataset.shape}\")
                print(f\"Data type: {dataset.dtype}\")
                print(f\"Chunks: {dataset.chunks}\")
                print(f\"Compression: {dataset.compression}\")

                # Show a sample of the data (first few elements)
                print(\"Sample data (first 5 rows if available):\")
                if len(dataset.shape) == 1:
                    print(dataset[:5] if dataset.shape[0] > 5 else dataset[:])
                elif len(dataset.shape) == 2:
                    rows_to_show = min(5, dataset.shape[0])
                    cols_to_show = min(5, dataset.shape[1])
                    print(dataset[:rows_to_show, :cols_to_show])
                elif len(dataset.shape) == 3:
                    # For image data (height, width, channels) or similar
                    rows_to_show = min(2, dataset.shape[0])
                    height_to_show = min(5, dataset.shape[1])
                    width_to_show = min(5, dataset.shape[2])
                    print(f\"Showing first {rows_to_show} samples:\")
                    for i in range(rows_to_show):
                        print(f\"Sample {i} shape {dataset[i].shape}:\")
                        print(dataset[i, :height_to_show, :width_to_show])
                else:
                    # For higher dimensional data, just show shape info
                    print(f\"Multi-dimensional data with shape {dataset.shape}\")
                    print(\"First element slice:\", dataset.flat[:5] if dataset.size > 0 else \"Empty\")

# Usage example:
# explore_h5_dataset('datasets/train_signs.h5')

if __name__ == \"__main__\":
    # This is where you would call the function with your actual file
    print(\"To use this function, call: explore_h5_dataset('datasets/train_signs.h5')\")
