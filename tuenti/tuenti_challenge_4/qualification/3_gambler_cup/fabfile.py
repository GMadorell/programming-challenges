from fabric.operations import local

def debug(input):
    local("sudo chmod +x ./gambler_cup.py")
    local("echo -n '{0}' | python gambler_cup.py".format(input))

def test():
    local("sudo chmod +x ./gambler_cup.py")
    local("sudo bash test_challenge {0} ./gambler_cup.py".format(open("challenge.token", "r").read()))

def submit():
    local("sudo chmod +x ./gambler_cup.py")
    local("zip publish.zip gambler_cup.py")
    local("sudo bash submit_challenge {0} publish.zip ./gambler_cup.py".format(open("challenge.token", "r").read()))