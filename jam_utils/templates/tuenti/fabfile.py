from fabric.operations import local

def debug(input):
    local("sudo chmod +x ./{{ python_problem_filename }}")
    local("echo -n '{0}' | python {{ python_problem_filename }}".format(input))

def test():
    local("sudo chmod +x ./{{ python_problem_filename }}")
    local("sudo bash test_challenge {0} ./{{ python_problem_filename }}".format(open("challenge.token", "r").read()))

def submit():
    local("sudo chmod +x ./{{ python_problem_filename }}")
    local("zip publish.zip {{ python_problem_filename }}")
    local("sudo bash submit_challenge {0} publish.zip ./{{ python_problem_filename }}".format(open("challenge.token", "r").read()))
