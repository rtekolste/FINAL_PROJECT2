import scr.DecisionTree as dt
import InputData as D

# dictionary for decision nodes
#               // key: cost, utility, [future nodes]
dictDecisions = {'d1': [0,     0,       ['baseline', 'training', 'supplies', 'both']]};

#           // key:             cost,   utility,    [future nodes],                     [probabilities]
dictChances = { 'baseline':     [0,     0,          ['BP', 'NoBP'],                     [D.BP_P, (1-D.BP_P)]],
                #NO BP Branch
                'NoBP':         [0,     0,          ['NoBP_HTN', 'T_NoBP_No_HTN'],     [D.HTN_P, (1-D.HTN_P)]],
                'NoBP_HTN':     [0,     0,          ['NoBP_PE', 'T_NoBP_HTN'],         [D.PE_P, (1-D.PE_P)]],
                'NoBP_PE':      [0,     0,          ['T_NoBP_E', 'T_NoBP_PE'],         [D.E_P, (1-D.E_P)]],

                #BP No MD Branch
                'BP':            [0,     0,          ['BP_HTN', 'T_BP_No_HTN'],          [D.HTN_P, (1-D.HTN_P)]],
                'BP_HTN':        [18,    0,          ['MD',  'No_MD'],                  [D.MD_P, (1-D.MD_P)]],
                'No_MD':         [0,     0,          ['No_MD_PE', 'T_No_MD_HTN'],        [D.PE_P, (1-D.PE_P)]],
                'No_MD_PE':      [0,     0,          ['T_No_MD_E', 'T_No_MD_PE'],        [D.E_P, (1-D.E_P)]],

                #BP MD, NO UA Branch
                'MD':            [18,    0,          ['UA', 'No_UA'],                    [D.UA_P, (1-D.UA_P)]],
                'No_UA':         [0,     0,          ['No_UA_PE', 'T_No_UA_HTN'],        [D.PE_P*D.RR, (1-(D.PE_P*D.RR))]],
                'No_UA_PE':      [0,     0,          ['T_No_UA_E', 'T_No_UA_PE'],        [D.E_P, (1-D.E_P)]],

                #BP, MD, UA, NO MGSO4 Branch
                'UA':            [12,    0,          ['UA_PE', 'T_UA_HTN'],              [D.PE_P*D.RR, (1-(D.PE_P*D.RR))]],
                'UA_PE':         [0,     0,          ['MGSO4', 'No_MGSO4'],              [D.MGSO4_P,  (1-D.MGSO4_P)]],
                'No_MGSO4':      [0,     0,          ['T_No_MGSO4_E', 'T_No_MGSO4_PE'],  [D.E_P, (1-D.E_P)]],

                #All
                'MGSO4':         [5,    0,          ['T_MGSO4_E', 'T_MGSO4_PE'],        [D.E_PMGSO4, (1-D.E_PMGSO4)]],

###TRAINING SCENARIO
                'training':     [8,     0,          ['Tr_BP', 'Tr_NoBP'],                     [D.TR_BP_P, (1-D.TR_BP_P)]],
                #NO BP Branch
                'Tr_NoBP':      [0,     0,          ['Tr_NoBP_HTN', 'Tr_T_NoBP_No_HTN'],     [D.HTN_P, (1-D.HTN_P)]],
                'Tr_NoBP_HTN':  [0,     0,          ['Tr_T_NoBP_HTN', 'Tr_NoBP_PE'],         [D.PE_P, (1-D.PE_P)]],
                'Tr_NoBP_PE':   [0,     0,          ['Tr_T_NoBP_E', 'Tr_T_NoBP_PE'],         [D.E_P, (1-D.E_P)]],

                #BP No MD Branch
                'Tr_BP':            [0,     0,          ['Tr_BP_HTN', 'Tr_T_BP_No_HTN'],          [D.HTN_P, (1-D.HTN_P)]],
                'Tr_BP_HTN':        [0,     0,          ['Tr_MD',  'Tr_No_MD'],                   [D.MD_P, (1-D.MD_P)]],
                'Tr_No_MD':         [0,     0,          ['Tr_No_MD_PE', 'Tr_T_No_MD_HTN'],        [D.PE_P, (1-D.PE_P)]],
                'Tr_No_MD_PE':      [0,     0,          ['Tr_T_No_MD_E', 'Tr_T_No_MD_PE'],        [D.E_P, (1-D.E_P)]],

                #BP MD, NO UA Branch
                'Tr_MD':            [18,     0,            ['Tr_UA', 'Tr_No_UA'],                    [D.UA_P, (1-D.UA_P)]],
                'Tr_No_UA':         [0,     0,             ['Tr_No_UA_PE', 'Tr_T_No_UA_HTN'],        [D.PE_P*D.RR, (1-(D.PE_P*D.RR))]],
                'Tr_No_UA_PE':      [0,     0,             ['Tr_T_No_UA_E', 'Tr_T_No_UA_PE'],        [D.E_P, (1-D.E_P)]],

                #BP, MD, UA, NO MGSO4 Branch
                'Tr_UA':            [12,     0,            ['Tr_UA_PE', 'Tr_T_UA_HTN'],              [D.PE_P*D.RR, (1-(D.PE_P*D.RR))]],
                'Tr_UA_PE':         [0,     0,             ['Tr_MGSO4', 'Tr_No_MGSO4'],              [D.MGSO4_P,  (1-D.MGSO4_P)]],
                'Tr_No_MGSO4':      [0,     0,             ['Tr_T_No_MGSO4_E', 'Tr_T_No_MGSO4_PE'],  [D.E_P, (1-D.E_P)]],

                #All
                'Tr_MGSO4':         [5,    0,              ['Tr_T_MGSO4_E', 'Tr_T_MGSO4_PE'],        [D.E_PMGSO4, (1-D.E_PMGSO4)]],

######SUPPLIES SCENARIO
                'supplies':         [0,     0,          ['sup_BP', 'sup_NoBP'],                     [D.BP_P, (1-D.BP_P)]],
                #NO BP Branch
                'sup_NoBP':         [0,     0,          ['sup_NoBP_HTN', 'sup_T_NoBP_No_HTN'],     [D.HTN_P, (1-D.HTN_P)]],
                'sup_NoBP_HTN':     [0,     0,          ['sup_NoBP_PE', 'sup_T_NoBP_HTN'],         [D.PE_P, (1-D.PE_P)]],
                'sup_NoBP_PE':      [0,     0,          ['sup_T_NoBP_E', 'sup_T_NoBP_PE'],         [D.E_P, (1-D.E_P)]],

                #BP No MD Branch
                'sup_BP':            [0,     0,          ['sup_BP_HTN', 'sup_T_BP_No_HTN'],          [D.HTN_P, (1-D.HTN_P)]],
                'sup_BP_HTN':        [0,     0,          ['sup_MD',  'sup_No_MD'],                   [D.SUP_MD_P, (1-D.SUP_MD_P)]],
                'sup_No_MD':         [0,     0,          ['sup_No_MD_PE', 'sup_T_No_MD_HTN'],        [D.PE_P, (1-D.PE_P)]],
                'sup_No_MD_PE':      [0,     0,          ['sup_T_No_MD_E', 'sup_T_No_MD_PE'],        [D.E_P, (1-D.E_P)]],

                #BP MD, NO UA Branch
                'sup_MD':            [18,    0,          ['sup_UA', 'sup_No_UA'],                    [D.UA_P, (1-D.UA_P)]],
                'sup_No_UA':         [0,     0,          ['sup_No_UA_PE', 'sup_T_No_UA_HTN'],        [D.PE_P*D.RR, (1-(D.PE_P*D.RR))]],
                'sup_No_UA_PE':      [0,     0,          ['sup_T_No_UA_E', 'sup_T_No_UA_PE'],        [D.E_P, (1-D.E_P)]],

                #BP, MD, UA, NO MGSO4 Branch
                'sup_UA':            [12,    0,          ['sup_UA_PE', 'sup_T_UA_HTN'],              [D.PE_P*D.RR, (1-(D.PE_P*D.RR))]],
                'sup_UA_PE':         [0,     0,          ['sup_MGSO4', 'sup_No_MGSO4'],              [D.SUP_MGSO4,  (1-D.SUP_MGSO4)]],
                'sup_No_MGSO4':      [0,     0,          ['sup_T_No_MGSO4_E', 'sup_T_No_MGSO4_PE'],  [D.E_P, (1-D.E_P)]],

                #All
                'sup_MGSO4':         [5,    0,          ['sup_T_MGSO4_E', 'sup_T_MGSO4_PE'],         [D.E_PMGSO4, (1-D.E_PMGSO4)]],
######BOTH SCENARIO
                'both':              [8,     0,          ['both_BP', 'both_NoBP'],                     [D.TR_BP_P, (1-D.TR_BP_P)]],
                #NO BP Branch
                'both_NoBP':         [0,     0,          ['both_NoBP_HTN', 'both_T_NoBP_No_HTN'],     [D.HTN_P, (1-D.HTN_P)]],
                'both_NoBP_HTN':     [0,     0,          ['both_NoBP_PE', 'both_T_NoBP_HTN'],         [D.PE_P, (1-D.PE_P)]],
                'both_NoBP_PE':      [0,     0,          ['both_T_NoBP_E', 'both_T_NoBP_PE'],         [D.E_P, (1-D.E_P)]],

                #BP No MD Branch
                'both_BP':            [0,     0,          ['both_BP_HTN', 'both_T_BP_No_HTN'],          [D.HTN_P, (1-D.HTN_P)]],
                'both_BP_HTN':        [18,    0,          ['both_MD',  'both_No_MD'],                   [D.SUP_MD_P, (1-D.SUP_MD_P)]],
                'both_No_MD':         [0,     0,          ['both_No_MD_PE', 'both_T_No_MD_HTN'],        [D.PE_P, (1-D.PE_P)]],
                'both_No_MD_PE':      [0,     0,          ['both_T_No_MD_E', 'both_T_No_MD_PE'],        [D.E_P, (1-D.E_P)]],

                #BP MD, NO UA Branch
                'both_MD':            [18,    0,          ['both_UA', 'both_No_UA'],                    [D.BOTH_UA, (1-D.BOTH_UA)]],
                'both_No_UA':         [0,     0,          ['both_No_UA_PE', 'both_T_No_UA_HTN'],        [D.PE_P*D.RR, (1-(D.PE_P*D.RR))]],
                'both_No_UA_PE':      [0,     0,          ['both_T_No_UA_E', 'both_T_No_UA_PE'],        [D.E_P, (1-D.E_P)]],

                #BP, MD, UA, NO MGSO4 Branch
                'both_UA':            [12,    0,          ['both_UA_PE', 'both_T_UA_HTN'],              [D.PE_P*D.RR, (1-(D.PE_P*D.RR))]],
                'both_UA_PE':         [0,     0,          ['both_MGSO4', 'both_No_MGSO4'],              [D.SUP_MGSO4,  (1-D.SUP_MGSO4)]],
                'both_No_MGSO4':      [0,     0,          ['both_T_No_MGSO4_E', 'both_T_No_MGSO4_PE'],  [D.E_P, (1-D.E_P)]],

                #All
                'both_MGSO4':         [5,    0,          ['both_T_MGSO4_E', 'both_T_MGSO4_PE'],        [D.E_PMGSO4, (1-D.E_PMGSO4)]]
                };



