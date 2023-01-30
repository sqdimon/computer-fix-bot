import pprint
import json
from docx2python import docx2python

json_result = []
# start collecting data from file
doc_result = docx2python('diagram.docx')
input_text = []
for x in range(len(doc_result.body[0][0][0])):
    input_text.append(doc_result.body[0][0][0][x])
    item_name_raw = str(doc_result.body[0][0][0][x])
    json_structure_lvl = 0                                          # указываем уровень вложености
    json_element_id = "id" + str(x)                                 # даём каждому элементу уникальный индекс.
    item_name_clean = item_name_raw.replace('--\t','')              # отчищаем строчку от --\t
    search_index_item_name_clean = item_name_clean.find("\t")       # ищем первое вхождение  вхождений \t
    while search_index_item_name_clean >=0:                         # по количеству \t определяем степень вложености  + чистим от \t
        item_name_clean = item_name_clean.replace('\t', '',1)
        search_index_item_name_clean = item_name_clean.find("\t")
        json_structure_lvl = json_structure_lvl + 1
    json_result_temp = {
        "Name":item_name_clean,
        "id":json_element_id,
        "lvl":json_structure_lvl,
    }
    json_result.append(json_result_temp)
print(json_result)
# end
# Search engine
# set target lvl # set searching id
def search_engene (lvl_target,id_target):
    lvl_parent = 0
    id_search_index = 0
    # searching targeting "id" and saving index
    for x in range(len(json_result)):
        if json_result[x]["id"] == id_target:
            id_search_index = x
            lvl_parent = json_result[x]["lvl"]
    id_search_index = id_search_index + 1                       # going to next record
    for x in range(len(json_result)-id_search_index):           # going thru remaning records
        if json_result[id_search_index]["lvl"] == lvl_parent:   # if ends current parent = break
            break
        if json_result[id_search_index]["lvl"] == lvl_target:   # getting targeting records
            print(json_result[id_search_index])
        id_search_index = id_search_index + 1                   # next record
    pass

search_engene(4,"id33")

#json_print_temp  = json.dumps(json_result,indent=4,ensure_ascii=False)
#print(json_print_temp)


