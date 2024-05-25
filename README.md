# LUT Model

## TO DO STILL
* ### Some of the plotting scripts still need to be fixed
* ### bit more general refractoring
* ### what is Blad_spikes.csv doing?
* ### synapses.py is not being used?
* ### feedback.py is currently using block format still and is unable to be ran parallel

## Activate environment 
```
source /opt/py39-nrn/bin/activate
```
## Build network
```
python build_network.py
```
## Compile mod files
```
cd biophys_components/mechanisms/
rm -rf x86_64/
nrnivmodl modfiles/
cd ../..
```
## Run network
```
python run_network.py
```
## To check results open the notebook in the analysis folder Kernel path is /opt/py39-nrn/bin/python


## The file structure of the whole model will be 
| python file |use      |
|----------- | ----------- |
| build_network.py     |build network files            |
| run_network.py       |run network            | 
| Analysis folder      |plot simulation results            |
| model_parameters.py  |adjust network parameters                |
| feedback_loop.py     |BMTK module for feedback                  |
| bladder_equations.py |biophysical bladder eqautions stored here                 |
| biophys_components   |Stores cell templates and modfiles                 |
| network              |Stores network files                 |
