
# SCOTUS

## KimCNN
|    Optimizer/Loss         |  Val Metric  | Epochs  |     Micro-F1     |     Macro-F1     |  Time
|--------------------------:|-------------:|--------:|-----------------:|-----------------:|-----------------:|
| SGD + mse loss            |   Micro-F1   | 88      |     0.5600       |      0.3984      |   1087.52(s) |
| SGD + cross entropy loss  |   Micro-F1   | 17      |     0.5271       |      0.4219      |   190.91(s)  |
| Adam + cross entropy loss |   Micro-F1   | 16      |     0.6243       |      0.4948      |   202.52(s)  |
