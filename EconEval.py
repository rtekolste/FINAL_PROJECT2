import scr.EconEvalClasses as Econ

baseline_strat = Econ.Strategy(name="Baseline", cost_obs=[148.86], effect_obs=[.966])
training_strat = Econ.Strategy("Training Only", cost_obs=[153.81], effect_obs=[.968])
supplies_strat = Econ.Strategy("Supplies Only", cost_obs=[145.72], effect_obs=[.9685])
both_strat = Econ.Strategy("Both Training and Supplies", cost_obs=[153.27], effect_obs=[.971])

SA1_baseline_strat = Econ.Strategy(name="18% Baseline", cost_obs=[163.95], effect_obs=[.939])
SA1_training_strat = Econ.Strategy(name ="18% Training Only", cost_obs=[166.47], effect_obs=[.9426])
SA1_supplies_strat = Econ.Strategy(name= "18% Supplies Only", cost_obs=[158.30], effect_obs=[.9434])
SA1_both_strat = Econ.Strategy(name="18% Both Training and Supplies", cost_obs=[165.48], effect_obs=[.949])

SA2_baseline_strat = Econ.Strategy(name="4% Baseline", cost_obs=[137.54], effect_obs=[.986])
SA2_training_strat = Econ.Strategy(name ="4% Training Only", cost_obs=[144.33], effect_obs=[.9872])
SA2_supplies_strat = Econ.Strategy(name= "4% Supplies Only", cost_obs=[136.29], effect_obs=[.9874])
SA2_both_strat = Econ.Strategy(name="4% Both Training and Supplies", cost_obs=[144.11], effect_obs=[.989])

econ_eval=Econ.CEA(strategies=[baseline_strat, training_strat, supplies_strat, both_strat], if_paired=False)
Econ.CEA.show_CE_plane(econ_eval, title='Cost Effectiveness Analysis with 10% Hypertension',\
                       y_label='Cost',\
                       x_label='Utility',\
                       show_names=True,\
                       figure_size=6)

SA1_econ_eval=Econ.CEA(strategies=[SA1_baseline_strat, SA1_training_strat, SA1_supplies_strat, SA1_both_strat], if_paired=False)
Econ.CEA.show_CE_plane(SA1_econ_eval, title='Cost Effectiveness Analysis with 18% Hypertension',\
                       y_label='Cost',\
                       x_label='Utility',\
                       show_names=True,\
                       figure_size=6)

SA2_econ_eval=Econ.CEA(strategies=[SA2_baseline_strat, SA2_training_strat, SA2_supplies_strat, SA2_both_strat], if_paired=False)
Econ.CEA.show_CE_plane(SA2_econ_eval, title='Cost Effectiveness Analysis with 4% Hypertension',\
                       y_label='Cost',\
                       x_label='Utility',\
                       show_names=True,\
                       figure_size=6)

total_econ_eval = Econ.CEA(strategies=[baseline_strat, training_strat, supplies_strat, both_strat,\
                                       SA1_baseline_strat, SA1_training_strat, SA1_supplies_strat, SA1_both_strat,\
                                       SA2_baseline_strat, SA2_training_strat, SA2_supplies_strat, SA2_both_strat], if_paired=False)
Econ.CEA.show_CE_plane(total_econ_eval, title='Cost Effectiveness Analysis',\
                       y_label='Cost',\
                       x_label='Utility',\
                       show_names=True,\
                       figure_size=6)
