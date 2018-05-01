import Decision_TreeSA1 as tree

myDT = tree.dt.DecisionNode('d1', 1, tree.dictDecisions, tree.dictChances, tree.dictTerminals)

# print the expected cost and utility of each alternative
print('\nExpected cost and utility:')
print(myDT.get_cost_utility())

# print the probability of terminal nodes under each alternative
print('\nProbabilities of terminal nodes:')
print(myDT.get_terminal_prob())

# plot the expected cost and utility of each alternative
tree.dt.graph_outcomes(myDT)
