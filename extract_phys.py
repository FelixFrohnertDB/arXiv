import json
import re 

cnt_surprise = 0 
cnt_quant = 0 
del_arr = ['submitter','authors', 'comments', 'journal-ref', 'doi', 'report-no', 'license', 'versions', 'update_date', 'authors_parsed']


with open('arxiv.csv','w', newline='') as file:
    for line in open("/home/felix/vscodeProjects/arXiv/archive/arxiv-metadata-oai-snapshot.json", 'r'): 

        temp = json.loads(line) 
        if "quant" in temp["categories"]:
            # if any(ext in temp["abstract"] for ext in indicator_arr):
            for del_item in del_arr:
                del temp[del_item]

            save_txt = "{},{},{}".format(str(temp["id"]),re.sub("[^A-Za-z']+", ' ', str(temp["title"])).lower(),re.sub("[^A-Za-z']+", ' ', str(temp["abstract"])).lower()  )

            file.write(save_txt)
            file.write('\n')

             
            cnt_quant += 1 
print(cnt_quant)