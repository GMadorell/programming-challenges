from fabric.operations import local

def debug():
    local("sudo rm -f DEBUG.txt")
    local("sudo chmod +x ./tuenti_restructuration.py")
    local("echo -n '{0}' | {1} tuenti_restructuration.py".format(
        open("test_input.txt", "r").read(), open("interpreter.txt", "r").read()))

def test():
    local("sudo rm -f DEBUG.txt")
    local("sudo chmod +x ./tuenti_restructuration.py")
    local("sudo bash test_challenge {0} {1} ./tuenti_restructuration.py".format(
        open("challenge.token", "r").read(), open("interpreter.txt", "r").read()))

def submit():
    local("sudo chmod +x ./tuenti_restructuration.py")
    local("zip publish.zip tuenti_restructuration.py")
    local("sudo bash submit_challenge {0} publish.zip {1} ./tuenti_restructuration.py".format(
        open("challenge.token", "r").read(), open("interpreter.txt", "r").read()))
