

## func for calculating the expected value of generated energy


instalation_power=2.5   #Moc instalacji fotowoltaicznej [kW]
panel_effect=0.2        #Efektywność paneli


def calc_exp_generated_energy(time_exposition, instalation_power=2.5, panel_effect=0.2):
    return (time_exposition/3600) * instalation_power * panel_effect


