import subprocess
from getpass import getpass


update_command = "sudo apt-get update"
install_command = "sudo apt-get -y install ccextractor"


def run_command_with_password(command):
    password = getpass("Enter your password: ")
    command_with_password = f"echo {password} | {command}"

    try:
        subprocess.run(command_with_password, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {command}\n{e}")


# Run update command
print("Running update command...")
subprocess.run(update_command, shell=True)

# Run install command with password
print("Running install command...")
run_command_with_password(install_command)

print("Script execution completed.")

# ccextractor -o ./output/subs1.srt ~/Downloads/8849331ddae9c3169024d569ce17b9a4fdd917401cd6c6bfb8dc1fd59c6af21e.mp4
