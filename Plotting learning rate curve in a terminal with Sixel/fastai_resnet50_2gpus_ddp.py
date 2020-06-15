#!/usr/bin/env python
# coding: utf-8

# In[1]:


import warnings
warnings.filterwarnings('ignore')

from fastai.vision import *
from fastai.callbacks import *
from fastai.distributed import *
from fastai.script import *


# In[2]:


def valid_func(o):
    return 'test' in str(o)

def label_func(o):
    name = o.name
    if 'virus' in name:
        return 'virus'
    if 'bacteria' in name:
        return 'bacteria'
    return 'normal'


# In[3]:


def get_data(sz=456, bs=64):
    data_path = Path('./chest_xray').absolute()
    stats = ([0.48746821, 0.48746821, 0.48746821], [0.24557937, 0.24557937, 0.24557937])

    data = (ImageList.from_folder(data_path)
        .split_by_valid_func(valid_func)
        .label_from_func(label_func)
        .transform(get_transforms(), size=sz)
        .databunch(bs=bs)
        .normalize(stats)
        )
    return data


# In[4]:


def get_learner(data, lr=0.003):
    model_path = Path('./model').absolute()
    learn = cnn_learner(data, 
                    models.resnet50,
                    bn_wd=False,
                    metrics=error_rate,
                    loss_func=LabelSmoothingCrossEntropy(),
                    callback_fns=[BnFreeze,
                                  partial(SaveModelCallback, monitor='error_rate', name='best_error')
                                 ],
                    model_dir = model_path
                   ).to_fp16()
    return learn


# In[5]:


@call_parse
def main( gpu:Param("GPU to run on", str)=None ):
    gpu = setup_distrib(gpu)
    n_gpus = num_distrib()
    print(f'Running on GPU {gpu} of {n_gpus}')
    
    data = get_data()
    learn = get_learner(data)
    learn.to_distributed(gpu)

    learn.lr_find()
    learn.recorder.plot(suggestion=True)
    learn.fit_one_cycle(5)
    
    learn.unfreeze()
    lr = 1e-4
    learn.lr_find()
    learn.recorder.plot(suggestion=True)
    learn.fit_one_cycle(5, slice(lr/40, lr))


# In[ ]:




