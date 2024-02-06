import os

commands = [
    "python learn_ltl_matrix.py -train_file=All2All/5/training_1.json -test_file=All2All/5/training_1.json -save_model=All2All/5/training_1.model -log_file=All2All/5/training_1.log -res_file=All2All/5/training_1.txt -epoch_num=80",
    "python learn_ltl_matrix.py -train_file=All2All/5/training_2.json -test_file=All2All/5/training_2.json -save_model=All2All/5/training_2.model -log_file=All2All/5/training_2.log -res_file=All2All/5/training_2.txt -epoch_num=80",
    "python learn_ltl_matrix.py -train_file=All2All/5/training_3.json -test_file=All2All/5/training_3.json -save_model=All2All/5/training_3.model -log_file=All2All/5/training_3.log -res_file=All2All/5/training_3.txt -epoch_num=80",
    "python learn_ltl_matrix.py -train_file=All2All/5/training_4.json -test_file=All2All/5/training_4.json -save_model=All2All/5/training_4.model -log_file=All2All/5/training_4.log -res_file=All2All/5/training_4.txt -epoch_num=80",
    "python learn_ltl_matrix.py -train_file=All2All/5/training_5.json -test_file=All2All/5/training_5.json -save_model=All2All/5/training_5.model -log_file=All2All/5/training_5.log -res_file=All2All/5/training_5.txt -epoch_num=80",
    "python learn_ltl_matrix.py -train_file=All2All/5/training_6.json -test_file=All2All/5/training_6.json -save_model=All2All/5/training_6.model -log_file=All2All/5/training_6.log -res_file=All2All/5/training_6.txt -epoch_num=80",
    "python learn_ltl_matrix.py -train_file=All2All/5/training_7.json -test_file=All2All/5/training_7.json -save_model=All2All/5/training_7.model -log_file=All2All/5/training_7.log -res_file=All2All/5/training_7.txt -epoch_num=80",
    "python learn_ltl_matrix.py -train_file=All2All/5/training_8.json -test_file=All2All/5/training_8.json -save_model=All2All/5/training_8.model -log_file=All2All/5/training_8.log -res_file=All2All/5/training_8.txt -epoch_num=80",
    "python learn_ltl_matrix.py -train_file=All2All/5/training_9.json -test_file=All2All/5/training_9.json -save_model=All2All/5/training_9.model -log_file=All2All/5/training_9.log -res_file=All2All/5/training_9.txt -epoch_num=80",
    "python learn_ltl_matrix.py -train_file=All2All/5/training_10.json -test_file=All2All/5/training_10.json -save_model=All2All/5/training_10.model -log_file=All2All/5/training_10.log -res_file=All2All/5/training_10.txt -epoch_num=80"
]

for command in commands:
    os.system(command)