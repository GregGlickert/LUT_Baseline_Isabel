# LUT Model

## TO DO STILL
* ### Some of the plotting scripts still need to be fixed
* ### bit more general refractoring
* ### what is Blad_spikes.csv doing?
* ### synapses.py is not being used?
* ### feedback.py is currently using block format still and is unable to be ran parallel

## Build network
```
python build_network.py
```
## Compile mod files
```
cd biophys_components/mechaisms
nrnivmodl modfiles
cd ../..
```
## Run network
```
python run_network.py
```
## Check results
```
python plot_results.py
```

## The file structure of the whole model will be 
| python file |use      |
|----------- | ----------- |
| build_network.py     |build network files            |
| run_network.py       |run network            | 
| plot_results.py      |plot simulation results            |
| model_parameters.py  |adjust network parameters                |
| feedback_loop.py     |BMTK module for feedback                  |
| bladder_equations.py |biophysical bladder eqautions stored here                 |
| biophys_components   |Stores cell templates and modfiles                 |
| network              |Stores network files                 |
