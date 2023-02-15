import pprint
import json
from docx2python import docx2python


def read_engene(file_path):
    input_text = []
    json_result = []
    doc_result = docx2python(file_path)  # start collecting data from file
    for x in range(len(doc_result.body[0][0][0])):  # cycle count records
        input_text.append(doc_result.body[0][0][0][x])
        item_name_raw = str(doc_result.body[0][0][0][x])  # collecting text with special symbols
        json_structure_lvl = 0  # указываем уровень вложености
        json_element_id = "id" + str(x)  # даём каждому элементу уникальный индекс.
        item_name_clean = item_name_raw.replace('--\t', '')  # отчищаем строчку от --\t
        search_index_item_name_clean = item_name_clean.find("\t")  # ищем первое вхождение  вхождений \t
        while search_index_item_name_clean >= 0:  # по количеству \t определяем степень вложености  + чистим от \t
            item_name_clean = item_name_clean.replace('\t', '', 1)
            search_index_item_name_clean = item_name_clean.find("\t")
            json_structure_lvl = json_structure_lvl + 1
        json_result_temp = {
            "Name": item_name_clean,
            "id": json_element_id,
            "lvl": json_structure_lvl,
        }
        json_result.append(json_result_temp)
    print(json_result)
    return json_result

#   take ID and list of records and
#   return list of records in dictionary
def search_engene(id_target,json_result):
    lvl_parent = 0
    id_search_index = 0
    search_engene_result = []
    # searching targeting "id" and saving index
    for x in range(len(json_result)):
        if json_result[x]["id"] == id_target:
            id_search_index = x
            lvl_parent = json_result[x]["lvl"]
    id_search_index = id_search_index + 1  # going to next record
    for x in range(len(json_result) - id_search_index):  # going thru remaning records
        if json_result[id_search_index]["lvl"] == lvl_parent:  # if ends current parent = break
            break
        if json_result[id_search_index]["lvl"] == lvl_parent + 1:  # getting targeting records
            search_engene_result.append(json_result[id_search_index])
        id_search_index = id_search_index + 1  # next record
    pass
    return search_engene_result

def search_prev_element(id_target,json_result):
    ret= ""
    for x in range(len(json_result)):
        if json_result[x]["id"] == id_target:
            lvl_current = json_result[x]["lvl"]
            for y in reversed(range(x)):  # search back
                if json_result[y]["lvl"] == lvl_current - 1:  # if lvl decrise  = break
                    ret = json_result[y]["id"]
                    break
            break
    return ret