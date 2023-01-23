from abc import ABC, abstractmethod
from command_executor import Executor

from settings import Settings


class AbstractCommand(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def get_output(self):
        pass

    @abstractmethod
    def get_error(self):
        pass


class CommandBlueprint:
    def __init__(self):
        self.cfg = Settings()
        self.executor = Executor()
        self.verbose = 0
        self.executable = "java -jar jenkins-cli.jar"
        self.jenkins_url = f'-s {self.cfg.jenkins_url}'
        self.auth = f"-auth {self.cfg.jenkins_auth}"


class ListPluginsCommand(AbstractCommand):
    def __init__(self, *args):
        self.cmd_bp = CommandBlueprint()
        self.args = args

    def execute(self):
        print("\nexecute of ListPluginsCommand\n")
        cmd = f'{self.cmd_bp.executable} {self.cmd_bp.jenkins_url} {self.cmd_bp.auth} list-plugins'
        self.cmd_bp.executor.run(cmd=cmd, verbose=self.cmd_bp.verbose)
        if self.cmd_bp.executor.get_exit_code():
            self.get_error()
        self.get_output()

    def show(self):
        print(f'{self.cmd_bp.executable} {self.cmd_bp.jenkins_url} {self.cmd_bp.auth} list-plugins')

    def get_output(self):
        print(self.cmd_bp.executor.get_output())

    def get_error(self):
        print(self.cmd_bp.executor.get_err())


class CheckPluginVersionCommand(AbstractCommand):
    def __init__(self, *args):
        self.cmd_bp = CommandBlueprint()
        self.args = args

    def execute(self):
        cmd = f'{self.cmd_bp.executable} {self.cmd_bp.jenkins_url} {self.cmd_bp.auth} list-plugins {self.args[0][0]}'
        self.cmd_bp.executor.run(cmd=cmd, verbose=self.cmd_bp.verbose)
        if self.cmd_bp.executor.get_exit_code():
            self.get_error()
        self.get_output()


    def show(self):
        print(f'{self.cmd_bp.executable} {self.cmd_bp.jenkins_url} {self.cmd_bp.auth} list-plugins {self.args[0][0]}')

    def get_output(self):
        result = self.cmd_bp.executor.get_output()
        version = result.split(" ")[-1]
        print(f'{self.args[0][0]} is in version {version}')
        return version

    def get_error(self):
        print(self.cmd_bp.executor.get_err())


class CommandFactory:

    @staticmethod
    def create(command, *args):
        if command == 'list_plugins':
            return ListPluginsCommand(args)
        elif command == 'get_plugin_version':
            return CheckPluginVersionCommand(args)
