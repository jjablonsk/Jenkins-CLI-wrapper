import shutil
import socket
from urllib.parse import urlparse
import urllib.request
import progressbar


class Utils:

    def connection_checker(self, url):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        parsed_url, parsed_port = self.get_details_form_url(url)
        print(f"Trying connect to {parsed_url} over port: {parsed_port}")
        result = sock.connect_ex((parsed_url, int(parsed_port)))
        if result:
            print("Port looks closed")
            return True
        else:
            print("Success! Port is open!")
            return False

    def check_java(self):
        if shutil.which("java") is None:
            Exception("JAVA not installed please install it to use this tool")
        print("JAVA found! ")

    def download_cli(self, url, url_path):
        try:
            bar_wrap = [None]

            def reporthook(count, block_size, total_size):
                bar = bar_wrap[0]
                if bar is None:
                    bar = progressbar.ProgressBar(
                        maxval=total_size,
                        widgets=[
                            progressbar.Percentage(),
                            ' ',
                            progressbar.Bar(),
                            ' ',
                            progressbar.FileTransferSpeed()
                        ])
                    bar.start()
                    bar_wrap[0] = bar
                bar.update(min(count * block_size, total_size))

            urllib.request.urlretrieve(f'{url}/{url_path}', "jenkins-cli.jar", reporthook)
        except Exception:
            print(f"Unable to download jenkins-cli.jar from {url}/{url_path}")

    def get_details_form_url(self, url):
        try:
            result = urlparse(url)
            if result.hostname is None:
                raise Exception
            hostname = result.hostname
            if result.port:
                port = result.port
            else:
                if result.scheme == "http":
                    port = 80
                elif result.scheme == "https":
                    port = 443
                else:
                    print("Port or schema not provided in url assuming https:443")
                    port = 443

            return hostname, port
        except BaseException:
            print("Unable to parse user provided URL. Please check config file. Aborting!")
