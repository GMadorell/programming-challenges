import os
import errno
from opster import command, dispatch
from jam_utils.create_jam_problem import create_jam_problem


@command(usage="contest version round prefix name")
def create(contest, version, round, prefix, name):
    """
    Creates a new google code jam problem in its respective folder.
    """
    current_path = os.path.dirname(os.path.realpath(__file__))
    directory_path = os.path.join(current_path, contest, version, round, prefix + "_" + name)
    file_path = os.path.join(directory_path, name + ".py")

    mkdirs(directory_path)

    with open(file_path, "w") as fd:
        fd.write(create_jam_problem(name))

    print("Done.")


def mkdirs(newdir, mode=0777):
    try:
        os.makedirs(newdir, mode)
    except OSError, err:
        # Reraise the error unless it's about an already existing directory
        if err.errno != errno.EEXIST or not os.path.isdir(newdir):
            raise


if __name__ == '__main__':
    dispatch()