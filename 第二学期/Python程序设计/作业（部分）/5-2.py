def interchange_dict(Adic):
    Bvalues=Adic.keys()
    Bkeys=Adic.values()
    Bdic=dict(zip(Bvalues,Bkeys))
    print(sorted(Bdic.items()))
