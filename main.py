from jenkins_cli import JenkinsCli
from settings import Settings
from utils import Utils

def main():
    "Load settings"
    cfg = Settings()
    cfg.load()
    cfg.view()

    "Check connection to Jenkins instance"
    utils = Utils()
    result = utils.connection_checker(cfg.jenkins_url)

    "check user if java exist in system"
    utils.check_java()

    "download jar from jenkins server"
    utils.download_cli(cfg.jenkins_url, cfg.jenkins_jar_path)

    jenkins_cli = JenkinsCli()
    jenkins_cli.list_plugins()
    jenkins_cli.get_plugin_version(plugin_name="javax-activation-api")




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
