import  pluggy
from sharespec import MyPlugin

pm = pluggy.PluginManager("mydemoapp")
pm.add_hookspecs(MyPlugin)
pm.load_setuptools_entrypoints("mydemoapp")
result = pm.get_plugin("plugina").add(1, 2)
print(result)