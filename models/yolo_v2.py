#

import torch
import torch.nn as nn
import torch.nn.functiional as F
import numpy as np
from easydict import EasyDict as edict

class yolo_v2(nn.Module):
	def __init__(self):
		super(yolo_v2,self).__init__()
		self.blocks = self.create_blocks()
		self.models  = self.create_model()
		self.header = torch.IntTensor([0,0,0,0])
		self.seen   = 0


	def create_model(self):
		models = nn.ModuleList()

		#32
		conv0  = nn.Sequential()
		conv0.add_moduel('conv0',nn.Conv2d(3,32,3,1,1,bias=False))
		conv0.add_moduel('bn0',nn.BatchNorm2d(32))
		conv0.add_moduel('leaky0',nn.LeakyReLU(0.1,inplace=True))
		models.append(conv0)
		#max pool 0
		models.append(nn.MaxPool2d(2,2))

		#64
		conv1.add_moduel('conv1',nn.Conv2d(32,64,3,1,1,bias=False))
		conv1.add_moduel('bn1',nn.BatchNorm2d(64))
		conv1.add_moduel('leaky1',nn.LeakyReLU(0.1,inplace=True))
		models.append(conv1)
		#max pool 1
		models.append(nn.MaxPool2d(2,2))

        #128
		conv2 = nn.Sequential()
		conv2.add_moduel('conv2',nn.Conv2d(64,128,3,1,1,bias=False))
		conv2.add_moduel('bn2',nn.BatchNorm2d(128))
		conv2.add_moduel('leaky2',nn.LeakyReLU(0.1,inplace=True))
		models.append(conv2)
		conv3 = nn.Sequential()
		conv3.add_moduel('conv3',nn.Conv2d(128,64,1,1,1,bias=False))
		conv3.add_moduel('bn3',nn.BatchNorm2d(64))
		conv3.add_moduel('leaky3',nn.LeakyReLU(0.1,inplace=True))
		models.append(conv3)
		conv4 = nn.Sequential()
		conv4.add_moduel('conv4',nn.Conv2d(64,128,3,1,1,bias=False))
		conv4.add_moduel('bn4',nn.BatchNorm2d(128))
		conv4.add_moduel('leaky4',nn.LeakyReLU(0.1,inplace=True))
		models.append(conv4)
		#max pool 2
		models.append(nn.MaxPool2d(2,2))

		#256
		conv5 = nn.Sequential()
		conv5.add_moduel('conv5',nn.Conv2d(128,256,3,1,1,bias=False))
		conv5.add_moduel('bn5',nn.BatchNorm2d(256))
		conv5.add_moduel('leaky5',nn.LeakyReLU(0.1,inplace=True))
		models.append(conv5)
		conv6 = nn.Sequential()
		conv6.add_moduel('conv6',nn.Conv2d(256,128,1,1,1,bias=False))
		conv6.add_moduel('bn6',nn.BatchNorm2d(128))
		conv6.add_moduel('leaky6',nn.LeakyReLU(0.1,inplace=True))
		models.append(conv6)
		conv7 = nn.Sequential()
		conv7.add_moduel('conv7',nn.Conv2d(128,256,3,1,1,bias=False))
		conv7.add_moduel('bn7',nn.BatchNorm2d(256))
		conv7.add_moduel('leaky7',nn.LeakyReLU(0.1,inplace=True))
		models.append(conv7)
		#max pool 3 
		models.append(nn.MaxPool2d(2,2))

		#512
		conv8 = nn.Sequential()
		conv8.add_moduel('conv8',nn.Conv2d(256,512,3,1,1,bias=False))
		conv8.add_moduel('bn8',nn.BatchNorm2d(512))
		conv8.add_moduel('leaky8',nn.LeakyReLU(0.1,inplace=True))
		models.append(conv8)
		conv9 = nn.Sequential()
		conv9.add_moduel('conv9',nn.Conv2d(512,256,1,1,1,bias=False))
		conv9.add_moduel('bn9',nn.BatchNorm2d(256))
		conv9.add_moduel('leaky9',nn.LeakyReLU(0.1,inplace=True))
		models.append(conv9)
		conv10 = nn.Sequential()
		conv10.add_moduel('conv10',nn.Conv2d(256,512,3,1,1,bias=False))
		conv10.add_moduel('bn10',nn.BatchNorm2d(512))
		conv10.add_moduel('leaky10',nn.LeakyReLU(0.1,inplace=True))
		models.append(conv10)
		conv11 = nn.Sequential()
		conv11.add_moduel('conv11',nn.Conv2d(512,256,1,1,1,bias=False))
		conv11.add_moduel('bn11',nn.BatchNorm2d(256))
		conv11.add_moduel('leaky11',nn.LeakyReLU(0.1,inplace=True))
		models.append(conv11)
		conv12 = nn.Sequential()
		conv12.add_moduel('conv12',nn.Conv2d(256,512,3,1,1,bias=False))
		conv12.add_moduel('bn12',nn.BatchNorm2d(512))
		conv12.add_moduel('leaky12',nn.LeakyReLU(0.1,inplace=True))
		models.append(conv12)
		#max pool 4
		models.append(nn.MaxPool2d(2,2))

		#1024
		conv13 = nn.Sequential()
		conv13.add_moduel('conv13',nn.Conv2d(512,1024,3,1,1,bias=False))
		conv13.add_moduel('bn13',nn.BatchNorm2d(1024))
		conv13.add_moduel('leaky13',nn.LeakyReLU(0.1,inplace=True))
		models.append(conv13)
		conv14 = nn.Sequential()
		conv14.add_moduel('conv14',nn.Conv2d(1024,512,1,1,1,bias=False))
		conv14.add_moduel('bn14',nn.BatchNorm2d(512))
		conv14.add_moduel('leaky14',nn.LeakyReLU(0.1,inplace=True))
		models.append(conv14)
		conv15 = nn.Sequential()
		conv15.add_moduel('conv15',nn.Conv2d(512,1024,3,1,1,bias=False))
		conv15.add_moduel('bn15',nn.BatchNorm2d(1024))
		conv15.add_moduel('leaky15',nn.LeakyReLU(0.1,inplace=True))
		models.append(conv15)
		conv16 = nn.Sequential()
		conv16.add_moduel('conv16',nn.Conv2d(1024,512,1,1,1,bias=False))
		conv16.add_moduel('bn16',nn.BatchNorm2d(512))
		conv16.add_moduel('leaky16',nn.LeakyReLU(0.1,inplace=True))
		models.append(conv16)
		conv17 = nn.Sequential()
		conv17.add_moduel('conv17',nn.Conv2d(512,1024,3,1,1,bias=False))
		conv17.add_moduel('bn17',nn.BatchNorm2d(1024))
		conv17.add_moduel('leaky17',nn.LeakyReLU(0.1,inplace=True))
		models.append(conv17)

	def forward(self,x):
		for block in blocks:


	def load_weights(self,weight_file):


	def create_blocks(self):
		blocks = []

		block = edict()
		block.type    		= "convolutional"
		block.filters 		= 32
		block.size    		= 3
		block.pad     		= 1
		block.stride  		= 1
		block.activation 	= "leaky"
		block.batch_normalize = 1
		blocks.append(block)

		block = edict()
		block.size         = 2
		block.stride       = 2
		blocks.append(block)

		block.type    		= "convolutional"
		block.filters 		= 64
		block.size    		= 3
		block.pad     		= 1
		block.stride  		= 1
		block.activation 	= "leaky"
		block.batch_normalize = 1
		blocks.append(block)

		block = edict()
		block.size         = 2
		block.stride       = 2
		blocks.append(block)

		block.type    		= "convolutional"
		block.filters 		= 128
		block.size    		= 3
		block.pad     		= 1
		block.stride  		= 1
		block.activation 	= "leaky"
		block.batch_normalize = 1
		blocks.append(block)

		block.type    		= "convolutional"
		block.filters 		= 64
		block.size    		= 1
		block.pad     		= 1
		block.stride  		= 1
		block.activation 	= "leaky"
		block.batch_normalize = 1
		blocks.append(block)

		block.type    		= "convolutional"
		block.filters 		= 128
		block.size    		= 3
		block.pad     		= 1
		block.stride  		= 1
		block.activation 	= "leaky"
		block.batch_normalize = 1
		blocks.append(block)

		block = edict()
		block.size         = 2
		block.stride       = 2
		blocks.append(block)

		block.type    		= "convolutional"
		block.filters 		= 256
		block.size    		= 3
		block.pad     		= 1
		block.stride  		= 1
		block.activation 	= "leaky"
		block.batch_normalize = 1
		blocks.append(block)

		block.type    		= "convolutional"
		block.filters 		= 128
		block.size    		= 1
		block.pad     		= 1
		block.stride  		= 1
		block.activation 	= "leaky"
		block.batch_normalize = 1
		blocks.append(block)

		block.type    		= "convolutional"
		block.filters 		= 256
		block.size    		= 3
		block.pad     		= 1
		block.stride  		= 1
		block.activation 	= "leaky"
		block.batch_normalize = 1
		blocks.append(block)

		block = edict()
		block.size         = 2
		block.stride       = 2
		blocks.append(block)

		block.type    		= "convolutional"
		block.filters 		= 512
		block.size    		= 3
		block.pad     		= 1
		block.stride  		= 1
		block.activation 	= "leaky"
		block.batch_normalize = 1
		blocks.append(block)

		block.type    		= "convolutional"
		block.filters 		= 256
		block.size    		= 1
		block.pad     		= 1
		block.stride  		= 1
		block.activation 	= "leaky"
		block.batch_normalize = 1
		blocks.append(block)

		block.type    		= "convolutional"
		block.filters 		= 512
		block.size    		= 3
		block.pad     		= 1
		block.stride  		= 1
		block.activation 	= "leaky"
		block.batch_normalize = 1
		blocks.append(block)

		block.type    		= "convolutional"
		block.filters 		= 256
		block.size    		= 1
		block.pad     		= 1
		block.stride  		= 1
		block.activation 	= "leaky"
		block.batch_normalize = 1
		blocks.append(block)

		block.type    		= "convolutional"
		block.filters 		= 512
		block.size    		= 3
		block.pad     		= 1
		block.stride  		= 1
		block.activation 	= "leaky"
		block.batch_normalize = 1
		blocks.append(block)


		block = edict()
		block.size         = 2
		block.stride       = 2
		blocks.append(block)


		block.type    		= "convolutional"
		block.filters 		= 1024
		block.size    		= 3
		block.pad     		= 1
		block.stride  		= 1
		block.activation 	= "leaky"
		block.batch_normalize = 1
		blocks.append(block)

		block.type    		= "convolutional"
		block.filters 		= 512
		block.size    		= 1
		block.pad     		= 1
		block.stride  		= 1
		block.activation 	= "leaky"
		block.batch_normalize = 1
		blocks.append(block)

		block.type    		= "convolutional"
		block.filters 		= 1024
		block.size    		= 3
		block.pad     		= 1
		block.stride  		= 1
		block.activation 	= "leaky"
		block.batch_normalize = 1
		blocks.append(block)

		block.type    		= "convolutional"
		block.filters 		= 512
		block.size    		= 1
		block.pad     		= 1
		block.stride  		= 1
		block.activation 	= "leaky"
		block.batch_normalize = 1
		blocks.append(block)

		block.type    		= "convolutional"
		block.filters 		= 1024
		block.size    		= 3
		block.pad     		= 1
		block.stride  		= 1
		block.activation 	= "leaky"
		block.batch_normalize = 1
		blocks.append(block)
