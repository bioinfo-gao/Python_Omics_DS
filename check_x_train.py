import tensorflow as tf  
import h5py  
import numpy as np  
  
def check_x_train_comprehensive(h5_file_path='datasets/train_signs.h5'): 
    \"\"\"???? x_train ????????\"\"\"  
    print(\"=\"*60)  
    print(\"???? x_train ???\")  
    print(\"=\"*60)  
  
    with h5py.File(h5_file_path, 'r') as train_dataset: 
        x_train = tf.data.Dataset.from_tensor_slices(train_dataset['train_set_x'])  
        print(\"1. ????:\")  
        print(\"-\" * 30)  
        print(f\"?????: {type(x_train)}\")  
        original_data = train_dataset['train_set_x']  
        print(f\"??????: {original_data.shape}\") 
        print(f\"??????: {original_data.dtype}\")  
        print(\"\\n2. TensorFlow ?????:\")  
        print(\"-\" * 30)  
        element_spec = x_train.element_spec  
        print(f\"????: {element_spec}\")  
        print(f\"????: {element_spec.shape}\") 
        print(f\"??????: {element_spec.dtype}\")  
        dataset_length = len(train_dataset['train_set_x'])  
        print(f\"?????: {dataset_length}\")  
        print(\"\\n3. ??????:\")  
        print(\"-\" * 30)  
        for i, sample in enumerate(x_train.take(3)): 
            print(f\"?? {i+1} ??: {sample.shape}\")  
            print(f\"?? {i+1} ????: {sample.dtype}\")  
            print(f\"?? {i+1} ???: {tf.reduce_min(sample).numpy()} - {tf.reduce_max(sample).numpy()}\")  
            print(f\"?? {i+1} ??: {tf.reduce_mean(sample).numpy()}\")  
            print()  
        print(\"4. ??????:\") 
        print(\"-\" * 30)  
        sample_count = 0  
        total_sum = 0  
        total_sq_sum = 0  
        min_val = float('inf')  
        max_val = float('-inf')  
        for i, sample in enumerate(x_train.take(100)): 
