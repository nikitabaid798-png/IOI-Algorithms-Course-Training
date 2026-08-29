# ---- Polymorphism Implementation----

class Math:
    def show_info(self):
        print("Math class information")


class Science:
    def show_info(self):
        print("Science class information")


math_class = Math()
science_class = Science()

math_class.show_info()
science_class.show_info()
