import torch.nn as nn
import torch.nn.functional as F


class BaseModel(nn.Module):
    '''Base Model for process different inputs

    Args:
        config (ArgDict): config of the experiment
        embed_vecs (FloatTensor): embedding vectors for initialization
    '''

    def __init__(
        self,
        embed_vecs,
        dropout=0.2,
        activation='relu',
        **kwargs
    ):
        super().__init__()
        self.embedding = nn.Embedding(len(embed_vecs), embed_vecs.shape[1], padding_idx=0)
        self.embedding.weight.data = embed_vecs.clone()
        self.embed_drop = nn.Dropout(p=dropout)
        # TODO define the activation function to model
        self.activation = getattr(F, activation)
