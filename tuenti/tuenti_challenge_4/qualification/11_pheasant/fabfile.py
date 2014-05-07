from fabric.operations import local

def debug():
    local("sudo chmod +x ./pheasant.py")
    local("echo -n '{0}' | {1} pheasant.py".format(
        open("test_input.txt", "r").read(), open("interpreter.txt", "r").read()))

def test():
    local("sudo chmod +x ./pheasant.py")
    local("sudo bash test_challenge {0} {1} ./pheasant.py".format(
        open("challenge.token", "r").read(), open("interpreter.txt", "r").read()))

def submit():
    local("sudo chmod +x ./pheasant.py")
    local("zip publish.zip pheasant.py")
    local("sudo bash submit_challenge {0} publish.zip {1} ./pheasant.py".format(
        open("challenge.token", "r").read(), open("interpreter.txt", "r").read()))
