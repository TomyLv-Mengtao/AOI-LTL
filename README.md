# AOI-LTL
LTL inference based on AOI data to classify the pilots' visual behaviours

To use the solver:
First Use the following command to obtain model file


```
python learn_ltl_matrix.py -train_file=data/training_10.json -test_file=data/training_10.json -save_model=log/training_10.model -log_file=log/training_10.log -res_file=log/training_10.txt -epoch_num=20
```

Then interpret the model file to LTL formula using
```
python matrix2ltl.py -train_file=data/training_6.json -test_file=data/test_6.json -save_model=log/training_6.model -top_num=100
```
