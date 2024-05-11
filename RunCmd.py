import os

commands = [
"python matrix2ltl.py -train_file=K-Means/TrainSet/75/training_1.json -test_file=K-Means/TrainSet/75/test_1.json -save_model=K-Means/TrainSet/75/training_1.model -top_num=300",
"python matrix2ltl.py -train_file=K-Means/TrainSet/75/training_2.json -test_file=K-Means/TrainSet/75/test_2.json -save_model=K-Means/TrainSet/75/training_2.model -top_num=300",
"python matrix2ltl.py -train_file=K-Means/TrainSet/75/training_3.json -test_file=K-Means/TrainSet/75/test_3.json -save_model=K-Means/TrainSet/75/training_3.model -top_num=300",
"python matrix2ltl.py -train_file=K-Means/TrainSet/75/training_4.json -test_file=K-Means/TrainSet/75/test_4.json -save_model=K-Means/TrainSet/75/training_4.model -top_num=300",
"python matrix2ltl.py -train_file=K-Means/TrainSet/75/training_5.json -test_file=K-Means/TrainSet/75/test_5.json -save_model=K-Means/TrainSet/75/training_5.model -top_num=300",
"python matrix2ltl.py -train_file=K-Means/TrainSet/75/training_6.json -test_file=K-Means/TrainSet/75/test_6.json -save_model=K-Means/TrainSet/75/training_6.model -top_num=300",
"python matrix2ltl.py -train_file=K-Means/TrainSet/75/training_7.json -test_file=K-Means/TrainSet/75/test_7.json -save_model=K-Means/TrainSet/75/training_7.model -top_num=300",
"python matrix2ltl.py -train_file=K-Means/TrainSet/75/training_8.json -test_file=K-Means/TrainSet/75/test_8.json -save_model=K-Means/TrainSet/75/training_8.model -top_num=300",
"python matrix2ltl.py -train_file=K-Means/TrainSet/75/training_9.json -test_file=K-Means/TrainSet/75/test_9.json -save_model=K-Means/TrainSet/75/training_9.model -top_num=300",
"python matrix2ltl.py -train_file=K-Means/TrainSet/75/training_10.json -test_file=K-Means/TrainSet/75/test_10.json -save_model=K-Means/TrainSet/75/training_10.model -top_num=300",

"python matrix2ltl.py -train_file=K-Means/TrainSet/70/training_1.json -test_file=K-Means/TrainSet/70/test_1.json -save_model=K-Means/TrainSet/70/training_1.model -top_num=300",
"python matrix2ltl.py -train_file=K-Means/TrainSet/70/training_2.json -test_file=K-Means/TrainSet/70/test_2.json -save_model=K-Means/TrainSet/70/training_2.model -top_num=300",
"python matrix2ltl.py -train_file=K-Means/TrainSet/70/training_3.json -test_file=K-Means/TrainSet/70/test_3.json -save_model=K-Means/TrainSet/70/training_3.model -top_num=300",
"python matrix2ltl.py -train_file=K-Means/TrainSet/70/training_4.json -test_file=K-Means/TrainSet/70/test_4.json -save_model=K-Means/TrainSet/70/training_4.model -top_num=300",
"python matrix2ltl.py -train_file=K-Means/TrainSet/70/training_5.json -test_file=K-Means/TrainSet/70/test_5.json -save_model=K-Means/TrainSet/70/training_5.model -top_num=300",
"python matrix2ltl.py -train_file=K-Means/TrainSet/70/training_6.json -test_file=K-Means/TrainSet/70/test_6.json -save_model=K-Means/TrainSet/70/training_6.model -top_num=300",
"python matrix2ltl.py -train_file=K-Means/TrainSet/70/training_7.json -test_file=K-Means/TrainSet/70/test_7.json -save_model=K-Means/TrainSet/70/training_7.model -top_num=300",
"python matrix2ltl.py -train_file=K-Means/TrainSet/70/training_8.json -test_file=K-Means/TrainSet/70/test_8.json -save_model=K-Means/TrainSet/70/training_8.model -top_num=300",
"python matrix2ltl.py -train_file=K-Means/TrainSet/70/training_9.json -test_file=K-Means/TrainSet/70/test_9.json -save_model=K-Means/TrainSet/70/training_9.model -top_num=300",
"python matrix2ltl.py -train_file=K-Means/TrainSet/70/training_10.json -test_file=K-Means/TrainSet/70/test_10.json -save_model=K-Means/TrainSet/70/training_10.model -top_num=300",


"python matrix2ltl.py -train_file=K-Means/TrainSet/65/training_1.json -test_file=K-Means/TrainSet/65/test_1.json -save_model=K-Means/TrainSet/65/training_1.model -top_num=300",
"python matrix2ltl.py -train_file=K-Means/TrainSet/65/training_2.json -test_file=K-Means/TrainSet/65/test_2.json -save_model=K-Means/TrainSet/65/training_2.model -top_num=300",
"python matrix2ltl.py -train_file=K-Means/TrainSet/65/training_3.json -test_file=K-Means/TrainSet/65/test_3.json -save_model=K-Means/TrainSet/65/training_3.model -top_num=300",
"python matrix2ltl.py -train_file=K-Means/TrainSet/65/training_4.json -test_file=K-Means/TrainSet/65/test_4.json -save_model=K-Means/TrainSet/65/training_4.model -top_num=300",
"python matrix2ltl.py -train_file=K-Means/TrainSet/65/training_5.json -test_file=K-Means/TrainSet/65/test_5.json -save_model=K-Means/TrainSet/65/training_5.model -top_num=300",
"python matrix2ltl.py -train_file=K-Means/TrainSet/65/training_6.json -test_file=K-Means/TrainSet/65/test_6.json -save_model=K-Means/TrainSet/65/training_6.model -top_num=300",
"python matrix2ltl.py -train_file=K-Means/TrainSet/65/training_7.json -test_file=K-Means/TrainSet/65/test_7.json -save_model=K-Means/TrainSet/65/training_7.model -top_num=300",
"python matrix2ltl.py -train_file=K-Means/TrainSet/65/training_8.json -test_file=K-Means/TrainSet/65/test_8.json -save_model=K-Means/TrainSet/65/training_8.model -top_num=300",
"python matrix2ltl.py -train_file=K-Means/TrainSet/65/training_9.json -test_file=K-Means/TrainSet/65/test_9.json -save_model=K-Means/TrainSet/65/training_9.model -top_num=300",
"python matrix2ltl.py -train_file=K-Means/TrainSet/65/training_10.json -test_file=K-Means/TrainSet/65/test_10.json -save_model=K-Means/TrainSet/65/training_10.model -top_num=300",

"python matrix2ltl.py -train_file=K-Means/TrainSet/60/training_1.json -test_file=K-Means/TrainSet/60/test_1.json -save_model=K-Means/TrainSet/60/training_1.model -top_num=300",
"python matrix2ltl.py -train_file=K-Means/TrainSet/60/training_2.json -test_file=K-Means/TrainSet/60/test_2.json -save_model=K-Means/TrainSet/60/training_2.model -top_num=300",
"python matrix2ltl.py -train_file=K-Means/TrainSet/60/training_3.json -test_file=K-Means/TrainSet/60/test_3.json -save_model=K-Means/TrainSet/60/training_3.model -top_num=300",
"python matrix2ltl.py -train_file=K-Means/TrainSet/60/training_4.json -test_file=K-Means/TrainSet/60/test_4.json -save_model=K-Means/TrainSet/60/training_4.model -top_num=300",
"python matrix2ltl.py -train_file=K-Means/TrainSet/60/training_5.json -test_file=K-Means/TrainSet/60/test_5.json -save_model=K-Means/TrainSet/60/training_5.model -top_num=300",
"python matrix2ltl.py -train_file=K-Means/TrainSet/60/training_6.json -test_file=K-Means/TrainSet/60/test_6.json -save_model=K-Means/TrainSet/60/training_6.model -top_num=300",
"python matrix2ltl.py -train_file=K-Means/TrainSet/60/training_7.json -test_file=K-Means/TrainSet/60/test_7.json -save_model=K-Means/TrainSet/60/training_7.model -top_num=300",
"python matrix2ltl.py -train_file=K-Means/TrainSet/60/training_8.json -test_file=K-Means/TrainSet/60/test_8.json -save_model=K-Means/TrainSet/60/training_8.model -top_num=300",
"python matrix2ltl.py -train_file=K-Means/TrainSet/60/training_9.json -test_file=K-Means/TrainSet/60/test_9.json -save_model=K-Means/TrainSet/60/training_9.model -top_num=300",
"python matrix2ltl.py -train_file=K-Means/TrainSet/60/training_10.json -test_file=K-Means/TrainSet/60/test_10.json -save_model=K-Means/TrainSet/60/training_10.model -top_num=300",

"python matrix2ltl.py -train_file=K-Means/TrainSet/55/training_1.json -test_file=K-Means/TrainSet/55/test_1.json -save_model=K-Means/TrainSet/55/training_1.model -top_num=300",
"python matrix2ltl.py -train_file=K-Means/TrainSet/55/training_2.json -test_file=K-Means/TrainSet/55/test_2.json -save_model=K-Means/TrainSet/55/training_2.model -top_num=300",
"python matrix2ltl.py -train_file=K-Means/TrainSet/55/training_3.json -test_file=K-Means/TrainSet/55/test_3.json -save_model=K-Means/TrainSet/55/training_3.model -top_num=300",
"python matrix2ltl.py -train_file=K-Means/TrainSet/55/training_4.json -test_file=K-Means/TrainSet/55/test_4.json -save_model=K-Means/TrainSet/55/training_4.model -top_num=300",
"python matrix2ltl.py -train_file=K-Means/TrainSet/55/training_5.json -test_file=K-Means/TrainSet/55/test_5.json -save_model=K-Means/TrainSet/55/training_5.model -top_num=300",
"python matrix2ltl.py -train_file=K-Means/TrainSet/55/training_6.json -test_file=K-Means/TrainSet/55/test_6.json -save_model=K-Means/TrainSet/55/training_6.model -top_num=300",
"python matrix2ltl.py -train_file=K-Means/TrainSet/55/training_7.json -test_file=K-Means/TrainSet/55/test_7.json -save_model=K-Means/TrainSet/55/training_7.model -top_num=300",
"python matrix2ltl.py -train_file=K-Means/TrainSet/55/training_8.json -test_file=K-Means/TrainSet/55/test_8.json -save_model=K-Means/TrainSet/55/training_8.model -top_num=300",
"python matrix2ltl.py -train_file=K-Means/TrainSet/55/training_9.json -test_file=K-Means/TrainSet/55/test_9.json -save_model=K-Means/TrainSet/55/training_9.model -top_num=300",
"python matrix2ltl.py -train_file=K-Means/TrainSet/55/training_10.json -test_file=K-Means/TrainSet/55/test_10.json -save_model=K-Means/TrainSet/55/training_10.model -top_num=300",

"python matrix2ltl.py -train_file=K-Means/TrainSet/50/training_1.json -test_file=K-Means/TrainSet/50/test_1.json -save_model=K-Means/TrainSet/50/training_1.model -top_num=300",
"python matrix2ltl.py -train_file=K-Means/TrainSet/50/training_2.json -test_file=K-Means/TrainSet/50/test_2.json -save_model=K-Means/TrainSet/50/training_2.model -top_num=300",
"python matrix2ltl.py -train_file=K-Means/TrainSet/50/training_3.json -test_file=K-Means/TrainSet/50/test_3.json -save_model=K-Means/TrainSet/50/training_3.model -top_num=300",
"python matrix2ltl.py -train_file=K-Means/TrainSet/50/training_4.json -test_file=K-Means/TrainSet/50/test_4.json -save_model=K-Means/TrainSet/50/training_4.model -top_num=300",
"python matrix2ltl.py -train_file=K-Means/TrainSet/50/training_5.json -test_file=K-Means/TrainSet/50/test_5.json -save_model=K-Means/TrainSet/50/training_5.model -top_num=300",
"python matrix2ltl.py -train_file=K-Means/TrainSet/50/training_6.json -test_file=K-Means/TrainSet/50/test_6.json -save_model=K-Means/TrainSet/50/training_6.model -top_num=300",
"python matrix2ltl.py -train_file=K-Means/TrainSet/50/training_7.json -test_file=K-Means/TrainSet/50/test_7.json -save_model=K-Means/TrainSet/50/training_7.model -top_num=300",
"python matrix2ltl.py -train_file=K-Means/TrainSet/50/training_8.json -test_file=K-Means/TrainSet/50/test_8.json -save_model=K-Means/TrainSet/50/training_8.model -top_num=300",
"python matrix2ltl.py -train_file=K-Means/TrainSet/50/training_9.json -test_file=K-Means/TrainSet/50/test_9.json -save_model=K-Means/TrainSet/50/training_9.model -top_num=300",
"python matrix2ltl.py -train_file=K-Means/TrainSet/50/training_10.json -test_file=K-Means/TrainSet/50/test_10.json -save_model=K-Means/TrainSet/50/training_10.model -top_num=300",

"python matrix2ltl.py -train_file=K-Means/TrainSet/45/training_1.json -test_file=K-Means/TrainSet/45/test_1.json -save_model=K-Means/TrainSet/45/training_1.model -top_num=300",
"python matrix2ltl.py -train_file=K-Means/TrainSet/45/training_2.json -test_file=K-Means/TrainSet/45/test_2.json -save_model=K-Means/TrainSet/45/training_2.model -top_num=300",
"python matrix2ltl.py -train_file=K-Means/TrainSet/45/training_3.json -test_file=K-Means/TrainSet/45/test_3.json -save_model=K-Means/TrainSet/45/training_3.model -top_num=300",
"python matrix2ltl.py -train_file=K-Means/TrainSet/45/training_4.json -test_file=K-Means/TrainSet/45/test_4.json -save_model=K-Means/TrainSet/45/training_4.model -top_num=300",
"python matrix2ltl.py -train_file=K-Means/TrainSet/45/training_5.json -test_file=K-Means/TrainSet/45/test_5.json -save_model=K-Means/TrainSet/45/training_5.model -top_num=300",
"python matrix2ltl.py -train_file=K-Means/TrainSet/45/training_6.json -test_file=K-Means/TrainSet/45/test_6.json -save_model=K-Means/TrainSet/45/training_6.model -top_num=300",
"python matrix2ltl.py -train_file=K-Means/TrainSet/45/training_7.json -test_file=K-Means/TrainSet/45/test_7.json -save_model=K-Means/TrainSet/45/training_7.model -top_num=300",
"python matrix2ltl.py -train_file=K-Means/TrainSet/45/training_8.json -test_file=K-Means/TrainSet/45/test_8.json -save_model=K-Means/TrainSet/45/training_8.model -top_num=300",
"python matrix2ltl.py -train_file=K-Means/TrainSet/45/training_9.json -test_file=K-Means/TrainSet/45/test_9.json -save_model=K-Means/TrainSet/45/training_9.model -top_num=300",
"python matrix2ltl.py -train_file=K-Means/TrainSet/45/training_10.json -test_file=K-Means/TrainSet/45/test_10.json -save_model=K-Means/TrainSet/45/training_10.model -top_num=300",

"python matrix2ltl.py -train_file=K-Means/TrainSet/40/training_1.json -test_file=K-Means/TrainSet/40/test_1.json -save_model=K-Means/TrainSet/40/training_1.model -top_num=300",
"python matrix2ltl.py -train_file=K-Means/TrainSet/40/training_2.json -test_file=K-Means/TrainSet/40/test_2.json -save_model=K-Means/TrainSet/40/training_2.model -top_num=300",
"python matrix2ltl.py -train_file=K-Means/TrainSet/40/training_3.json -test_file=K-Means/TrainSet/40/test_3.json -save_model=K-Means/TrainSet/40/training_3.model -top_num=300",
"python matrix2ltl.py -train_file=K-Means/TrainSet/40/training_4.json -test_file=K-Means/TrainSet/40/test_4.json -save_model=K-Means/TrainSet/40/training_4.model -top_num=300",
"python matrix2ltl.py -train_file=K-Means/TrainSet/40/training_5.json -test_file=K-Means/TrainSet/40/test_5.json -save_model=K-Means/TrainSet/40/training_5.model -top_num=300",
"python matrix2ltl.py -train_file=K-Means/TrainSet/40/training_6.json -test_file=K-Means/TrainSet/40/test_6.json -save_model=K-Means/TrainSet/40/training_6.model -top_num=300",
"python matrix2ltl.py -train_file=K-Means/TrainSet/40/training_7.json -test_file=K-Means/TrainSet/40/test_7.json -save_model=K-Means/TrainSet/40/training_7.model -top_num=300",
"python matrix2ltl.py -train_file=K-Means/TrainSet/40/training_8.json -test_file=K-Means/TrainSet/40/test_8.json -save_model=K-Means/TrainSet/40/training_8.model -top_num=300",
"python matrix2ltl.py -train_file=K-Means/TrainSet/40/training_9.json -test_file=K-Means/TrainSet/40/test_9.json -save_model=K-Means/TrainSet/40/training_9.model -top_num=300",
"python matrix2ltl.py -train_file=K-Means/TrainSet/40/training_10.json -test_file=K-Means/TrainSet/40/test_10.json -save_model=K-Means/TrainSet/40/training_10.model -top_num=300"

]

