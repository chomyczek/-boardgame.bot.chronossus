import os
import subprocess
import sys

python: str
MIN_PYTHON_MINOR_VER = 7
PYTHON_MAJOR_VER = 3


def at_least_py_3_7():
    """
    Check if python version meet criteria
    :return: Return True if python version meet criteria
    """
    return sys.version_info.major == PYTHON_MAJOR_VER and sys.version_info.minor >= MIN_PYTHON_MINOR_VER


def execute_cmd(cmd, cwd="scripts/"):
    """Execute passed command and return return_code and output
    :param cmd: Command to handle
    :param cwd: Current working directory
    :return: Return code and command output
    """
    try:
        if cwd:
            child = subprocess.run(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                check=True,
                cwd=cwd,
                shell=True,
            )
        else:
            child = subprocess.run(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                check=True,
                shell=True,
            )
    except subprocess.CalledProcessError as e:
        child = e
    return child.returncode, child.stderr.decode("utf-8") + child.stdout.decode("utf-8")


def handle_isort_black(cmd):
    """
    Special handle for isort and black
    :param cmd: Command to handle
    :return: Return code
    """
    _rc, _ = execute_cmd(cmd + " --check")  # run with --check to gather return code
    if found_error_in(_rc):
        _, output = execute_cmd(cmd)  # run without check to reformat files
        print(output)
    return _rc


def handle_common_cmd(cmd):
    """
    Handle for common command
    :param cmd: Command to handle
    :return: Return code
    """
    _rc, output = execute_cmd(cmd)
    if found_error_in(_rc):
        print(output)
    return _rc


def run_isort():
    """
    Check and format imports
    :return: Return code
    """
    print("Running isort ...")
    cmd = "isort .."
    return handle_isort_black(cmd)


def run_black():
    """
    Check and format PEP8
    :return: Return code
    """
    print("Running black ...")
    cmd = "black .."
    return handle_isort_black(cmd)


def run_pylint():
    """
    Check docstrings
    :return: Return code
    """
    print("Running pylint ...")
    cmd = "pylint ../src --rcfile=../docstring.pylintrc"
    return handle_common_cmd(cmd)


def run_pip_install():
    """
    Install necessary packages
    :return: Return code
    """
    print("Running pip install ...")
    cmd = f"{python} -m pip install -r ../requirements_dev.txt"
    return handle_common_cmd(cmd)


def run_flake8():
    """
    Check PEP8
    :return: Return code
    """
    print("Running flake8 ...")
    cmd = "flake8 --config ../setup.cfg ../src"
    return handle_common_cmd(cmd)


def run_coverage():
    """
    Run tests and check coverage
    :return: Return code
    """
    print("Running coverage ...")
    _rc = 0
    cmd = f"{python} -m pytest --cov=./src --cov-fail-under=100 --cov-report term-missing"
    _rc, output = execute_cmd(cmd, ".")
    if found_error_in(_rc):
        print(output)
    return _rc


def found_error_in(_rc):
    """
    Returns true if command ends with non-zero error code
    :param _rc: Return code to check
    :return: True if return code is none-zero
    """

    return _rc != 0


def print_separator():
    """Print simple text separator"""
    print("*" * 20 + " VERIFICATION FAILED! " + "*" * 20)


def verify_python_version():
    """Verify if python version meets criteria"""
    if not at_least_py_3_7():
        print("This script requires Python 3.7 or higher!")
        print("You are using Python {}.{}.".format(sys.version_info.major, sys.version_info.minor))

        sys.exit(1)


def get_python_path():
    if len(sys.argv) < 2:
        print("As second parameter add path to python (python from venv is the best option).")
        sys.exit(1)
    global python
    python = sys.argv[1]
    if not os.path.exists(python):
        print("Python path is not valid, file don't exists.")
        print(f"path: {python}")
        sys.exit(1)


if __name__ == "__main__":
    """This script assume that current working directory is root of this repository"""

    verify_python_version()
    get_python_path()

    rc = 0
    summary = []
    print("Running script verify_all.py ...")
    if found_error_in(run_pip_install()):
        print_separator()
        print("There was problem with pip command!")
        sys.exit(1)
    isort_rc = run_isort()
    black_rc = run_black()
    if found_error_in(isort_rc) or found_error_in(black_rc):
        summary.append("FILES WAS MODIFIED!")
        summary.append("Please commit changes before pushing your branch.")
        rc = 1
    if found_error_in(run_pylint()):
        summary.append("There was problem with docstrings!")
        rc = 1
    if found_error_in(run_flake8()):
        summary.append("Code does not meet the PEP8 standard!")
        rc = 1
    if found_error_in(run_coverage()):
        summary.append("Tests failed or code is not fully covered!")
        rc = 1

    if rc == 0:
        print("You are good to go!")
    else:
        print_separator()
        for line in summary:
            print(line)
    sys.exit(rc)
