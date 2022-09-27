from os import mkdir, chdir
from os.path import join, exists
from time import strftime

from jinja2 import Environment, FileSystemLoader, select_autoescape

from ... import __version__
from ...utils import PROJECT_PATH, MODULE_PATH


class Template:
    def __init__(self, root_path=None, project_name=None, force_create=False):
        self.template_path = join(MODULE_PATH, 'core', 'templates', 'static')
        self.env = Environment(
            loader=FileSystemLoader(self.template_path),
            autoescape=select_autoescape(default=True)
        )

        self.header = {
            'datetime': strftime('%A, %d %b %Y %I:%M:%S %p %Z'),
            'version': __version__,
            'project': project_name
        }
        self.file_meta_list = []
        self.force_create = force_create
        if root_path:
            self.user_project_path = join(PROJECT_PATH, root_path)
        else:
            self.user_project_path = PROJECT_PATH

    @staticmethod
    def add_dirs(directory_tree):
        for dir_name in directory_tree:
            try:
                mkdir(dir_name)
            except FileExistsError:
                pass
            except Exception as e:
                print(e)

    def add_file(self, file_name: str, file_vars: dict = None, relative_path: list = None):
        if file_vars is None:
            file_vars = {}
        file_meta = (file_name, file_vars, relative_path)
        self.file_meta_list.append(file_meta)

    def check_dir_or_create(self, path_list: list):
        full_path = join(self.user_project_path, *path_list)
        if not exists(full_path):
            try:
                chdir(self.user_project_path)
                for path in path_list:
                    mkdir(path)
                    chdir(path)
            except Exception:
                raise Exception('Folder creation failed')

    def get_file_data(self, file_name: str, additional_data: dict, relative_path: list = None, **kwargs):
        if relative_path:
            file_name = join(*relative_path, file_name)
        template = self.env.get_template(file_name)
        data = template.render(**additional_data, **self.header, **kwargs)
        return data

    def create_file(self, file_data, file_name, relative_path: list = None):
        if relative_path:
            self.check_dir_or_create(relative_path)
            file_path = join(self.user_project_path, *relative_path, file_name)
        else:
            file_path = join(self.user_project_path, file_name)

        if not exists(file_path) or self.force_create:
            try:
                with open(file_path, 'w') as f:
                    f.write(file_data)
                    f.write('\n')
            except Exception:
                raise Exception('Something went wrong')
        else:
            print(f'File {file_name} already exist. Try flage --force to override previous files')

    def copy_file(self, file_name, relative_path=None):
        if relative_path:
            file_path = join(self.template_path, relative_path, file_name)
        else:
            file_path = join(self.template_path, file_name)

        with open(file_path, 'r') as f:
            data = f.read()

        self.create_file(data, file_name, relative_path)

    def __call__(self):
        for file_meta in self.file_meta_list:
            file_name, file_vars, relative_path = file_meta
            file_data = self.get_file_data(file_name, file_vars, relative_path)
            self.create_file(file_data, file_name, relative_path)
