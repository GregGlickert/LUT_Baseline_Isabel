import sys
from bmtk.simulator import bionet
from bmtk.simulator.bionet.default_setters.cell_models import loadHOC
from bmtk.simulator.bionet.io_tools import io
from neuron import h
from feedback_loop import FeedbackLoop
import json
import model_parameters 
# Import the synaptic depression/facilitation model
#import synapses
model = model_parameters.model_settings()

press_thres = 17 # cm H20 #40
                 # Lingala, et al. 2016
change_thres = 10 # cm H20 #10
                 # Need biological value for this

bionet.pyfunction_cache.add_cell_model(loadHOC, directive='hoc', model_type='biophysical')

def run(config_file):
    with open(config_file, 'r') as json_file:
        conf_dict = json.load(json_file)
        conf_dict['run']['tstop'] = model.t_sim
        conf_dict['run']['dt'] = model.dt
        conf = bionet.Config.from_dict(conf_dict, validate=True)

    conf.build_env()

    fbmod = FeedbackLoop()

    graph = bionet.BioNetwork.from_config(conf)
    sim = bionet.BioSimulator.from_config(conf, network=graph)
    sim.add_mod(fbmod)  # Attach the above module to the simulator.
    sim.run()
    bionet.nrn.quit_execution()

if __name__ == '__main__':
    if len(sys.argv) > 1:
        io.log_info("running " + sys.argv[1])
        run(sys.argv[1])
    else:
        if model.case == 'baseline':
            config = 'jsons/simulation_config.json'
        # could add different cases and manage them like this
        #if model.case == 'sci':
        #    config = 'sci_simulation_config.json'
        io.log_info("running " + config)
        run(config_file=config)
