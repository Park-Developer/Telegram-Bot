import json
json_addr = 'C:\\Users\\gnvid\\PycharmProjects\\telegramBot\\stock_list.json'
with open(json_addr, 'r', encoding='UTF8') as f:
    json_data = json.load(f)

#print(json_data['Stock List'])

saved_stock_list=[]
print("json_data['Stock List']",json_data['Stock List'])
print(type(json_data['Stock List']))
print(json_data['Stock List'][0])
asd=json_data['Stock List'][0]
print(asd.values())
print(list(asd.values())[0])

print(type(list(asd.values())[0]))
for saved_stock in json_data['Stock List']:
    saved_stock_list.append(list(saved_stock.keys())[0])

print(saved_stock_list)