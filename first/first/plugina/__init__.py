from sharespec import hookimpl

class PluginA:
    @hookimpl
    def add(self, x, y):
        return x + y

    @hookimpl
    def sub(self, x, y):
        return x - y
    
MyPluginA = PluginA()