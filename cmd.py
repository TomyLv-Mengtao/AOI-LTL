import os

commands = [



"python matrix2ltl.py -train_file=5Sec/All2All/training_10.json -test_file=5Sec/All2All/test_10.json -save_model=5Sec/All2All/training_10.model -top_num=100",
"python matrix2ltl.py -train_file=5Sec/All2All/training_9.json -test_file=5Sec/All2All/test_9.json -save_model=5Sec/All2All/training_9.model -top_num=100",
"python matrix2ltl.py -train_file=5Sec/All2All/training_8.json -test_file=5Sec/All2All/test_8.json -save_model=5Sec/All2All/training_8.model -top_num=100",
"python matrix2ltl.py -train_file=5Sec/All2All/training_7.json -test_file=5Sec/All2All/test_7.json -save_model=5Sec/All2All/training_7.model -top_num=100",
"python matrix2ltl.py -train_file=5Sec/All2All/training_6.json -test_file=5Sec/All2All/test_6.json -save_model=5Sec/All2All/training_6.model -top_num=100",
"python matrix2ltl.py -train_file=5Sec/All2All/training_5.json -test_file=5Sec/All2All/test_5.json -save_model=5Sec/All2All/training_5.model -top_num=100",
"python matrix2ltl.py -train_file=5Sec/All2All/training_4.json -test_file=5Sec/All2All/test_4.json -save_model=5Sec/All2All/training_4.model -top_num=100",
"python matrix2ltl.py -train_file=5Sec/All2All/training_3.json -test_file=5Sec/All2All/test_3.json -save_model=5Sec/All2All/training_3.model -top_num=100",
"python matrix2ltl.py -train_file=5Sec/All2All/training_2.json -test_file=5Sec/All2All/test_2.json -save_model=5Sec/All2All/training_2.model -top_num=100",
"python matrix2ltl.py -train_file=5Sec/All2All/training_1.json -test_file=5Sec/All2All/test_1.json -save_model=5Sec/All2All/training_1.model -top_num=100",
"python matrix2ltl.py -train_file=5Sec/All2All/training_20.json -test_file=5Sec/All2All/test_20.json -save_model=5Sec/All2All/training_20.model -top_num=100",
"python matrix2ltl.py -train_file=5Sec/All2All/training_19.json -test_file=5Sec/All2All/test_19.json -save_model=5Sec/All2All/training_19.model -top_num=100",
"python matrix2ltl.py -train_file=5Sec/All2All/training_18.json -test_file=5Sec/All2All/test_18.json -save_model=5Sec/All2All/training_18.model -top_num=100",
"python matrix2ltl.py -train_file=5Sec/All2All/training_17.json -test_file=5Sec/All2All/test_17.json -save_model=5Sec/All2All/training_17.model -top_num=100",
"python matrix2ltl.py -train_file=5Sec/All2All/training_16.json -test_file=5Sec/All2All/test_16.json -save_model=5Sec/All2All/training_16.model -top_num=100",
"python matrix2ltl.py -train_file=5Sec/All2All/training_15.json -test_file=5Sec/All2All/test_15.json -save_model=5Sec/All2All/training_15.model -top_num=100",
"python matrix2ltl.py -train_file=5Sec/All2All/training_14.json -test_file=5Sec/All2All/test_14.json -save_model=5Sec/All2All/training_14.model -top_num=100",
"python matrix2ltl.py -train_file=5Sec/All2All/training_13.json -test_file=5Sec/All2All/test_13.json -save_model=5Sec/All2All/training_13.model -top_num=100",
"python matrix2ltl.py -train_file=5Sec/All2All/training_12.json -test_file=5Sec/All2All/test_12.json -save_model=5Sec/All2All/training_12.model -top_num=100",
"python matrix2ltl.py -train_file=5Sec/All2All/training_11.json -test_file=5Sec/All2All/test_11.json -save_model=5Sec/All2All/training_11.model -top_num=100",
"python matrix2ltl.py -train_file=5Sec/All2All/training_30.json -test_file=5Sec/All2All/test_30.json -save_model=5Sec/All2All/training_30.model -top_num=100",
"python matrix2ltl.py -train_file=5Sec/All2All/training_29.json -test_file=5Sec/All2All/test_29.json -save_model=5Sec/All2All/training_29.model -top_num=100",
"python matrix2ltl.py -train_file=5Sec/All2All/training_28.json -test_file=5Sec/All2All/test_28.json -save_model=5Sec/All2All/training_28.model -top_num=100",
"python matrix2ltl.py -train_file=5Sec/All2All/training_27.json -test_file=5Sec/All2All/test_27.json -save_model=5Sec/All2All/training_27.model -top_num=100",
"python matrix2ltl.py -train_file=5Sec/All2All/training_26.json -test_file=5Sec/All2All/test_26.json -save_model=5Sec/All2All/training_26.model -top_num=100",
"python matrix2ltl.py -train_file=5Sec/All2All/training_25.json -test_file=5Sec/All2All/test_25.json -save_model=5Sec/All2All/training_25.model -top_num=100",
"python matrix2ltl.py -train_file=5Sec/All2All/training_24.json -test_file=5Sec/All2All/test_24.json -save_model=5Sec/All2All/training_24.model -top_num=100",
"python matrix2ltl.py -train_file=5Sec/All2All/training_23.json -test_file=5Sec/All2All/test_23.json -save_model=5Sec/All2All/training_23.model -top_num=100",
"python matrix2ltl.py -train_file=5Sec/All2All/training_22.json -test_file=5Sec/All2All/test_22.json -save_model=5Sec/All2All/training_22.model -top_num=100",
"python matrix2ltl.py -train_file=5Sec/All2All/training_21.json -test_file=5Sec/All2All/test_21.json -save_model=5Sec/All2All/training_21.model -top_num=100",
"python matrix2ltl.py -train_file=5Sec/All2All/training_40.json -test_file=5Sec/All2All/test_40.json -save_model=5Sec/All2All/training_40.model -top_num=100",
"python matrix2ltl.py -train_file=5Sec/All2All/training_39.json -test_file=5Sec/All2All/test_39.json -save_model=5Sec/All2All/training_39.model -top_num=100",
"python matrix2ltl.py -train_file=5Sec/All2All/training_38.json -test_file=5Sec/All2All/test_38.json -save_model=5Sec/All2All/training_38.model -top_num=100",
"python matrix2ltl.py -train_file=5Sec/All2All/training_37.json -test_file=5Sec/All2All/test_37.json -save_model=5Sec/All2All/training_37.model -top_num=100",
"python matrix2ltl.py -train_file=5Sec/All2All/training_36.json -test_file=5Sec/All2All/test_36.json -save_model=5Sec/All2All/training_36.model -top_num=100",
"python matrix2ltl.py -train_file=5Sec/All2All/training_35.json -test_file=5Sec/All2All/test_35.json -save_model=5Sec/All2All/training_35.model -top_num=100",
"python matrix2ltl.py -train_file=5Sec/All2All/training_34.json -test_file=5Sec/All2All/test_34.json -save_model=5Sec/All2All/training_34.model -top_num=100",
"python matrix2ltl.py -train_file=5Sec/All2All/training_33.json -test_file=5Sec/All2All/test_33.json -save_model=5Sec/All2All/training_33.model -top_num=100",
"python matrix2ltl.py -train_file=5Sec/All2All/training_32.json -test_file=5Sec/All2All/test_32.json -save_model=5Sec/All2All/training_32.model -top_num=100",
"python matrix2ltl.py -train_file=5Sec/All2All/training_31.json -test_file=5Sec/All2All/test_31.json -save_model=5Sec/All2All/training_31.model -top_num=100",
"python matrix2ltl.py -train_file=5Sec/All2All/training_50.json -test_file=5Sec/All2All/test_50.json -save_model=5Sec/All2All/training_50.model -top_num=100",
"python matrix2ltl.py -train_file=5Sec/All2All/training_49.json -test_file=5Sec/All2All/test_49.json -save_model=5Sec/All2All/training_49.model -top_num=100",
"python matrix2ltl.py -train_file=5Sec/All2All/training_48.json -test_file=5Sec/All2All/test_48.json -save_model=5Sec/All2All/training_48.model -top_num=100",
"python matrix2ltl.py -train_file=5Sec/All2All/training_47.json -test_file=5Sec/All2All/test_47.json -save_model=5Sec/All2All/training_47.model -top_num=100",
"python matrix2ltl.py -train_file=5Sec/All2All/training_46.json -test_file=5Sec/All2All/test_46.json -save_model=5Sec/All2All/training_46.model -top_num=100",
"python matrix2ltl.py -train_file=5Sec/All2All/training_45.json -test_file=5Sec/All2All/test_45.json -save_model=5Sec/All2All/training_45.model -top_num=100",
"python matrix2ltl.py -train_file=5Sec/All2All/training_44.json -test_file=5Sec/All2All/test_44.json -save_model=5Sec/All2All/training_44.model -top_num=100",
"python matrix2ltl.py -train_file=5Sec/All2All/training_43.json -test_file=5Sec/All2All/test_43.json -save_model=5Sec/All2All/training_43.model -top_num=100",
"python matrix2ltl.py -train_file=5Sec/All2All/training_42.json -test_file=5Sec/All2All/test_42.json -save_model=5Sec/All2All/training_42.model -top_num=100",
"python matrix2ltl.py -train_file=5Sec/All2All/training_41.json -test_file=5Sec/All2All/test_41.json -save_model=5Sec/All2All/training_41.model -top_num=100"


]

i = 1
for command in commands:
    print("\n",i,"All-All 的 5秒 VAT 解析")
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