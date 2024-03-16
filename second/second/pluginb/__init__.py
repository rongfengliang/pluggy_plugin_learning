from sharespec import hookimpl

class PluginB:
    @hookimpl
    def add(self, x, y):
        return x + y

    @hookimpl
    def sub(self, x, y):
        return x - y
    
MyPluginB = PluginB()