import scr.DecisionTree as dt
import InputData as D

# dictionary for decision nodes
#               // key: cost, utility, [future nodes]
dictDecisions = {'d1': [0,     0,       ['baseline']]};

#           // key:             cost,   utility,    [future nodes],                     [probabilities]
dictChances = { 'baseline':     [0,     0,          ['BP', 'NoBP'],                     [D.BP_P, (1-D.BP_P)]],
                #NO BP Branch
                'NoBP':         [0,     0,          ['NoBP_HTN', 'T_No_BP_No_HTN'],     [D.HTN_P, (1-D.HTN_P)]],
                'NoBP_HTN':     [0,     0,          ['T_NoBP_HTN', 'No_BP_PE'],         [D.PE_P, (1-D.PE_P)]],
                'NoBP_PE':      [0,     0,          ['T_No_BP_PE', 'T_No_BP_E'],        [D.E_P, (1-D.E_P)]],

                #BP No MD Branch
                'BP':            [0,     0,          ['T_BP_No_HTN', 'BP_HTN'],          [D.HTN_P, (1-D.HTN_P)]],
                'BP_HTN':        [0,     0,          ['MD',  'No_MD'],                   [D.MD_P, (1-D.MD_P)]],
                'No_MD':         [0,     0,          ['No_MD_PE', 'T_No_MD_HTN'],        [D.PE_P, (1-D.PE_P)]],
                'No_MD_PE':      [0,     0,          ['T_No_MD_E', 'T_No_MD_PE'],        [D.E_P, (1-D.E_P)]],

                #BP MD, NO UA Branch
                'MD':            [0,     0,          ['UA', 'No_UA'],                    [D.UA_P, (1-D.UA_P)]],
                'No_UA':         [0,     0,          ['No_UA_PE', 'T_No_UA_HTN'],        [D.PE_P*D.RR, (1-(D.PE_P*D.RR))]],
                'No_UA_PE':      [0,     0,          ['T_No_UA_PE', 'T_No_UA_E'],        [D.E_P, (1-D.E_P)]],

                #BP, MD, UA, NO MGSO4 Branch
                'UA':            [0,     0,          ['UA_PE', 'T_UA_HTN'],              [D.PE_P*D.RR, (1-(D.PE_P*D.RR))]],
                'UA_PE':         [0,     0,          ['MGSO4', 'No_MGSO4'],              [D.MGSO4_P,  (1-D.MGSO4_P)]],
                'No_MGSO4':      [0,     0,          ['T_No_MGSO4_E', 'T_No_MGSO4_PE'],  [D.E_P, (1-D.E_P)]],

                #All
                'MGSO4':         [0,    0,          ['T_MGSO4_E', 'T_MGSO4_PE'],        [D.E_PMGSO4, (1-D.E_PMGSO4)]] };

# dictionary for terminal nodes
#               //key:          cost,   utility
dictTerminals = {'T_No_BP_No_HTN':       [0,     1.0],
                 'T_No_BP_HTN':          [0,     .78],
                 'T_No_BP_PE':           [0,     .4],
                 'T_No_BP_E':            [0,     .1],

                 #NoMD
                 'T_BP_No_HTN':          [0,    1.0],
                 'T_No_MD_HTN':          [0,    .78],
                 'T_No_MD_PE':           [0,    .4],
                 'T_No_MD_E':            [0,    .1],

                 #No UA
                'T_No_UA_HTN':          [0,    .78],
                'T_No_UA_PE':           [0, .4],
                'T_No_UA_E':            [0, .1],

                'T_No_MGSO4_PE':        [0, .4],
                'T_No_MGSO4_E':         [0, .1],

                #MGSO4
                'T_MGSO4_PE':           [0, .4],
                'T_MGSO4_E':            [0, .1]
};

myDT = dt.DecisionNode('d1', 1, dictDecisions, dictChances, dictTerminals)

# print the expected cost and utility of each alternative
print('\nExpected cost and utility:')
print(myDT.get_cost_utility())

# print the probability of terminal nodes under each alternative
print('\nProbabilities of terminal nodes:')
print(myDT.get_terminal_prob())

# plot the expected cost and utility of each alternative
dt.graph_outcomes(myDT)
