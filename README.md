# AOI-LTL
LTL inference based on AOI data to classify the pilots' visual behaviours

To use the solver:
First Use the following command to obtain model file


```
python learn_ltl_matrix.py -train_file=data/training_2.json -test_file=data/training_2.json -save_model=log/training_2.model -log_file=log/training_2.log -res_file=log/training_2.txt -epoch_num=20

python learn_ltl_matrix.py -train_file=data/training_1.json -test_file=data/training_1.json -save_model=log/training_1.model -log_file=log/training_1.log -res_file=log/training_1.txt -epoch_num=20

```

Then interpret the model file to LTL formula using
```
python matrix2ltl.py -train_file=data/training_1.json -test_file=data/test_1.json -save_model=log/training_1.model -top_num=100
python matrix2ltl.py -train_file=data/training_2.json -test_file=data/test_2.json -save_model=log/training_2.model -top_num=100
```
