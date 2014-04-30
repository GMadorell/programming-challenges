import os
from jinja2 import Environment, PackageLoader


def create_google_problem(directory_path, problem_name):
    """
    :param problem_name: shall be formatted as a python variable
                         (underscores between words).
    :type problem_name: str
    """

    problem_class_name = "".join(map(lambda s: s.capitalize(), problem_name.split("_")))
    render_template("google/google_template.txt", directory_path, problem_name + ".py",
                    problem_class_name=problem_class_name)

def create_tuenti_problem(directory_path, problem_name):
    python_problem_filename = problem_name + ".py"
    problem_class_name = "".join(map(lambda s: s.capitalize(), problem_name.split("_")))

    render_template("tuenti/fabfile.py", directory_path, "fabfile.py", python_problem_filename=python_problem_filename)
    render_template("tuenti/problem_template.txt", directory_path, python_problem_filename, problem_class_name=problem_class_name)
    render_template("tuenti/gitignore_template.txt", directory_path, ".gitignore")
    render_template("tuenti/challenge.token", directory_path, "challenge.token")
    render_template("tuenti/interpreter.txt", directory_path, "interpreter.txt")
    render_template("tuenti/test_input.txt", directory_path, "test_input.txt")
    render_template("tuenti/submit_challenge", directory_path, "submit_challenge")
    render_template("tuenti/test_challenge", directory_path, "test_challenge")



def render_template(template_path, directory_path, file_name, **kwargs):
    env = Environment(loader=PackageLoader("jam_utils", "templates"))
    template = env.get_template(template_path)
    render = template.render(**kwargs)

    file_path = os.path.join(directory_path, file_name)
    with open(file_path, "w") as fd:
        fd.write(render)