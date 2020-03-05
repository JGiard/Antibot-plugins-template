from injector import inject

from antibot.plugin import AntibotPlugin


class {{cookiecutter.name}}(AntibotPlugin):
    @inject
    def __init__(self):
        super().__init__('{{cookiecutter.name}}')
