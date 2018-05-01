import scr.EconEvalClasses as Econ
import Decision_Tree as Inputs
import RunTree as run

baseline_strat = Econ.Strategy(name="Baseline", cost_obs=1.44, effect_obs=.966)
training_strat = Econ.Strategy("Training Only", cost_obs=8.81, effect_obs=.9661)
supplies_strat = Econ.Strategy("Supplies Only", cost_obs=1.17, effect_obs=.968)
both_strat = Econ.Strategy("Both Training and Supplies", cost_obs=12.432, effect_obs=.915)

econ_eval=Econ.CEA(strategies=[baseline_strat, training_strat, supplies_strat, both_strat], if_paired=False)
Econ.CEA.show_CE_plane(econ_eval, title='Cost Effectiveness Analysis',\
                       y_label='Cost',\
                       x_label='Utility')
