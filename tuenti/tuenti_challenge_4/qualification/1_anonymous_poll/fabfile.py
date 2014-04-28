from fabric.operations import local

def test():
    local("sudo bash test_challenge {0} ./anonymous_poll.py".format(open("challenge.token", "r").read()))

def submit():
    local("zip publish.zip anonymous_poll.py")
    local("sudo bash submit_challenge {0} publish.zip ./anonymous_poll.py".format(open("challenge.token", "r").read()))
