# AOI-LTL
LTL inference based on AOI data to classify the pilots' visual behaviours

To use the solver:
First Use the following command to obtain model file


```
python learn_ltl_matrix.py -train_file=data/training_3.json -test_file=data/training_3.json -save_model=log/training_3.model -log_file=log/training_3.log -res_file=log/training_3.txt -epoch_num=20
```

Then interpret the model file to LTL formula using
```
python matrix2ltl.py -train_file=data/test_2.json -test_file=data/test_2.json -save_model=log/training_2.model -top_num=100
```
