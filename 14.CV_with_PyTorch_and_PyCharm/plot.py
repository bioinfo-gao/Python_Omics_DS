# https://www.bilibili.com/video/BV1e34y1M7wR?spm_id_from=333.788.player.switch&vd_source=9a4bc8c6c4b3f65118a7338473c15077&p=48
from torchvision.datasets import FashionMNIST
from torchvision import transforms
import matplotlib.pyplot as plt
import numpy as np
import torchshow # pip install torchshow
import torch.utils.data as data

train_data = FashionMNIST(root='./data', train=True,
                          transform=transforms.Compose([transforms.Resize(size=224), transforms.ToTensor()]),
                          download=True  )


train_loader = data.DataLoader(train_data, batch_size=64,
                               shuffle=True,
                               num_workers=0) #  help(data.DataLoader)# ALT+ Shit + E , 0 means in the main process

for step, (b_x, b_y) in enumerate(train_loader):
    print(b_x.size()) # torch.Size([64, 1, 224, 224])     print(b_x) #     torchshow.show(b_x) #=== doesn't work for unknown reason
    #print(b_y)
    if 0 <= step: # means read the 1st batch only for following demonstration
        break

# the following is for data demon , numpy for plot, training no need numpy
batch_x = b_x.squeeze().numpy() # remove 1st dim from 4 dim tensor and change to Numpy array
batch_y = b_y.numpy() # remove 1st dim from 4 dim tensor and change to Numpy array
class_labels = train_data.classes
# print(class_labels)

# show plot of a batch
plt.figure(figsize=(12,5))
for ii in np.arange(len(batch_y)):
    plt.subplot(4,16, ii + 1) # 16 plot in each line ,total 64
    plt.imshow(batch_x[ii, :, :], cmap='gray')
    plt.title(class_labels[batch_y[ii]], size=10)
    plt.axis('off')
    plt.subplots_adjust(wspace=0.05)
plt.show()