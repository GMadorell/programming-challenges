from jinja2 import Environment, PackageLoader


def create_jam_problem(problem_name):
    """
    :param problem_name: shall be formatted as a python variable
                         (underscores between words).
    :type problem_name: str
    """
    env = Environment(loader=PackageLoader("jam_utils", "templates"))

    template = env.get_template("jam_template.txt")

    problem_class_name = "".join(map(lambda s: s.capitalize(), problem_name.split("_")))

    return template.render(problem_class_name=problem_class_name)