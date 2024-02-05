# AOI-LTL
LTL inference based on AOI data to classify the pilots' visual behaviours

To use the solver:
First Use the following command to obtain model file


```
python learn_ltl_matrix.py -train_file=data/training_10.json -test_file=data/training_10.json -save_model=log/training_10.model -log_file=log/training_10.log -res_file=log/training_10.txt -epoch_num=20

python learn_ltl_matrix.py -train_file=data/training_10.json -test_file=data/training_10.json -save_model=log/training_10.model -log_file=log/training_10.log -res_file=log/training_10.txt -epoch_num=20
```

Then interpret the model file to LTL formula using
```
python matrix2ltl.py -train_file=data/training_10.json -test_file=data/test_9.json -save_model=log/training_10.model -top_num=100
python matrix2ltl.py -train_file=data/training_10.json -test_file=data/test_10.json -save_model=log/training_10.model -top_num=100
```

V2:
```
python learn_ltl_matrix.py -train_file=V2/Training_Set/20/training_10.json -test_file=V2/Training_Set/20/training_10.json -save_model=V2/Log/20/training_10.model -log_file=V2/Log/20/training_10.log -res_file=V2/Log/20/training_10.txt -epoch_num=20

python matrix2ltl.py -train_file=V2/Training_Set/20/training_10.json -test_file=V2/Training_Set/20/test_10.json -save_model=V2/Log/20/training_10.model -top_num=100
```