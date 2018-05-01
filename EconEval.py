import scr.EconEvalClasses as Econ
import Decision_Tree as Inputs
import RunTree as run

baseline_strat = Econ.Strategy("Baseline", 1.44, .966)
training_strat = Econ.Strategy("Training Only", 8.81, .9661)
supplies_strat = Econ.Strategy("Supplies Only", 1.17, .968)
both_strat = Econ.Strategy("Both Training and Supplies", 12.432, .915)
