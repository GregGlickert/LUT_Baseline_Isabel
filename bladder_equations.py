#### BLADDER EQUATIONS from Grill, et al. 2016 

def blad_vol(vol):
    f = 1.5*100*vol #- 1.5 #-10 #math.exp(48*vol-64.9) + 8
    return f

# Grill function returning pressure in units of cm H20
def pressure(PGN,v,IMG):
    p = 0.6*PGN +  1.0*v - 0.1*IMG + 9
    #print("p = 0.7*{0} + 7*{1} - 0.7*{2}".format(PGN, v, IMG))
    p = max(p,0.0)
    return p 

# Grill function returning bladder afferent firing rate in units of Hz
def blad_aff_fr(p):
    fr1 = -3.0E-08*p**5 + 1.0E-5*p**4 - 1.5E-03*p**3 + 7.9E-02*p**2 - 0.6*p
    fr1 = max(fr1,0.0)
    return fr1 # Using scaling factor of 5 here to get the correct firing rate range