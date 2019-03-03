# -*- coding: utf-8 -*-
import json

history_tasks = {}

with open('history.json', 'w') as fp:
    json.dump(history_tasks, fp)
