#-*- coding: utf-8 -*-

class Problem (object):
	def __init__(self, list_disc_variables={}, list_cont_var = {}, list_functions={}, list_constraint={}, list_objective={}):
		list_of_continuous_variables = list_disc_variables
		list_of_continuous_variables = list_cont_var
		list_of_functions = list_functions
		list_of_constraints = list_constraint
		list_of_objectives = list_objective
	
	def __str__(self):
		#,self.list_of_functions, self.list_of_constraints, self.list_of_objectives))
		return "Les variables: "+ str(self.list_of_variables)