import os

commands = [

"python matrix2ltl.py -train_file=V2/Training_Set/35/training_1.json -test_file=V2/Training_Set/35/test_1.json -save_model=V2/Log/35/training_1.model -top_num=100",
"python matrix2ltl.py -train_file=V2/Training_Set/35/training_2.json -test_file=V2/Training_Set/35/test_2.json -save_model=V2/Log/35/training_2.model -top_num=100",
"python matrix2ltl.py -train_file=V2/Training_Set/35/training_3.json -test_file=V2/Training_Set/35/test_3.json -save_model=V2/Log/35/training_3.model -top_num=100",
"python matrix2ltl.py -train_file=V2/Training_Set/35/training_4.json -test_file=V2/Training_Set/35/test_4.json -save_model=V2/Log/35/training_4.model -top_num=100",
"python matrix2ltl.py -train_file=V2/Training_Set/35/training_5.json -test_file=V2/Training_Set/35/test_5.json -save_model=V2/Log/35/training_5.model -top_num=100",
"python matrix2ltl.py -train_file=V2/Training_Set/35/training_6.json -test_file=V2/Training_Set/35/test_6.json -save_model=V2/Log/35/training_6.model -top_num=100",
"python matrix2ltl.py -train_file=V2/Training_Set/35/training_7.json -test_file=V2/Training_Set/35/test_7.json -save_model=V2/Log/35/training_7.model -top_num=100",
"python matrix2ltl.py -train_file=V2/Training_Set/35/training_8.json -test_file=V2/Training_Set/35/test_8.json -save_model=V2/Log/35/training_8.model -top_num=100",
"python matrix2ltl.py -train_file=V2/Training_Set/35/training_9.json -test_file=V2/Training_Set/35/test_9.json -save_model=V2/Log/35/training_9.model -top_num=100",
"python matrix2ltl.py -train_file=V2/Training_Set/35/training_10.json -test_file=V2/Training_Set/35/test_10.json -save_model=V2/Log/35/training_10.model -top_num=100"


]

i = 1
for command in commands:
    print("\n",i," 35秒 VAT 解析")
    os.system(command)
    i +=1


