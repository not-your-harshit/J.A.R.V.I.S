from nltk.util import Index
import numpy as np
import json
import torch.nn as nn
import torch
from torch.utils.data import dataset, dataloader
from AdminComman.Nuron import bag_word, tokenize, stem
from AdminComman.Brain import NuerlNet

with open('React.json', 'r') as f:
    React = json.load(f)

all_words = []
tags = []
xy = []

for intent in React['intents']:
    tag = intent['tag']
    tags.append(tag)

    for pattern in intent['patterns']:
        print(pattern)
        w = tokenize(pattern)
        all_words.extend(w)
        xy.append((w, tag))

        ingnore_word = [',', '?', '/', '.', '!']
        all_word =  [stem(w)for w in all_words if w not in ingnore_word]
        all_word = sorted(set(all_word)) 
        tags  =  sorted(set(tags))

        x_train = [] 
        y_train = [] 


        for (pattern_sentence,tag) in xy:
            bag = bag_word(pattern_sentence, all_words)
            x_train.append(bag)

            Label = tags.index(tag)
            y_train.append(Label)

x_train = np.array(x_train)
y_tarin = np.array(y_train)

num_epochs = 1000
batch_size = 8   
lerning_rate = 0.001
input_size = len(x_train[0])
hidden_size = 8
output_size = len(tags)

print("Training The Model.....")


class ChatDataset(dataset):

    def __init__(self):
        self.n_examples = len(x_train)
        self.x_data = x_train
        self.y_data = y_train
    
    def __getitem__(self):
        return self.x_data[Index],self.y_data[Index]
    
dataset = ChatDataset()

train_loder = dataloader(dataset=dataset , batch_size= batch_size , shuffle = True , num_worker = 0 ) 


device =  torch.device('cuda' if torch.cuda.is_available() else'cpu')
model = NuerlNet(input_size,hidden_size,output_size).to(device=device)
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(),lr=lerning_rate)


