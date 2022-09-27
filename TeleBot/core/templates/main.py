from .template import Template
from ..crypto import generate_key
from ...utils import get_params


def init_project(arguments: list = None):
    additional_options = get_params(arguments)
    dir_tree = [
        'settings', 'settings/config',
        'handlers', 'handlers/commands', 'handlers/forms', 'handlers/text',
        'modules'
    ]

    if 'force' in additional_options: force_create = True
    else: force_create = False

    template = Template(force_create=force_create)
    template.add_dirs(dir_tree)
    template.add_file('main.py')
    template.add_file('__init__.py', relative_path=['handlers'])
    template.add_file('base.py', relative_path=['handlers'])
    template.add_file('__init__.py', relative_path=['handlers', 'commands'])
    template.add_file('help.py', relative_path=['handlers', 'commands'])
    template.add_file('start.py', relative_path=['handlers', 'commands'])
    template.copy_file('.gitignore')
    template.create_file(generate_key(), '.key', relative_path=['settings'])
    template()


def add_new_key(arguments: list = None):
    template = Template(force_create=True)
    relative_path = ['settings']
    additional_options = get_params(arguments)
    if not additional_options:
        help_text = "Please supply any additional flag from below:" \
                    "\n\t--new\tGenerate new key" \
                    "\n\t--force\tDon't confirm your action"
        print(help_text)
    if 'new' in additional_options:
        if 'force' in additional_options:
            template.create_file(generate_key(), '.key', relative_path=relative_path)
            print('New key generated successfully')
        else:
            inp_text = f"It will override previous key.\n" \
                       f"You won\'t be able to use previously saved crediantials[if any]\n" \
                       f"Are you still want to override previous key? [y/n]: "
            aggree = input(inp_text)
            if 'y' in aggree.lower():
                template.create_file(generate_key(), '.key', relative_path=relative_path)
                print('New key generated successfully')
            else:
                print('Aborted action, key remains same..')


def add_command(arguments: list = None):
    pass