i = 1
for command in commands:
    print("\n",i," VAT 解析")
    os.system(command)
    i +=1


'''
All-All VAT 学习

"python learn_ltl_matrix.py -train_file=25iles/2ndRnd/All2All/40/training_1.json -test_file=25iles/2ndRnd/All2All/40/training_1.json -save_model=25iles/2ndRnd/All2All/40/training_1.model -log_file=25iles/2ndRnd/All2All/40/training_1.log -res_file=25iles/2ndRnd/All2All/40/training_1.txt -epoch_num=60",
"python learn_ltl_matrix.py -train_file=25iles/2ndRnd/All2All/40/training_2.json -test_file=25iles/2ndRnd/All2All/40/training_2.json -save_model=25iles/2ndRnd/All2All/40/training_2.model -log_file=25iles/2ndRnd/All2All/40/training_2.log -res_file=25iles/2ndRnd/All2All/40/training_2.txt -epoch_num=60",
"python learn_ltl_matrix.py -train_file=25iles/2ndRnd/All2All/40/training_3.json -test_file=25iles/2ndRnd/All2All/40/training_3.json -save_model=25iles/2ndRnd/All2All/40/training_3.model -log_file=25iles/2ndRnd/All2All/40/training_3.log -res_file=25iles/2ndRnd/All2All/40/training_3.txt -epoch_num=60",
"python learn_ltl_matrix.py -train_file=25iles/2ndRnd/All2All/40/training_4.json -test_file=25iles/2ndRnd/All2All/40/training_4.json -save_model=25iles/2ndRnd/All2All/40/training_4.model -log_file=25iles/2ndRnd/All2All/40/training_4.log -res_file=25iles/2ndRnd/All2All/40/training_4.txt -epoch_num=60",
"python learn_ltl_matrix.py -train_file=25iles/2ndRnd/All2All/40/training_5.json -test_file=25iles/2ndRnd/All2All/40/training_5.json -save_model=25iles/2ndRnd/All2All/40/training_5.model -log_file=25iles/2ndRnd/All2All/40/training_5.log -res_file=25iles/2ndRnd/All2All/40/training_5.txt -epoch_num=60",
"python learn_ltl_matrix.py -train_file=25iles/2ndRnd/All2All/40/training_6.json -test_file=25iles/2ndRnd/All2All/40/training_6.json -save_model=25iles/2ndRnd/All2All/40/training_6.model -log_file=25iles/2ndRnd/All2All/40/training_6.log -res_file=25iles/2ndRnd/All2All/40/training_6.txt -epoch_num=60",
"python learn_ltl_matrix.py -train_file=25iles/2ndRnd/All2All/40/training_7.json -test_file=25iles/2ndRnd/All2All/40/training_7.json -save_model=25iles/2ndRnd/All2All/40/training_7.model -log_file=25iles/2ndRnd/All2All/40/training_7.log -res_file=25iles/2ndRnd/All2All/40/training_7.txt -epoch_num=60",
"python learn_ltl_matrix.py -train_file=25iles/2ndRnd/All2All/40/training_8.json -test_file=25iles/2ndRnd/All2All/40/training_8.json -save_model=25iles/2ndRnd/All2All/40/training_8.model -log_file=25iles/2ndRnd/All2All/40/training_8.log -res_file=25iles/2ndRnd/All2All/40/training_8.txt -epoch_num=60",
"python learn_ltl_matrix.py -train_file=25iles/2ndRnd/All2All/40/training_9.json -test_file=25iles/2ndRnd/All2All/40/training_9.json -save_model=25iles/2ndRnd/All2All/40/training_9.model -log_file=25iles/2ndRnd/All2All/40/training_9.log -res_file=25iles/2ndRnd/All2All/40/training_9.txt -epoch_num=60",
"python learn_ltl_matrix.py -train_file=25iles/2ndRnd/All2All/40/training_10.json -test_file=25iles/2ndRnd/All2All/40/training_10.json -save_model=25iles/2ndRnd/All2All/40/training_10.model -log_file=25iles/2ndRnd/All2All/40/training_10.log -res_file=25iles/2ndRnd/All2All/40/training_10.txt -epoch_num=60",




90-10 的 40秒 VAT 解析
"python matrix2ltl.py -train_file=K-Means/TrainSet/30/training_1.json -test_file=K-Means/TrainSet/30/test_1.json -save_model=K-Means/TrainSet/30/training_1.model -top_num=100",
"python matrix2ltl.py -train_file=K-Means/TrainSet/30/training_2.json -test_file=K-Means/TrainSet/30/test_2.json -save_model=K-Means/TrainSet/30/training_2.model -top_num=100",
"python matrix2ltl.py -train_file=K-Means/TrainSet/30/training_3.json -test_file=K-Means/TrainSet/30/test_3.json -save_model=K-Means/TrainSet/30/training_3.model -top_num=100",
"python matrix2ltl.py -train_file=K-Means/TrainSet/30/training_4.json -test_file=K-Means/TrainSet/30/test_4.json -save_model=K-Means/TrainSet/30/training_4.model -top_num=100",
"python matrix2ltl.py -train_file=K-Means/TrainSet/30/training_5.json -test_file=K-Means/TrainSet/30/test_5.json -save_model=K-Means/TrainSet/30/training_5.model -top_num=100",
"python matrix2ltl.py -train_file=K-Means/TrainSet/30/training_6.json -test_file=K-Means/TrainSet/30/test_6.json -save_model=K-Means/TrainSet/30/training_6.model -top_num=100",
"python matrix2ltl.py -train_file=K-Means/TrainSet/30/training_7.json -test_file=K-Means/TrainSet/30/test_7.json -save_model=K-Means/TrainSet/30/training_7.model -top_num=100",
"python matrix2ltl.py -train_file=K-Means/TrainSet/30/training_8.json -test_file=K-Means/TrainSet/30/test_8.json -save_model=K-Means/TrainSet/30/training_8.model -top_num=100",
"python matrix2ltl.py -train_file=K-Means/TrainSet/30/training_9.json -test_file=K-Means/TrainSet/30/test_9.json -save_model=K-Means/TrainSet/30/training_9.model -top_num=100",
"python matrix2ltl.py -train_file=K-Means/TrainSet/30/training_10.json -test_file=K-Means/TrainSet/30/test_10.json -save_model=K-Means/TrainSet/30/training_10.model -top_num=100"

'''
