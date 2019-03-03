import random
import json
import constants

# history_tasks = dict from datastore


def read_json(file_in):
    '''
    (str) -> dict

    str - history.json or discreth.json
    Return dictionary where key isquestion and value
    tuple of two values: right answer and tuple of all possible answers
    '''
    json_file = open(file_in)
    json_data = json.loads(json_file.read())
    json_file.close()
    return json_data


def choose_question(tasks):
    """
    (dict) -> str, tuple

    Return random name of question and tiple with its options
    """
    chosen_question = random.choice(
        list(question for question in tasks.keys()))
    question_options = tasks[chosen_question][1]
    return chosen_question, question_options, tasks[chosen_question][0]


def correct_answer(answer, quest_options):
    """
    (str, tuple) -> bool

    Rreturn if chosen option is true or false
    """
    bad_result = ''
    if answer == quest_options:
        if constants.gl_chosen_sub == "../src/datastorage/history.json":
            constants.DJEJORYKY +=15
        elif constants.gl_chosen_sub == "../src/datastorage/discret.json":
            constants.SHCERBYNCHYKY +=15
        return " - це првильна відповідь!✅✅✅"
    else:
        if constants.gl_chosen_sub == "../src/datastorage/history.json":
            constants.DJEJORYKY -=10
        elif constants.gl_chosen_sub == "../src/datastorage/discret.json":
            constants.SHCERBYNCHYKY -=10
        bad_result = "\n🆘🆘🆘на жаль, це не првильна відповідь.🆘🆘🆘\n✅✅✅ Правильно - " + answer + "✅✅✅"
        return bad_result


def run_question(json_file):
    """
    (string) -> function(dict)

    Get signal from user, return
    """
    sub_tasks = read_json(json_file)
    return choose_question(sub_tasks)
