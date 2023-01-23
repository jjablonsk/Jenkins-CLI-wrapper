from jenkins_cli_commands import CommandFactory


class JenkinsCli(CommandFactory):
    def __init__(self):
        self.cf = CommandFactory()

    def list_plugins(self):
        self.cf.create("list_plugins").execute()

    def get_plugin_version(self, plugin_name):
        self.cf.create("get_plugin_version", plugin_name).execute()
