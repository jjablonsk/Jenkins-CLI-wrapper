import os
import subprocess
import datetime


class Executor:

    def __init__(self):
        self.process = None
        self.stdout = None
        self.stderr = None
        self.exit_code = None
        self.env = os.environ.copy()

    def add_env_variable(self, key, val):
        """Enables addition of custom OS environment variable for the cmd run."""
        self.env[key] = val

    def run(self, cmd, verbose=0):
        """Runs a cmd, logs output details to log and sets object members."""
        start_time = datetime.datetime.now().strftime("%y_%m_%d@%H:%M:%S")
        self.process = subprocess.run(cmd, stdin=subprocess.DEVNULL, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                      shell=True, encoding="utf-8", env=self.env)
        end_time = datetime.datetime.now().strftime("%y_%m_%d@%H:%M:%S")
        self.stdout = self.process.stdout
        self.stderr = self.process.stderr
        self.exit_code = int(self.process.returncode)
        if (verbose):
            print("CMD={}".format(cmd))
            print("STARTTIME={}".format(start_time))
            print("ENDTIME={}".format(end_time))
            print("ExitCode={}".format(str(self.exit_code)))
            print("STDOUT={}".format(self.stdout))
            print("STDERR={}".format(self.stderr))

            if self.get_exit_code() == 0:
                print("STATUS=SUCCESS")
            else:
                print("STATUS=FAIL")

    def get_output(self):
        """Returns output."""
        return self.stdout

    def get_err(self):
        """Returns error."""
        return self.stderr

    def get_exit_code(self):
        """Returns exit status from cmd."""
        return self.exit_code
