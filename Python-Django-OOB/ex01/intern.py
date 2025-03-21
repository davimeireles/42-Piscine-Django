class Intern:
    def __init__(self, name):
        self.name = name or "My name? I’m nobody, an intern, I have no name."

    def __str__(self):
        return self.name

    def work(self):
        raise Exception("I’m just an intern, I can’t do that...")

    def make_coffe(self):
        return Coffe()

class Coffe:
    def __str__(self):
        return "This is the worst coffee you ever tasted."


if __name__ == '__main__':

    try:
        intern_no_name = Intern(None)
        print(intern_no_name.__str__())
        print("\n")

        intern = Intern("Mark")
        print(intern.__str__())
        print("\n")

        print(intern.make_coffe())
        print("\n")

        intern_no_name.work()

    except Exception as error:
        print(f"{error}")