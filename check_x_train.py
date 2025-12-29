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
            sample_np = sample.numpy()  
            sample_count += 1  
            total_sum += np.mean(sample_np)  
            total_sq_sum += np.mean(np.square(sample_np))  
            min_val = min(min_val, np.min(sample_np))  
            max_val = max(max_val, np.max(sample_np))  
        if sample_count 
            overall_mean = total_sum / sample_count  
            overall_var = (total_sq_sum / sample_count) - (overall_mean ** 2)  
            overall_std = np.sqrt(overall_var)  
            print(f\"?100????????:\")  
            print(f\"  ??: {overall_mean}\")  
            print(f\"  ???: {overall_std}\")  
            print(f\"  ???: {min_val}\") 
            print(f\"  ???: {max_val}\")  
        print(\"\\n5. ???????:\")  
        print(\"-\" * 30)  
        batched_x_train = x_train.batch(32)  
        print(f\"?????32??????????: {batched_x_train.element_spec}\")  
        for batch in batched_x_train.take(1):  
            print(f\"????: {batch.shape}\") 
            break  
        print(\"\\n6. ???????:\")  
        print(\"-\" * 30)  
        print(f\"?????? (??): {original_data.size * original_data.dtype.itemsize}\")  
        print(f\"?????? (MB): {original_data.size * original_data.dtype.itemsize / (1024*1024):.2f}\")  
        print(\"\\n\" + \"=\"*60)  
        print(\"????\")  
        print(\"=\"*60)  
  
if __name__ == \"__main__\": 
    print(\"?????????? HDF5 ????\")  
    print(\"???????????????\") 
