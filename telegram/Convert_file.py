import pprint
import json

from docx2python import docx2python
doc_result = docx2python('diagram.docx')

xx = len(doc_result.body[0][0][0])
#print(xx)
"""
{
"Name": "Чат бот"
"Item": "item0" 
"lvl": 0
"next": [{
    "Name": "Комьютер железо"
    "Item": "item1" 
    "lvl": 1
    "next": {[
            "Name": "Не включается, нет признаков жизни"
            "Item": "item3" 
            "lvl": 2
            "next": {[
                ...
                ]}
            ...
            ]}
    ...
    },{
    "Name": "Windows"
    "Item": "item..." 
    "lvl": 1
    "next": [{
    ...}]
    }]       
}
"""
json_result = []
#print(type(json_result))
input_text = []
json_last = json_result
ind = 0 # отступ при выводе
for x in range(len(doc_result.body[0][0][0])):

    input_text.append(doc_result.body[0][0][0][x])
    item_name_raw = str(doc_result.body[0][0][0][x])

    # указываем уровень вложености
    json_structure_lvl = 0

    # даём каждому элементу уникальный индекс.
    json_element_id = "id" + str(x)

    # отчищаем строчку от --\t
    item_name_clean = item_name_raw.replace('--\t','')

    # ищем первое вхождение  вхождений \t
    search_index_item_name_clean = item_name_clean.find("\t")

    # по количеству \t определяем степень вложености  + чистим от \t
    while search_index_item_name_clean >=0:
        item_name_clean = item_name_clean.replace('\t', '',1)
        search_index_item_name_clean = item_name_clean.find("\t")
        json_structure_lvl = json_structure_lvl + 1
    json_result_temp = {
        "Name":item_name_clean,
        "id":json_element_id,
        "lvl":json_structure_lvl,
        "prev": int,
        "next": int
    }
    # x- id текущего элемента
    # lvl - глубина

    json_result.append(json_result_temp)

    # lvl difference

    dif = json_result[x]["lvl"]-json_result[x-1]["lvl"]
    #print(dif)
    if ( dif > 0 ):
       json_result[x-1]["next"] = json_result[x]["id"]
       # json_result[x-1]["next"].append(json_result[x]["id"])

    if (json_result[x]["lvl"]==json_result[x-1]["lvl"]):
        gap = json_result[x]["lvl"]==json_result[x-1]["lvl"]
        json_result[x-1]["next"] = json_result[x]["id"]

    #print(json_result[x-1]["next"])
    #print(json_result[x]["id"])

    # формируем отступы
    ind = 4 * (json_result[x]["lvl"])

    #json_print_temp = json.dumps(json_result_temp, indent=ind, ensure_ascii=False)
    #print(json_print_temp)

    #print(json_result[x]["lvl"])
    #print(json_result[x-1]["lvl"])
    #print("************************")
"""
    if json_structure_lvl == 0:
        json_result.json_result_temp # Записали первый элемент в структуру
        #json_last = json_result
    else:
        #json_result_temp["prev"] = int(id(json_last))
        #json_result.append(json_result_temp)
        #json_last["next"] = json_result_temp # все последующие элементы будут идти в субсписок'''
        #json_last = json_last["next"]
        #print("prev: ",type(id(json_last)))
        #print("next: ",type(id(json_last)))
    #json_print_temp  = json.dumps(json_result,indent=1,ensure_ascii=False)
    #print(json_print_temp)
    #print(json_result)
    
    """
print(json_result)

# Search engine
lvl_target = 5      # set target lvl
id_target = "id33"  # set searching id

lvl_parent = 0
id_search_index = 0

# searching targeting "id" and saving index
for x in range(len(json_result)):
    if json_result[x]["id"] == id_target:
        #print(x)
        id_search_index = x
        lvl_parent = json_result[x]["lvl"]
        #print(json_result[x])
id_search_index = id_search_index + 1                       # going to next record
for x in range(len(json_result)-id_search_index):           # going thru remaning records
    if json_result[id_search_index]["lvl"] == lvl_parent:   # if ends current parent = break
        break
    if json_result[id_search_index]["lvl"] == lvl_target:   # getting targeting records
        print(json_result[id_search_index])
    id_search_index = id_search_index + 1                   # next record


#json_print_temp  = json.dumps(json_result,indent=4,ensure_ascii=False)
#print(json_print_temp)


