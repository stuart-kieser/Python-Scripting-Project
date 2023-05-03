import os  # operating system
import json
import shutil  # allows copy and overwite
from subprocess import PIPE, run  # Allows run of terminal command
import sys

GAME_DIR_PATTERN = "game"


def find_all_game_paths(source):
    game_paths = []

    for root, dirs, files in os.walk(source):
        # dirs is a built in command avoidusing built in command that are apart of python
        for directory in dirs:
            if GAME_DIR_PATTERN in directory.lower():
                path = os.path.join(source, directory)
                game_paths.append(path)
        break


def main(source, target):
    cwd = os.getcwd()
    source_path = os.path.join(cwd, source)
    target_path = os.path.join(cwd, target)

    game_paths = find_all_game_paths(source_path)
    print(game_paths)


if __name__ == "__main__":
    args = sys.argv
    if len(args) != 3:
        raise Exception("You must pass a soruce and target directory - only")

    source, target = args[1:]
    main(source, target)
