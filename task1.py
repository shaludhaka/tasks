import json
final_result = {}

def get_values(prefix,data):
    prefix = prefix
    if type(data) != list:
        quantity = data.get("quantity")
        final_result.setdefault(prefix + "-" + str(quantity), []).append(quantity * .23)
        final_result.setdefault(prefix + "-" + str(quantity), []).append(quantity * .5)
        final_result.setdefault(prefix + "-" + str(quantity), []).append(quantity * 2.6)
        return final_result
    if type(data) == list:
        for element in data:
            for key,value in element.items():
                prefix = key
                get_values(prefix,value)

json_data = open('data.json').read()
data  = json.loads(json_data)
data_100gm = data.get('data').get("100gm")

for key,value in data_100gm.items():
    for item in value:
        for k,v in item.items():
            try:
                final_data = get_values(k,v)
            except Exception as e:
                 pass

print final_data
#IT will print the final data in dictionary format where key is the qunatity with prefix to be coverted into 23,50 and 260 gm
#respectively and value is the list of converted value for ex : if key is Betaine-67.60326 then Betaine is key under which 'quantity'
# 67.60326 is present and value is a list[67.60326*.23,67.60326*.5,67.60326*2.6]
# <type 'list'>: [15.548749800000001, 33.80163, 175.76847600000002]