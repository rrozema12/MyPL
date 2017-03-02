"""
Ryan Rozema
my_symbol_table.py
hw5
"""
class SymbolTable(object):
    def __init__(self):
        self.scopes = []        # list of {var_name:{'type':t, 'value':v}}

    def __environment(self, var_name):
        # search from last (most recent) to first environment
        for i in range(len(self.scopes)-1, -1, -1):
            if var_name in self.scopes[i]:
                return self.scopes[i]

    def variable_exists(self, var_name):
        return self.__environment(var_name) != None

    def add_variable(self, var_name):
        # can't add if no environments
        if len(self.scopes) == 0:
            return
        # add to the most recently added environemt
        self.scopes[-1][var_name] = {'type':None, 'value':None}

    def get_variable_type(self, var_name):
        env = self.__environment(var_name)
        if env != None:
            return env[var_name]['type']

    def set_variable_type(self, var_name, var_type):
        env = self.__environment(var_name)
        if env != None:
            env[var_name]['type'] = var_type

    def set_variable_value(self, var_name, var_value):
        env = self.__environment(var_name)
        if env != None:
            env[var_name]['value'] = var_value

    def get_variable_value(self, var_name):
        env = self.__environment(var_name)
        if env != None:
            return env[var_name]['value']

    def push_environment(self):
        self.scopes.append({})

    def pop_environment(self):
        if len(self.scopes) > 0:
            self.scopes.pop()

    def __str__(self):
        return str(self.scopes)