##################################
		block.type    		= "convolutional"
		block.filters 		= 1024
		block.size    		= 3
		block.pad     		= 1
		block.stride  		= 1
		block.activation 	= "leaky"
		block.batch_normalize = 1
		blocks.append(block)

		block.type    		= "convolutional"
		block.filters 		= 1024
		block.size    		= 3
		block.pad     		= 1
		block.stride  		= 1
		block.activation 	= "leaky"
		block.batch_normalize = 1
		blocks.append(block)

		block.type    		= "route"
		block.layers 		= "-9"
		blocks.append(block)

		block.type    		  = "convolutional"
		block.filters 		  = 64
		block.size    		  = 1
		block.pad     		  = 1
		block.stride  		  = 1
		block.activation 	  = "leaky"
		block.batch_normalize = 1
		blocks.append(block)

		block.type    		  = "route"
		block.layers 		  = "-1,-4"
		blocks.append(block)

		block.type    		  = "convolutional"
		block.filters 		  = 1024
		block.size    		  = 3
		block.pad     		  = 1
		block.stride  		  = 1
		block.activation 	  = "leaky"
		block.batch_normalize = 1
		blocks.append(block)

		block.type    		  = "convolutional"
		block.filters 		  = 125
		block.size    		  = 1
		block.pad     		  = 1
		block.stride  		  = 1
		block.activation 	  = "linear"
		blocks.append(block)

		block.type    		  = "region"
		block.anchors 		  = "1.3221, 1.73145, 3.19275, 4.00944, 5.05587, 8.09892, 9.47112, 4.84053, 11.2364, 10.0071"
		block.bias_match      = 1
		block.classes     	  = 20
		block.coords  		  = 4
		block.num             = 5
		block.softmax         = 1
		block.jitter          = 0.3
		block.rescore         = 1
		block.object_scale    = 5
		block.nnobject_scale  = 1
		block.class_scale     = 1
		block.coord_scale     = 1
		block.absolute        = 1
		block.thresh          = 0.6
		block.random          = 1
		
		blocks.append(block)




		return blocks




