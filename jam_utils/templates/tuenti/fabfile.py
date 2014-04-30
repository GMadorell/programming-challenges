from fabric.operations import local

def debug():
    local("sudo chmod +x ./{{ python_problem_filename }}")
    local("echo -n '{0}' | {1} {{ python_problem_filename }}".format(
        open("test_input.txt", "r").read(), open("interpreter.txt", "r").read()))

def test():
    local("sudo chmod +x ./{{ python_problem_filename }}")
    local("sudo bash test_challenge {0} {1} ./{{ python_problem_filename }}".format(
        open("challenge.token", "r").read(), open("interpreter.txt", "r").read()))

def submit():
    local("sudo chmod +x ./{{ python_problem_filename }}")
    local("zip publish.zip {{ python_problem_filename }}")
    local("sudo bash submit_challenge {0} publish.zip {1} ./{{ python_problem_filename }}".format(
        open("challenge.token", "r").read(), open("interpreter.txt", "r").read()))

