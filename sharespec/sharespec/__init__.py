import pluggy

hookspec = pluggy.HookspecMarker("mydemoapp")
hookimpl = pluggy.HookimplMarker("mydemoapp")

class MyPlugin:
    @hookspec
    def add(self, x, y):
      """my add hook spec"""

    @hookspec
    def sub(self,x,y):
       """my sub hook spec"""
    