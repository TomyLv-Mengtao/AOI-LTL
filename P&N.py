#!/us/bin/env/ python
# encoding: utf-8

"""
@author: Mengtao Lyu (Tomy Lv) 
@contact: mengtao.lyu@connect.polyu.hk
@file: P&N.py.py
@time: 10/5/2024 2:50 pm
@desc:
"""
#!/us/bin/env/ python
# encoding: utf-8

"""
@author: Mengtao Lyu (Tomy Lv) 
@contact: mengtao.lyu@connect.polyu.hk
@file: Pos_Neg.py.py
@time: 10/5/2024 2:15 pm
@desc:
"""

import json
import glob
import os

def switch_labels(directory):
    # Search for all JSON files in the given directory
    file_pattern = os.path.join(directory, '*.json')
    json_files = glob.glob(file_pattern)

    for file_path in json_files:
        # Load the JSON data from file
        with open(file_path, 'r') as file:
            data = json.load(file)
        print(file_path)
        # Swap 'traces_pos' and 'traces_neg'
        data['traces_pos'], data['traces_neg'] = data['traces_neg'], data['traces_pos']

        # Save the modified data back to the same file
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)

# Define the directory containing the JSON files
directory = '25iles/2ndRnd/All2All/40'
switch_labels(directory)
