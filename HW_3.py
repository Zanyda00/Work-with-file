dict_len_files = {}
with open('1.txt', 'r', encoding='utf-8') as f:
    file_1 = f.readlines()
    dict_len_files.update({'1.txt': len(file_1)})

with open('2.txt', 'r', encoding='utf-8') as f:
    file_2 = f.readlines()
    dict_len_files.update({'2.txt': len(file_2)})

with open('3.txt', 'r', encoding='utf-8') as f:
    file_3 = f.readlines()
    dict_len_files.update({'3.txt': len(file_3)})

sorted_tuple_len_file = sorted(dict_len_files.items(), key=lambda x: x[1])
sorted_dict_len_file = {k: v for k, v in sorted_tuple_len_file}