# dictionary for terminal nodes
#               //key:          cost,   utility
dictTerminals = {'T_NoBP_No_HTN':       [0,     1.0],
                 'T_NoBP_HTN':          [0,     .78],
                 'T_NoBP_PE':           [0,     .4],
                 'T_NoBP_E':            [0,     .1],

                 #NoMD
                 'T_BP_No_HTN':          [0,    1.0],
                 'T_No_MD_HTN':          [0,    .78],
                 'T_No_MD_PE':           [0,    .4],
                 'T_No_MD_E':            [0,    .1],

                 #No UA
                'T_No_UA_HTN':          [0,    .78],
                'T_No_UA_PE':           [0,    .4],
                'T_No_UA_E':            [0,    .1],

                 #UA, No PE
                'T_UA_HTN':             [0,.78],

                #
                'T_No_MGSO4_PE':        [0, .4],
                'T_No_MGSO4_E':         [0, .1],

                #MGSO4
                'T_MGSO4_PE':           [0, .4],
                'T_MGSO4_E':            [0, .1],
#####TRAINING SCENARIO
                 'Tr_T_NoBP_No_HTN':       [0,     1.0],
                 'Tr_T_NoBP_HTN':          [0,     .78],
                 'Tr_T_NoBP_PE':           [0,     .4],
                 'Tr_T_NoBP_E':            [0,     .1],

                 #NoMD
                 'Tr_T_BP_No_HTN':          [0,    1.0],
                 'Tr_T_No_MD_HTN':          [0,    .78],
                 'Tr_T_No_MD_PE':           [0,    .4],
                 'Tr_T_No_MD_E':            [0,    .1],

                 #No UA
                'Tr_T_No_UA_HTN':          [0,    .78],
                'Tr_T_No_UA_PE':           [0, .4],
                'Tr_T_No_UA_E':            [0, .1],

#UA, No PE
                'Tr_T_UA_HTN':             [0,.78],


                'Tr_T_No_MGSO4_PE':        [0, .4],
                'Tr_T_No_MGSO4_E':         [0, .1],

                #MGSO4
                'Tr_T_MGSO4_PE':           [0, .4],
                'Tr_T_MGSO4_E':            [0, .1],

########SUPPLIES SCENARIO
                 'sup_T_NoBP_No_HTN':       [0,     1.0],
                 'sup_T_NoBP_HTN':          [0,     .78],
                 'sup_T_NoBP_PE':           [0,     .4],
                 'sup_T_NoBP_E':            [0,     .1],

                 #NoMD
                 'sup_T_BP_No_HTN':          [0,    1.0],
                 'sup_T_No_MD_HTN':          [0,    .78],
                 'sup_T_No_MD_PE':           [0,    .4],
                 'sup_T_No_MD_E':            [0,    .1],

                 #No UA
                'sup_T_No_UA_HTN':          [0,    .78],
                'sup_T_No_UA_PE':           [0, .4],
                'sup_T_No_UA_E':            [0, .1],

                #UA, No PE
                'sup_T_UA_HTN':             [0,.78],


                'sup_T_No_MGSO4_PE':        [0, .4],
                'sup_T_No_MGSO4_E':         [0, .1],

                #MGSO4
                'sup_T_MGSO4_PE':           [0, .4],
                'sup_T_MGSO4_E':            [0, .1],


########BOTH SCENARIO
                 'both_T_NoBP_No_HTN':       [0,     1.0],
                 'both_T_NoBP_HTN':          [0,     .78],
                 'both_T_NoBP_PE':           [0,     .4],
                 'both_T_NoBP_E':            [0,     .1],

                 #NoMD
                 'both_T_BP_No_HTN':          [0,    1.0],
                 'both_T_No_MD_HTN':          [0,    .78],
                 'both_T_No_MD_PE':           [0,    .4],
                 'both_T_No_MD_E':            [0,    .1],

                 #No UA
                'both_T_No_UA_HTN':          [0,    .78],
                'both_T_No_UA_PE':           [0, .4],
                'both_T_No_UA_E':            [0, .1],

                #UA, No PE
                'both_UA_HTN':             [0,.78],

                'both_T_No_MGSO4_PE':        [0, .4],
                'both_T_No_MGSO4_E':         [0, .1],

                #MGSO4
                'both_T_MGSO4_PE':           [0, .4],
                'both_T_MGSO4_E':            [0, .1]

};


