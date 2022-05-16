import pytest
from subprocess import check_output

script_path = "./loops1.sh"

def run_shell_test(script, arg1):
    out = check_output([script, str(arg1)], universal_newlines=True)
    return out.split("\n")[0]

def test_hello_world():
    result = run_shell_test(script_path, 'Hello World!')
    assert result == "!DLROw OLLEh"

def test_bash():
    result = run_shell_test(script_path, 'bash')
    assert result == "HSAB"