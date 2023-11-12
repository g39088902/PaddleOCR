import random
input_file = "../train_data/202311121026/Label.txt"
ouput_path = "../train_data/202311121026/"
input = open(input_file, 'r', encoding='utf-8')
train_set = open(f"{ouput_path}/train.txt".format(ouput_path=ouput_path), 'w', encoding='utf-8')
eval_set = open(f"{ouput_path}/eval.txt".format(ouput_path=ouput_path), 'w', encoding='utf-8')
input_list = input.readlines()
random.shuffle(input_list)
train_num = int(len(input_list) * 0.85)
train_list = input_list[:train_num]
eval_list = input_list[train_num:]
for line in train_list:
    train_set.write(line)
for line in eval_list:
    eval_set.write(line)
train_set.close()
eval_set.close()
input.close()
print("train.txt and eval.txt are generated successfully!")