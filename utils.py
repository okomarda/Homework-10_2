import json
#загрузка модуля оыщт

file_json = "candidates.json"

def load_candidates(file_json):
    """Функция, позволяющая загрузить данные из файла с расширением json"""
    with open(file_json, "r", encoding = "utf-8") as f:
        data_candidates = json.load(f)

        return data_candidates

def get_candidate_by_id(candidate_id):
    """Функция, позволяющая выгрузить данные кандидатов по порядковому номеру"""
    data_cand = load_candidates(file_json)
    for cand in data_cand:
        if cand["id"] == candidate_id:
            return cand
    return

def get_candidates_by_name(candidate_name):
    """Функция, позволяющая выгрузить данные кандидатов по имени"""
    data_cand = load_candidates(file_json)
    for cand in data_cand:
        if cand["name"] == candidate_name:
            return cand
    return

def get_candidates_by_first_name(candidate_name):
    """Функция, позволяющая выгрузить данные кандидатов по имени"""
    data_cand = load_candidates(file_json)
    equal_names = []
    for cand in data_cand:
        if candidate_name.lower() in cand["name"].lower().split(" "):
            equal_names.append(cand["name"])
    return equal_names

def get_candidates_by_skill(skill_name):
    """Функция, позволяющая выгрузить данные кандидатов по навыку"""
    data_cand = load_candidates (file_json)
    cand_skill_list = []

    for cand in data_cand:
       if skill_name.lower() in cand["skills"].lower().split(", "):
           cand_skill_list.append(cand)

    return cand_skill_list