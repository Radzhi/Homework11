import json

__data = []


def load_candidates_from_json(path):
    """Возвращает список всех кандидатов"""
    global __data
    with open(path, 'r', encoding='utf-8') as file:
        __data = json.load(file)
    return __data


def get_candidate(candidate_id):
    """Возвращает одного кандидата по его id"""
    for candidate in __data:
        if candidate['id'] == candidate_id:
            return {
                'name': candidate['name'],
                'position': candidate['position'],
                'picture': candidate['picture'],
                'skills': candidate['skills']
            }
    return {'not found': 'Ушел на обед'}


def get_candidates_by_name(candidate_name):
    """Возвращает кандидатов по имени"""
    return [candidate for candidate in __data if candidate_name.lower() in
            candidate['name'].lower()]



def get_candidates_by_skill(skill_name):
    """Возвращает кандидатов по навыку"""
    results = []
    for candidate in __data:
        if skill_name in candidate['skills'].lower():
            results.append(candidate)
    return results
