import json
import os


file_path = './oxford5k_qimages.json'
path = './'
with open(file_path, 'r', encoding='utf-8') as f:
    try:
        load_dict = json.load(f)
        # load_dict = [str(x) for x in load_dict]
        for i in range(len(load_dict)):
            print(load_dict[i])
            # print(type(load_dict[i]))
            os.popen('cp %s %s'%(load_dict[i],path))

    except:
        f.close()
