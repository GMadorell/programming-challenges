import os
import errno
from opster import command, dispatch
from jam_utils.create_jam_problem import create_google_problem, create_tuenti_problem


@command(usage="contest version round prefix name")
def create_google(contest, version, round, prefix, name):
    """
    Creates a new google code jam problem in its respective folder.
    """
    directory_path = get_directory_path(contest, name, prefix, round, version)
    mkdirs(directory_path)
    create_google_problem(directory_path, name)
    print("Done.")


@command(usage="contest version round prefix name")
def create_tuenti(contest, version, round, prefix, name):
    """
    Creates a new tuenti challenge problem in its respective folder.
    """
    directory_path = get_directory_path(contest, name, prefix, round, version)
    mkdirs(directory_path)
    create_tuenti_problem(directory_path, name)
    print("Done.")


def get_directory_path(contest, name, prefix, round, version):
    current_path = os.path.dirname(os.path.realpath(__file__))
    directory_path = os.path.join(current_path, contest, version, round, prefix + "_" + name)
    return directory_path


def mkdirs(newdir, mode=0777):
    try:
        os.makedirs(newdir, mode)
    except OSError, err:
        # Reraise the error unless it's about an already existing directory
        if err.errno != errno.EEXIST or not os.path.isdir(newdir):
            raise


if __name__ == '__main__':
    import sys
    reload(sys)
    sys.setdefaultencoding("utf-8")

    dispatch()