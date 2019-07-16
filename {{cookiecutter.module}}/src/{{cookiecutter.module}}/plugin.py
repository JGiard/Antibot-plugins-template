from pynject import pynject

from antibot.model.plugin import AntibotPlugin


@pynject
class {{cookiecutter.name}}(AntibotPlugin):
    def __init__(self):
        super().__init__('{{cookiecutter.name}}')
