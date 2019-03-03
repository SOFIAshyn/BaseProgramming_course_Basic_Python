import json
from constants import leaderboard_path, courses_dict


def get_leaderboard():
    '''
    Returns dictionary from json file
    in leaderboard_path directory
    '''
    with open(leaderboard_path) as leaderboard:
        data = json.load(leaderboard)
        return data


def meanscore(leaderboard_item):
    # used in sorting by mean of scores
    return (sum(leaderboard_item[1]) / len(leaderboard_item[1]))


def sort_leaderboard(data):
    '''
    sort by mean
    (dict) -> list
    '''
    return sorted(data.items(), key=(meanscore), reverse=True)


def add_record(user_id, points, course, skip_points=0):
    '''
    (str, int, str)
    Adds new record in a leaderboard
    e.g.
    add_record("woman", 25, "history")
    '''
    data = get_leaderboard()
    if course not in courses_dict.keys():
        return None
    if (user_id in data.keys()):
        data[user_id][courses_dict[course]] += (points - skip_points)
    else:
        data[user_id] = [0] * (len(courses_dict.keys()) + 1)
        data[user_id][courses_dict[course]] += (points - skip_points)

    with open(leaderboard_path, 'w') as f:
        json.dump(data, f)


def get_sorted_leaderboard():
    # returns list of players sorted by mean score
    return sort_leaderboard(get_leaderboard())
