import json


def load_candidates_from_json() -> list[dict]:
    """
    Функция возвращает список кандидатов из файла candidates.json
    :param
    :return:
    """
    with open('candidates.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data


def get_candidate(candidate_id: int) -> dict:
    """
    Функция достает кандидата из списка по id
    :param candidate_id:
    :return:
    """
    for candidate in load_candidates_from_json():
        if candidate['id'] == candidate_id:
            return candidate


def get_candidates_by_name(candidate_name: str) -> list[dict]:
    result = []
    for candidate in load_candidates_from_json():
        if candidate['name'] == candidate_name:
            result.append(candidate)
    return result


def get_candidates_by_skill(skill_name: str) -> list[dict]:
    result = []
    for candidate in load_candidates_from_json():
        if skill_name in candidate['skills'].lower().split(', '):
            result.append(candidate)
    return result

