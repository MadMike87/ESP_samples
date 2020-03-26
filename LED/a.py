class WPLClass:
    def __init__(self):
        txt = '\n\t\t\t\tWPL is the best\n'
        print(txt)

    def wpl_add(self, a, b):
        print('\tHallo from class WPLClass method wpl_add\n')
        return a + b

    def wpl_sub(self, a, b):
        print('\tHallo from class WPLClass method wpl_sub\n')
        return a - b

    def wpl_addsub(self, a, b):
        print('\tHallo from class WPLClass method wpl_addsub\n')
        return (a + b) + (a - b)
