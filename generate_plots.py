import plot_results_old
from bmtk.simulator import bionet

config_file='jsons/simulation_config.json'
conf = bionet.Config.from_json(config_file, validate=True)
conf.build_env()

graph = bionet.BioNetwork.from_config(conf)
sim = bionet.BioSimulator.from_config(conf, network=graph)
plot_results_old.run(sim=sim,conf=conf)