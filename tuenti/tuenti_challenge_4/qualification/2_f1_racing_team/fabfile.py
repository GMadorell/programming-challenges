from fabric.operations import local

def debug(input):
    local("sudo chmod +x ./f1_racing_team.py")
    local("echo -n '{0}' | python f1_racing_team.py".format(input))

def test():
    local("sudo chmod +x ./f1_racing_team.py")
    local("sudo bash test_challenge {0} ./f1_racing_team.py".format(open("challenge.token", "r").read()))

def submit():
    local("sudo chmod +x ./f1_racing_team.py")
    local("zip publish.zip f1_racing_team.py")
    local("sudo bash submit_challenge {0} publish.zip ./f1_racing_team.py".format(open("challenge.token", "r").read()))