#!/local/driftinfo/venv/bin/python3
import subprocess
import yaml

config_file = '/local/driftinfo/conf/config_file.yml'
with open(config_file,'r') as ymlfile:
    cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)
plugin_conf = cfg['plugins']
commands = []
for plugin_object in plugin_conf:
    for plugin in plugin_object:
        if plugin_object[plugin]:
            for arg in plugin_object[plugin]:
                commands.append(["/local/driftinfo/venv/plugins/" + plugin + ".py", arg])
        else:
                commands.append(["/local/driftinfo/venv/plugins/" + plugin + ".py"])

for command in commands:
    subprocess.Popen(command)
