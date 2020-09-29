#!/usr/bin/python

import yaml;
import sys;

path = "install-config.yaml";
data = yaml.safe_load(open(path));
data["compute"][0]["replicas"] = 0;

# open(path, "w").write(yaml.dump(data, default_flow_style=False))
sys.stdout.write(yaml.dump(data, default_flow_style=False))
