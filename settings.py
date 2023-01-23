import sys

import yaml
class _Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(_Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Singleton(_Singleton('SingletonMeta', (object,), {})): pass

class Settings(Singleton):

    def __init__(self):
        self.jar_path = "jnlpJars/jenkins-cli.jar"
        self.cfg = ""

    def load(self):
        with open("config.yml", "r") as ymlfile:
            self.cfg = yaml.full_load(ymlfile)

    def view(self):
        print("Current Config")
        print(yaml.dump(self.cfg))

    @property
    def jenkins_jar_path(self):
        return self.jar_path

    @property
    def jenkins_url(self):
        try:
            return self.cfg['jenkins']['url']
        except AttributeError:
            print("The jenkins_url is not set in config")
            return False

    @property
    def jenkins_auth(self):
        try:
            return self.cfg['jenkins']['auth']
        except AttributeError:
            print("The auth is not set in config")
            return False
