"""
Basic idea of this is class is to store all model parameters that are regularly changes here.
Then you would not have to go into all the script and make sure they are changed.

"""
class model_settings():
    
    def __init__(self) -> None:
        self.case = 'baseline'
        self.dt = 0.2 # ms
        self.t_sim = 30500.0 # ms
        self.scale = 1
        self.node_set = [
            {"name": "Bladaff", "start": 0*self.scale, "end": 9*self.scale, "color": "blue"},
            {"name": "PAGaff", "start": 10*self.scale, "end": 19*self.scale, "color": "gray"},
            {"name": "EUSaff", "start": 20*self.scale, "end": 29*self.scale, "color": "green"},
            {"name": "IND", "start": 30*self.scale, "end": 39*self.scale, "color": "orange"},
            {"name": "Hypo", "start": 40*self.scale, "end": 49*self.scale, "color": "red"},
            {"name": "INmplus", "start": 50*self.scale, "end": 59*self.scale, "color": "purple"},
            {"name": "INmminus", "start": 60*self.scale, "end": 69*self.scale, "color": "cyan"},
            {"name": "PGN", "start": 70*self.scale, "end": 79*self.scale, "color": "magenta"},
            {"name": "FB", "start": 80*self.scale, "end": 89*self.scale, "color": "lime"},
            {"name": "IMG", "start": 90*self.scale, "end":  99*self.scale, "color": "yellow"},
            {"name": "MPG", "start": 100*self.scale, "end": 109*self.scale, "color": "brown"},
            {"name": "EUSmn", "start": 110*self.scale, "end": 119*self.scale, "color": "pink"},
            {"name": "Bladmn", "start": 120*self.scale, "end": 129*self.scale, "color": "skyblue"}
        ]

        pass
