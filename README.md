# AOI-LTL
LTL inference based on AOI data to classify the pilots' visual behaviours

To use the solver:
First Use the following command to obtain model file

```
python learn_ltl_matrix.py -train_file=mindata_f3_d0/E2_0.json -test_file=mindata_f3_d0/ET2_0.json -save_model=mindata_f3_d0-2_0.model -log_file=mindata_f3_d0-2_0.log -res_file=mindata_f3_d0-2_0.txt -epoch_num=20
```
'''
python learn_ltl_matrix.py -train_file=data/training_1.json -test_file=data/training_1.json -save_model=log/training_1.model -log_file=log/training_1.log -res_file=log/training_1.txt -epoch_num=20
'''

Then interpret the model file to LTL formula using
```
python matrix2ltl.py -train_file=mindata_f3_d0/E2_0.json -test_file=mindata_f3_d0/ET2_0.json -save_model=mindata_f3_d0-2_0.model -top_num=100
```
