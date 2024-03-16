import fire
import  pluggy
from sharespec import MyPlugin
class App:
    def __init__(self):
        self.__pm = pluggy.PluginManager("mydemoapp")
        self.__pm.add_hookspecs(MyPlugin)
        self.__pm.load_setuptools_entrypoints("mydemoapptest")

    def run(self,plugin_name:str = "plugina"):
        result = self.__pm.get_plugin(plugin_name).add(1, 2)
        print(result)

def main():
    fire.Fire(App)

if __name__ == "__main__":
    main()