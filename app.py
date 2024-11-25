import subprocess
import shlex

def run_command(cmd):
    safe_cmd = shlex.split(cmd)
    subprocess.call(safe_cmd)

if __name__ == "__main__":
    cmd = input("Enter a command to run: ")
    run_command(cmd)
