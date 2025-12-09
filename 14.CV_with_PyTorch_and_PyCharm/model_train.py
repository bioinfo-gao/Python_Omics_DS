# https://www.bilibili.com/video/BV1e34y1M7wR?spm_id_from=333.788.player.switch&vd_source=9a4bc8c6c4b3f65118a7338473c15077&p=48
#from keras.src.ops import nn
import copy # # from datetime import time
import time

from model import * # import model defined
import pandas as pd
from torchvision.datasets import FashionMNIST
from torchvision import transforms
import matplotlib.pyplot as plt
import numpy as np
import torch.utils.data as data
from model import LeNet5
import torch.optim as optim
import torch.nn as nn
import torch

def train_val_data_process():
    train_data = FashionMNIST(root='./data', train=True,
                          transform=transforms.Compose([transforms.Resize(size=224), transforms.ToTensor()]),
                          download=True  )
    #train_data, val_data = data.random_split(train_data, [60000, 10000])
    train_data, val_data = data.random_split(train_data,[round(0.8*len(train_data)), len(train_data)-round(0.8*len(train_data))]) # round(0.2*len(train_data))

    train_dataloader = data.DataLoader(train_data,
                                       batch_size=128,
                                       shuffle=True,
                                       num_workers=8) #  help(data.DataLoader)# ALT+ Shit + E , 0 means in the main process
    val_dataloader = data.DataLoader(val_data,
                                     batch_size=128,
                                     shuffle=True,
                                     num_workers=8) #
    return train_dataloader, val_dataloader

def train_model_process(model, train_dataloader, val_dataloader, num_epochs):
    device    = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
    criterion = nn.CrossEntropyLoss()

    model= model.to(device)

    best_model_wts = copy.deepcopy(model.state_dict())
    best_acc = 0.0 #accuracy

    train_losses_all = []
    val_losses_all   = []
    train_acc_all    = []
    val_acc_all      = []

    since = time.time()

    for epoch in range(num_epochs):
        print('Epoch {}/{}'.format(epoch, num_epochs )) # num_epochs - 1))
        print('-' * 10) # print line of "---"
        train_losses   = 0.0
        train_corrects = 0.0
        val_losses     = 0.0
        val_corrects   = 0.0
        # training batch number
        train_num = 0
        val_num   = 0
        # train
        for step, (b_x, b_y) in enumerate(train_dataloader):
            b_x = b_x.to(device) # data and model has to being put into same device line 38
            b_y = b_y.to(device)

            model.train()
            b_x
            output = model(b_x)

            pre_label = torch.argmax(output, dim=1)
            loss = criterion(output, b_y)

            optimizer.zero_grad() # has to clear, avoid left from earlier batch
            loss.backward()
            optimizer.step()

            train_losses +=  loss.item() * b_x.size(0) ## ============= (0)
            train_corrects += (pre_label == b_y).sum().item() # torch.sum() also works to sum
            train_num += b_x.size(0)

        # validate
        for step, (b_x, b_y) in enumerate(val_dataloader):
            b_x = b_x.to(device) # data and model has to being put into same device line 38
            b_y = b_y.to(device)

            model.eval()
            output = model(b_x)

            pre_label = torch.argmax(output, dim=1)
            loss = criterion(output, b_y)

            # validation only check the loss ===== no following training
            val_losses +=  loss.item() * b_x.size(0)
            val_corrects += (pre_label == b_y).sum().item() # torch.sum() also works to sum
            val_num += b_x.size(0)

        train_losses_all.append( train_losses/train_num)
        train_acc_all.append( train_corrects.item()/train_num) # double()

        val_losses_all.append( val_losses/val_num)
        val_acc_all.append( val_corrects.item() /val_num)

        print('{} train loss: {:.4f} training acc: {:.4f}'.format(epoch, train_losses_all[-1], train_acc_all[-1]))
        print('{} eval loss: {:.4f} training acc: {:.4f}'.format(epoch, val_losses_all[-1], val_acc_all[-1]))

        if val_acc_all[-1] > best_acc:
            best_acc = val_acc_all[-1]
            #wts means "want to show"  essentially the "model parameters" of the current best model
            best_model_wts = copy.deepcopy(model.state_dict()) # automatic, no copy needed

        time_use = time.time() - since
        print('Best val acc: {:.4f}'.format(best_acc))
        print('Best model: {:.4f}'.format(best_model_wts))
        print('Elapsed time: {:.4f} seconds'.format(time_use))
        print('-' * 10)

        torch.save(best_model_wts, 'best_model_weights.pth') # pth ending : specially  for model weight

        train_process = pd.DataFrame(data={"epoch": range(num_epochs),
                                           "train_loss_all": train_losses_all,
                                           "val_loss_all": val_losses_all,
                                           "train_acc_all": train_acc_all,
                                           "val_acc_all": val_acc_all   }        )
        return train_process

def matplot_acc_loss(train_process):
    plt.figure(figsize=(12,4))
    plt.subplot(1, 2 ,1) # 16 plot in each line ,total 64

    plt.plot(train_process['epoch'], train_process['train_loss_all'], 'ro-', label='train loss') # 'ro-' table label
    plt.plot(train_process['epoch'], train_process['val_loss_all'], 'bs-', label='val loss') # 'ro-' table label
    plt.legend(loc='best')

    #plt.title(class_labels[batch_y[ii]], size=10)
    plt.xlabel('epoch')
    plt.ylabel('loss')

    plt.plot(train_process['epoch'], train_process['train_acc_all'], 'ro-', label='train acc') # 'ro-' table label
    plt.plot(train_process['epoch'], train_process['val_acc_all'], 'bs-', label='val acc') # 'ro-' table label
    plt.legend(loc='best')

    #plt.title(class_labels[batch_y[ii]], size=10)
    plt.xlabel('epoch')
    plt.ylabel('acc')
    plt.show()

if __name__ == '__main__':
    device = torch.device("cuda:0" if  torch.cuda.is_available()  else "cpu")
    print(device)                        #print(torch.rand(3,3).cuda())
    LeNet = LeNet5()
    train_dataloader, val_dataloader = train_val_data_process()
    train_process = train_model_process(LeNet, train_dataloader, val_dataloader, 20)
    matplot_acc_loss(train_process)