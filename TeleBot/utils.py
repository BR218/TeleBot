import pathlib
import os
from typing import List

PROJECT_PATH = os.path.abspath('.')
MODULE_PATH = pathlib.Path(__file__).parent


def get_params(param_list: List[str]):
    params = []
    if param_list:
        for param in param_list:
            if '--' in param:
                option = param.replace('--', '')
                params.append(option)
            else:
                break
    return params
