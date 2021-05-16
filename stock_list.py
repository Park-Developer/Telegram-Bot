import json
with open('C:\\Users\\gnvid\\PycharmProjects\\telegramBot\\stock_list.json', 'r', encoding='UTF8') as f:

    json_data = json.load(f)
print(json_data)



with open('test.json','w',encoding="utf-8") as make_file:
    json.dump(json_data,make_file,ensure_ascii=False,indent='\t')