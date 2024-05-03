import os
import subprocess
from hateSpeechClassifier.logger import logging
from colorama import Fore, Style


def get_all_python_files(directory):
    python_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                python_files.append(os.path.join(root, file))
    return python_files


def lint_python_files(files):
    for file in files:
        subprocess.run(['autopep8', '--in-place',
                       '--aggressive', '--aggressive', file])

        flake8_process = subprocess.run(
            ['flake8', file], capture_output=True, text=True)
        if flake8_process.returncode != 0:
            logging.error(f"Flake8 found errors in file: {file}")
            logging.error(flake8_process.stdout)

            print(f"{Fore.RED}Flake8 found errors in file: {file}{Style.RESET_ALL}")
            print(f"{Fore.RED}{flake8_process.stdout}{Style.RESET_ALL}")

        print(f"Linted file: {file}")


if __name__ == "__main__":
    project_directory = "/home/kalema/Projects/Hate-Speech-Text-Classification-NLP"
    all_python_files = get_all_python_files(project_directory)
    lint_python_files(all_python_files)