'''

90-10 的 20秒 VAT 学习
"python learn_ltl_matrix.py -train_file=V2/Training_Set/20/training_1.json -test_file=V2/Training_Set/20/training_1.json -save_model=V2/Log/20/training_1.model -log_file=V2/Log/20/training_1.log -res_file=V2/Log/20/training_1.txt -epoch_num=80",
"python learn_ltl_matrix.py -train_file=V2/Training_Set/20/training_2.json -test_file=V2/Training_Set/20/training_2.json -save_model=V2/Log/20/training_2.model -log_file=V2/Log/20/training_2.log -res_file=V2/Log/20/training_2.txt -epoch_num=80",
"python learn_ltl_matrix.py -train_file=V2/Training_Set/20/training_3.json -test_file=V2/Training_Set/20/training_3.json -save_model=V2/Log/20/training_3.model -log_file=V2/Log/20/training_3.log -res_file=V2/Log/20/training_3.txt -epoch_num=80",
"python learn_ltl_matrix.py -train_file=V2/Training_Set/20/training_4.json -test_file=V2/Training_Set/20/training_4.json -save_model=V2/Log/20/training_4.model -log_file=V2/Log/20/training_4.log -res_file=V2/Log/20/training_4.txt -epoch_num=80",
"python learn_ltl_matrix.py -train_file=V2/Training_Set/20/training_5.json -test_file=V2/Training_Set/20/training_5.json -save_model=V2/Log/20/training_5.model -log_file=V2/Log/20/training_5.log -res_file=V2/Log/20/training_5.txt -epoch_num=80",
"python learn_ltl_matrix.py -train_file=V2/Training_Set/20/training_6.json -test_file=V2/Training_Set/20/training_6.json -save_model=V2/Log/20/training_6.model -log_file=V2/Log/20/training_6.log -res_file=V2/Log/20/training_6.txt -epoch_num=80",
"python learn_ltl_matrix.py -train_file=V2/Training_Set/20/training_7.json -test_file=V2/Training_Set/20/training_7.json -save_model=V2/Log/20/training_7.model -log_file=V2/Log/20/training_7.log -res_file=V2/Log/20/training_7.txt -epoch_num=80",
"python learn_ltl_matrix.py -train_file=V2/Training_Set/20/training_8.json -test_file=V2/Training_Set/20/training_8.json -save_model=V2/Log/20/training_8.model -log_file=V2/Log/20/training_8.log -res_file=V2/Log/20/training_8.txt -epoch_num=80",
"python learn_ltl_matrix.py -train_file=V2/Training_Set/20/training_9.json -test_file=V2/Training_Set/20/training_9.json -save_model=V2/Log/20/training_9.model -log_file=V2/Log/20/training_9.log -res_file=V2/Log/20/training_9.txt -epoch_num=80",
"python learn_ltl_matrix.py -train_file=V2/Training_Set/20/training_10.json -test_file=V2/Training_Set/20/training_10.json -save_model=V2/Log/20/training_10.model -log_file=V2/Log/20/training_10.log -res_file=V2/Log/20/training_10.txt -epoch_num=80"

90-10 的 20秒 VAT 解析
"python matrix2ltl.py -train_file=V2/Training_Set/20/training_1.json -test_file=V2/Training_Set/20/test_1.json -save_model=V2/Log/20/training_1.model -top_num=100",
"python matrix2ltl.py -train_file=V2/Training_Set/20/training_2.json -test_file=V2/Training_Set/20/test_2.json -save_model=V2/Log/20/training_2.model -top_num=100",
"python matrix2ltl.py -train_file=V2/Training_Set/20/training_3.json -test_file=V2/Training_Set/20/test_3.json -save_model=V2/Log/20/training_3.model -top_num=100",
"python matrix2ltl.py -train_file=V2/Training_Set/20/training_4.json -test_file=V2/Training_Set/20/test_4.json -save_model=V2/Log/20/training_4.model -top_num=100",
"python matrix2ltl.py -train_file=V2/Training_Set/20/training_5.json -test_file=V2/Training_Set/20/test_5.json -save_model=V2/Log/20/training_5.model -top_num=100",
"python matrix2ltl.py -train_file=V2/Training_Set/20/training_6.json -test_file=V2/Training_Set/20/test_6.json -save_model=V2/Log/20/training_6.model -top_num=100",
"python matrix2ltl.py -train_file=V2/Training_Set/20/training_7.json -test_file=V2/Training_Set/20/test_7.json -save_model=V2/Log/20/training_7.model -top_num=100",
"python matrix2ltl.py -train_file=V2/Training_Set/20/training_8.json -test_file=V2/Training_Set/20/test_8.json -save_model=V2/Log/20/training_8.model -top_num=100",
"python matrix2ltl.py -train_file=V2/Training_Set/20/training_9.json -test_file=V2/Training_Set/20/test_9.json -save_model=V2/Log/20/training_9.model -top_num=100",
"python matrix2ltl.py -train_file=V2/Training_Set/20/training_10.json -test_file=V2/Training_Set/20/test_10.json -save_model=V2/Log/20/training_10.model -top_num=100"


All-All 的 20秒 VAT 学习
"python learn_ltl_matrix.py -train_file=All2All/20/training_1.json -test_file=All2All/20/training_1.json -save_model=All2All/20/training_1.model -log_file=All2All/20/training_1.log -res_file=All2All/20/training_1.txt -epoch_num=80",
"python learn_ltl_matrix.py -train_file=All2All/20/training_2.json -test_file=All2All/20/training_2.json -save_model=All2All/20/training_2.model -log_file=All2All/20/training_2.log -res_file=All2All/20/training_2.txt -epoch_num=80",
"python learn_ltl_matrix.py -train_file=All2All/20/training_3.json -test_file=All2All/20/training_3.json -save_model=All2All/20/training_3.model -log_file=All2All/20/training_3.log -res_file=All2All/20/training_3.txt -epoch_num=80",
"python learn_ltl_matrix.py -train_file=All2All/20/training_4.json -test_file=All2All/20/training_4.json -save_model=All2All/20/training_4.model -log_file=All2All/20/training_4.log -res_file=All2All/20/training_4.txt -epoch_num=80",
"python learn_ltl_matrix.py -train_file=All2All/20/training_5.json -test_file=All2All/20/training_5.json -save_model=All2All/20/training_5.model -log_file=All2All/20/training_5.log -res_file=All2All/20/training_5.txt -epoch_num=80",
"python learn_ltl_matrix.py -train_file=All2All/20/training_6.json -test_file=All2All/20/training_6.json -save_model=All2All/20/training_6.model -log_file=All2All/20/training_6.log -res_file=All2All/20/training_6.txt -epoch_num=80",
"python learn_ltl_matrix.py -train_file=All2All/20/training_7.json -test_file=All2All/20/training_7.json -save_model=All2All/20/training_7.model -log_file=All2All/20/training_7.log -res_file=All2All/20/training_7.txt -epoch_num=80",
"python learn_ltl_matrix.py -train_file=All2All/20/training_8.json -test_file=All2All/20/training_8.json -save_model=All2All/20/training_8.model -log_file=All2All/20/training_8.log -res_file=All2All/20/training_8.txt -epoch_num=80",
"python learn_ltl_matrix.py -train_file=All2All/20/training_9.json -test_file=All2All/20/training_9.json -save_model=All2All/20/training_9.model -log_file=All2All/20/training_9.log -res_file=All2All/20/training_9.txt -epoch_num=80",
"python learn_ltl_matrix.py -train_file=All2All/20/training_10.json -test_file=All2All/20/training_10.json -save_model=All2All/20/training_10.model -log_file=All2All/20/training_10.log -res_file=All2All/20/training_10.txt -epoch_num=80"


All-All 的 20秒 VAT 解析
"python matrix2ltl.py -train_file=All2All/20/training_10.json -test_file=All2All/20/test_10.json -save_model=All2All/20/training_10.model -top_num=100",
"python matrix2ltl.py -train_file=All2All/20/training_9.json -test_file=All2All/20/test_9.json -save_model=All2All/20/training_9.model -top_num=100",
"python matrix2ltl.py -train_file=All2All/20/training_8.json -test_file=All2All/20/test_8.json -save_model=All2All/20/training_8.model -top_num=100",
"python matrix2ltl.py -train_file=All2All/20/training_7.json -test_file=All2All/20/test_7.json -save_model=All2All/20/training_7.model -top_num=100",
"python matrix2ltl.py -train_file=All2All/20/training_6.json -test_file=All2All/20/test_6.json -save_model=All2All/20/training_6.model -top_num=100",
"python matrix2ltl.py -train_file=All2All/20/training_5.json -test_file=All2All/20/test_5.json -save_model=All2All/20/training_5.model -top_num=100",
"python matrix2ltl.py -train_file=All2All/20/training_4.json -test_file=All2All/20/test_4.json -save_model=All2All/20/training_4.model -top_num=100",
"python matrix2ltl.py -train_file=All2All/20/training_3.json -test_file=All2All/20/test_3.json -save_model=All2All/20/training_3.model -top_num=100",
"python matrix2ltl.py -train_file=All2All/20/training_2.json -test_file=All2All/20/test_2.json -save_model=All2All/20/training_2.model -top_num=100",
"python matrix2ltl.py -train_file=All2All/20/training_1.json -test_file=All2All/20/test_1.json -save_model=All2All/20/training_1.model -top_num=100“


All-One 的 20秒 VAT 学习
"python learn_ltl_matrix.py -train_file=All2One/20/training_1.json -test_file=All2One/20/training_1.json -save_model=All2One/20/training_1.model -log_file=All2One/20/training_1.log -res_file=All2One/20/training_1.txt -epoch_num=80",
"python learn_ltl_matrix.py -train_file=All2One/20/training_2.json -test_file=All2One/20/training_2.json -save_model=All2One/20/training_2.model -log_file=All2One/20/training_2.log -res_file=All2One/20/training_2.txt -epoch_num=80",
"python learn_ltl_matrix.py -train_file=All2One/20/training_3.json -test_file=All2One/20/training_3.json -save_model=All2One/20/training_3.model -log_file=All2One/20/training_3.log -res_file=All2One/20/training_3.txt -epoch_num=80",
"python learn_ltl_matrix.py -train_file=All2One/20/training_4.json -test_file=All2One/20/training_4.json -save_model=All2One/20/training_4.model -log_file=All2One/20/training_4.log -res_file=All2One/20/training_4.txt -epoch_num=80",
"python learn_ltl_matrix.py -train_file=All2One/20/training_5.json -test_file=All2One/20/training_5.json -save_model=All2One/20/training_5.model -log_file=All2One/20/training_5.log -res_file=All2One/20/training_5.txt -epoch_num=80",
"python learn_ltl_matrix.py -train_file=All2One/20/training_6.json -test_file=All2One/20/training_6.json -save_model=All2One/20/training_6.model -log_file=All2One/20/training_6.log -res_file=All2One/20/training_6.txt -epoch_num=80",
"python learn_ltl_matrix.py -train_file=All2One/20/training_7.json -test_file=All2One/20/training_7.json -save_model=All2One/20/training_7.model -log_file=All2One/20/training_7.log -res_file=All2One/20/training_7.txt -epoch_num=80",
"python learn_ltl_matrix.py -train_file=All2One/20/training_8.json -test_file=All2One/20/training_8.json -save_model=All2One/20/training_8.model -log_file=All2One/20/training_8.log -res_file=All2One/20/training_8.txt -epoch_num=80",
"python learn_ltl_matrix.py -train_file=All2One/20/training_9.json -test_file=All2One/20/training_9.json -save_model=All2One/20/training_9.model -log_file=All2One/20/training_9.log -res_file=All2One/20/training_9.txt -epoch_num=80",
"python learn_ltl_matrix.py -train_file=All2One/20/training_10.json -test_file=All2One/20/training_10.json -save_model=All2One/20/training_10.model -log_file=All2One/20/training_10.log -res_file=All2One/20/training_10.txt -epoch_num=80"

All-One 的 20秒 VAT 解析
"python matrix2ltl.py -train_file=All2One/20/training_10.json -test_file=All2One/20/test_10.json -save_model=All2One/20/training_10.model -top_num=100",
"python matrix2ltl.py -train_file=All2One/20/training_9.json -test_file=All2One/20/test_9.json -save_model=All2One/20/training_9.model -top_num=100",
"python matrix2ltl.py -train_file=All2One/20/training_8.json -test_file=All2One/20/test_8.json -save_model=All2One/20/training_8.model -top_num=100",
"python matrix2ltl.py -train_file=All2One/20/training_7.json -test_file=All2One/20/test_7.json -save_model=All2One/20/training_7.model -top_num=100",
"python matrix2ltl.py -train_file=All2One/20/training_6.json -test_file=All2One/20/test_6.json -save_model=All2One/20/training_6.model -top_num=100",
"python matrix2ltl.py -train_file=All2One/20/training_5.json -test_file=All2One/20/test_5.json -save_model=All2One/20/training_5.model -top_num=100",
"python matrix2ltl.py -train_file=All2One/20/training_4.json -test_file=All2One/20/test_4.json -save_model=All2One/20/training_4.model -top_num=100",
"python matrix2ltl.py -train_file=All2One/20/training_3.json -test_file=All2One/20/test_3.json -save_model=All2One/20/training_3.model -top_num=100",
"python matrix2ltl.py -train_file=All2One/20/training_2.json -test_file=All2One/20/test_2.json -save_model=All2One/20/training_2.model -top_num=100",
"python matrix2ltl.py -train_file=All2One/20/training_1.json -test_file=All2One/20/test_1.json -save_model=All2One/20/training_1.model -top_num=100"

'''