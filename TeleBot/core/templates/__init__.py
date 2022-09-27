from .main import init_project, add_new_key


command_map = {
    'init': init_project,
    'addkey': add_new_key
}


def handel_commands(arguments: list):
    command = arguments[0]
    command_arguments = arguments[1:]
    if command in command_map.keys():
        command_map[command](command_arguments)
