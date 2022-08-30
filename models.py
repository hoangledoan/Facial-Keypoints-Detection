## TODO: define the convolutional neural network architecture

import torch
import torch.nn as nn
import torch.nn.functional as F
# can use the below import should you choose to initialize the weights of your Net
import torch.nn.init as I


class Net(nn.Module):

    def __init__(self):
        super(Net, self).__init__()
        
        ## TODO: Define all the layers of this CNN, the only requirements are:
        ## 1. This network takes in a square (same width and height), grayscale image as input
        ## 2. It ends with a linear layer that represents the keypoints
        ## it's suggested that you make this last layer output 136 values, 2 for each of the 68 keypoint (x, y) pairs
        
        # As an example, you've been given a convolutional layer, which you may (but don't have to) change:
        # 1 input image channel (grayscale), 32 output channels/feature maps, 5x5 square convolution kernel
        
        # 1. CNN layer (5x5 kernel)
        self.conv1 = nn.Conv2d(1, 32, 5)
        # maxpool layer with kernel_size = 2 and stride = 2
        self.pool1 = nn.MaxPool2d(2, 2)
        # input image has the size [1, 224, 224] so W = 224, F = 5, S = 1
        # The output size = (W-F)/S +1 = 220
        # After one pool layer it would havethe dimension [32,110,110]
        # so the output's dimension is [32,110,110]
        self.drop1 = nn.Dropout(p=0.1)
        
        # 2. CNN layer (3x3 kernel)
        self.conv2 = nn.Conv2d(32, 64, 3)
        # maxpool layer with kernel_size = 2 and stride = 2
        self.pool2 = nn.MaxPool2d(2, 2)
        # input image has the size [32, 110, 110] so W = 110, F = 3, S = 1
        # Output_size = (W-F)/S +1 = 108
        # After one pool layer it would havethe dimension [64,54,54]
        # so the output's dimension is [64,54,54]
        self.drop2 = nn.Dropout(p=0.2)
        
        # 3. CNN layer (3x3 kernel)
        self.conv3 = nn.Conv2d(64, 128, 3)
        # maxpool layer with kernel_size = 2 and stride = 2
        self.pool3 = nn.MaxPool2d(2,2)
        # input image has the size [64, 54, 54] so W = 54, F = 3, S = 1
        # Output_size = (W-F)/S +1 = 52
        # After one pool layer it would havethe dimension [128,26,26] 
        # so the output's dimension is [128,26,26]
        self.drop3 = nn.Dropout(p=0.3)
       
        # 4. CNN layer (3x3 kernel)
        self.conv4 = nn.Conv2d(128, 256, 3)
        # maxpool layer with kernel_size = 2 and stride = 2
        self.pool4 = nn.MaxPool2d(2,2)
        # input image has the size [128,26,26] so W = 26, F = 3, S = 1
        # Output_size = (W-F)/S +1 = 24
        # After one pool layer it would havethe dimension [256,12,12] 
        # so the output's dimension is [256,12,12]
        self.drop4 = nn.Dropout(p=0.4)
        
        # 5. CNN layer (3x3 kernel)
        self.conv5 = nn.Conv2d(256, 512, 3)
        # maxpool layer with kernel_size = 2 and stride = 2
        self.pool5 = nn.MaxPool2d(2,2)
        # input image has the size [256,12,12] so W = 12, F = 3, S = 1
        # Output_size = (W-F)/S +1 = 10
        # After one pool layer it would havethe dimension [512,5,5] 
        # so the output's dimension is [512,5,5]        
        self.drop5 = nn.Dropout(p=0.5)
      
    
        self.fc6 = nn.Linear(512*5*5, 1360)
        self.drop6 = nn.Dropout(p=0.4)
        
        self.fc7 = nn.Linear(1360, 136)
)
        
        ## Note that among the layers to add, consider including:
        # maxpooling layers, multiple conv layers, fully-connected layers, and other layers (such as dropout or batch normalization) to avoid overfitting
        

        
    def forward(self, x):
        ## TODO: Define the feedforward behavior of this model
        ## x is the input image and, as an example, here you may choose to include a pool/conv step:
        
        x = self.pool1(F.relu(self.conv1(x)))
        x = self.drop1(x)
        
        x = self.pool2(F.relu(self.conv2(x)))
        x = self.drop2(x)
        
        x = self.pool3(F.relu(self.conv3(x)))
        x = self.drop3(x)
        
        x = self.pool4(F.relu(self.conv4(x)))
        x = self.drop4(x)
        
        x = self.pool5(F.relu(self.conv5(x)))
        x = self.drop5(x)
        
        x = x.view(x.size(0), -1)
        
        x = F.relu(self.fc6(x))
        x = self.drop6(x)
        
 
        
        x = self.fc7(x)

        # a modified x, having gone through all the layers of your model, should be returned
        return x