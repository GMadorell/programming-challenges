from fabric.operations import local

def debug():
    local("sudo chmod +x ./random_password.py")
    local("echo -n '{0}' | {1} random_password.py".format(
        open("test_input.txt", "r").read(), open("interpreter.txt", "r").read()))

def test():
    local("sudo chmod +x ./random_password.py")
    local("sudo bash test_challenge {0} {1} ./random_password.py".format(
        open("challenge.token", "r").read(), open("interpreter.txt", "r").read()))

def submit():
    local("sudo chmod +x ./random_password.py")
    local("zip publish.zip random_password.py")
    local("sudo bash submit_challenge {0} publish.zip {1} ./random_password.py".format(
        open("challenge.token", "r").read(), open("interpreter.txt", "r").read()))
