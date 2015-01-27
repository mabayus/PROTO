#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ply.yacc as yacc

#from variables_classes import *
#from functions_classes import *

from language.problem_class import Problem
from language.variables_classes import VariableDiscrete, ContinuousVariable,\
	Intervalle
from language.functions_classes import Function
from _csv import Error
from language.lexique import tokens


flag_for_error = 0
tab =[]
tmp_liste_descripeur = []
liste_var = {"0":"0"}

liste_of_discrete_variables = {} #cette variable globale est une liste qui contiendra la liste de toutes les variables discrètes qui vont être rencontrées

liste_of_continuous_variables = {} #cette variable globale est une liste qui contiendra la liste de toutes les variables continues qui vont être rencontrées

liste_of_functions = {} #variable contenant la liste des fonctions déclarées

liste_of_random_variables ={}

liste_of_options = [] #contiendra la liste des options. C'est-à-dire tout ce qui est spécifié dans la clause options

#indice_cont_var
#def p_expression_COMMENT (p):
#	'''
#		COMMENT : BEGIN_COMMENT [*] END_COMMENT
#	'''

def init_var():
	global liste_of_discrete_variables
	global liste_of_continuous_variables
	global flag_for_error
	global error_list
	if('liste_of_discrete_variables' in globals()):
		del liste_of_discrete_variables
	if('liste_of_continuous_variables' in globals()):
		del liste_of_continuous_variables	
	if('flag_for_error' in globals()):
		flag_for_error = 0
	if ('error_list' in globals()):
		error_list = []
	liste_of_discrete_variables = {}
	liste_of_continuous_variables = {}
	flag_for_error = 0



def p_expression_DESCRIPTION (p):
	'''
		DESCRIIPTION :	LISTE_DE_CAS_DE_CHARGEMENTS
	|					PROBLEME
	'''

def p_expression_LISTE_DE_CAS_DE_CHARGEMENTS (p):
	'''
		LISTE_DE_CAS_DE_CHARGEMENTS :	PB_LOAD_CASE
	|					PB_LOAD_CASE LISTE_DE_CAS_DE_CHARGEMENTS
	'''

def p_expression_PROBLEME (p):

	#| à rajouter
	'''
		PROBLEME : CLAUSE_VAR CLAUSE_FONCTION CLAUSE_OBJECTIF CLAUSE_CONSTRAINT CLAUSE_OPTIONS
	|	CLAUSE_VAR
	|	CLAUSE_OBJECTIF
	|	CLAUSE_FONCTION
	|	CLAUSE_CONSTRAINT
	|	CLAUSE_OPTIONS
	'''
		
# ******************************************************************************************************************************
#	Pour introduire un cas de chargement, après begin ... le premier DESCRIPTEUR représente le nom du cas de chargement
#	le second qui suit PHENOMENOLOGY donne le type de physique.
#	Puis viennent les différentes clauses.
#*******************************************************************************************************************************

def p_expression_PB_LOAD_CASE (p):
	"""
		PB_LOAD_CASE : BEGIN CLAUSE LOAD_CASE DESCRIPTEUR PHENOMENOLOGY DESCRIPTEUR SOLVER DESCRIPTEUR PROBLEME  END CLAUSE
	|					BEGIN CLAUSE LOAD_CASE DESCRIPTEUR PHENOMENOLOGY DESCRIPTEUR SOLVER DESCRIPTEUR PROBLEME  END CLAUSE LOAD_CASE
	|					BEGIN CLAUSE LOAD_CASE DESCRIPTEUR PHENOMENOLOGY DESCRIPTEUR SOLVER DESCRIPTEUR PROBLEME END CLAUSE LOAD_CASE PB_LOAD_CASE
	"""

#Grammaire de la clause options. Comment une clause options doit être déclarée
def p_expression_CLAUSE_OPTIONS (p):
	'''
		CLAUSE_OPTIONS : BEGIN CLAUSE OPTIONS THE_OPTIONS END CLAUSE OPTIONS
	|			BEGIN CLAUSE OPTIONS THE_OPTIONS END CLAUSE
	'''

#********************************************************************************
#Ici je dis ce que peut être une option. Une option est soit:
#	une option budget de calcul BUDGET_OPTION
#	une option sur le nombre maximal d'itération ITERARTION_OPTIONS
#	une option sur le coût de calcul COST_OPTION
#	une option sur le fonctionnement RUNNING_OPTIONS
#****************************************************************************
def p_expression_THE_OPTIONS (p):
	'''
		THE_OPTIONS :	OPTIMIZER_POLICY
	|					ITERARTION_OPTIONS
	|					ALGORITHMS_CHOICE
	|					BUDGET_OPTIONS
	'''
#	|BUDGET_OPTIONS FIN_INSTRUCTION
#	|			ITERARTION_OPTIONS FIN_INSTRUCTION
#	|			COST_OPTIONS FIN_INSTRUCTION
#	|			ALGORITHMS_CHOICE FIN_INSTRUCTION
#	|			RUNNING_OPTIONS FIN_INSTRUCTION
#	|			OPTIMIZER_SELECTION FIN_INSTRUCTION
#	|			BUDGET_OPTIONS FIN_INSTRUCTION OPTIONS
#	|			ITERARTION_OPTIONS FIN_INSTRUCTION OPTIONS
#	|			COST_OPTIONS FIN_INSTRUCTION OPTIONS
#	|			RUNNING_OPTIONS FIN_INSTRUCTION OPTIONS
#	|			ALGORITHMS_CHOICE FIN_INSTRUCTION OPTIONS
#	|			OPTIMIZER_SELECTION FIN_INSTRUCTION OPTIONS
#	'''
#	p[0] = p[1]

#*****************************************************************************************************
#			Cette option sert à indiquer au collaborative-filtering les critères sur lesquels il doit*
#	se baser pour comparer les algorithmes d'optimisation qui seront adaptés au problème		     *
#*****************************************************************************************************
def p_expression_OPTIMIZER_POLICY (p):
	'''
		OPTIMIZER_POLICY : OPTIMIZER POLICY LISTE_DESCRIPTEUR FIN_INSTRUCTION
	'''
	p[0] = p[1]

#*****************************************************************************************************
#			Cette option sert à fixer à l'optimiseur le nombre maximal d'itérations qu'il dvra faire *
#*****************************************************************************************************
def p_expression_ITERATION_OPTIONS (p):
	'''
		ITERARTION_OPTIONS : MAXIMAL ITERATION NUMBER FIN_INSTRUCTION
	'''
	
	p[0] = str(p[1]) + " " + str(p[2]) + " " + str(p[3])
	liste_of_options.append(p[0])

#************************************************************************************************
#			Cette option sert à indiquer des algorithmes que l'expret aimerait voir tester sur  *
# son problème. 																				*
#************************************************************************************************
def p_expression_ALGORITHM_CHOICE (p):
	'''
		ALGORITHMS_CHOICE : TEST ALGORITHMS LISTE_DESCRIPTEUR FIN_INSTRUCTION
	'''

#************************************************************************************************
#			Cette option permet à l'expert d'allouer un budget de calcul soit pour le problème  *
# soit allouer un budget de calcul par fonction à calculer										*
#************************************************************************************************
def p_expression_BUDGET_OPTIONS (p):
	'''
		BUDGET_OPTIONS :	GLOBAL COMPUTATION BUDGET
	|						FUNCTIONS COMPUTATION BUDGET
	'''

#def p_expression_ITERATION_OPTIONS (p):
#	'''
#		ITERARTION_OPTIONS : MAXIMAL ITERATION NUMBER
#	'''


#-----------------------------------La clause Variables---------------------------------
#C'est dans cette clause qu'on déclare les différentes variables du problème d'optimisation
def p_expression_CLAUSE_VAR (p):
	'''
		CLAUSE_VAR : BEGIN CLAUSE VARIABLES VARIABLES_DECLARATION END CLAUSE VARIABLES
	|		     BEGIN CLAUSE VARIABLES VARIABLES_DECLARATION END CLAUSE
	'''
	#ici les traitements à faire
#	print ("Une clause var")


#-----------------------------------La clause Objectif---------------------------------
def p_expression_CLAUSE_OBJECTIF (p):
	'''
		CLAUSE_OBJECTIF : BEGIN CLAUSE OBJECTIVE L_OBJECTIF END CLAUSE
	|			BEGIN CLAUSE OBJECTIVE L_OBJECTIF END CLAUSE OBJECTIVE
	'''
#	print ("Un ojectif ", p[4])



#-----------------------------------La clause Fonction ---------------------------------
def p_expression_CLAUSE_FONCTION (p):
	'''
		CLAUSE_FONCTION : BEGIN CLAUSE FUNCTION LISTE_FONCTIONS END CLAUSE
	|			  BEGIN CLAUSE FUNCTION LISTE_FONCTIONS END CLAUSE FUNCTION
	'''
#	print ("J'ai une liste de fonction ")


#-------------------------------- Grammaire de la clause Variables---------------------------------
#def p_expression_CLAUSE_OBJECTIF (p):
#	'''
		#CLAUSE_OBJECTIF : BEGIN CLAUSE OBJECTIVE L_OBJECTIF END CLAUSE
#	|			BEGIN CLAUSE OBJECTIVE L_OBJECTIF END CLAUSE OBJECTIVE
#	'''
#	print ("Un ojectif ", p[4])"""


#-------------------------------- Grammaire de la clause contrainte---------------------------------
def p_expression_CLAUSE_CONSTRAINT (p):
	'''
		CLAUSE_CONSTRAINT : BEGIN CLAUSE CONSTRAINT LISTE_CONSTRAINTS END CLAUSE
	|				BEGIN CLAUSE CONSTRAINT LISTE_CONSTRAINTS END CLAUSE CONSTRAINT
	'''
#************************************************************************************************************************************************
#			Là j'écris la grammaire de chaque clause. Comment sera structuré le contenu de chaque bloc				*
#************************************************************************************************************************************************

#---------------------------------------Définition du contenu du bloc VARIABLES_DECLARATION -------------------------------------------------
	
def p_expression_VARIABLES_DECLARATION (p):
	'''
		VARIABLES_DECLARATION : LISTE_DECLARATION_NUMERIC_VARIABLE
	|				LISTE_DECLARATION_CONTINUOUS_VARIABLE 
	|				LISTE_DECLARATION_DISCRETE_VARIABLE
	|				LISTE_DECLARATION_VECTEUR_VARIABLE_CONTINU
	|				DECLARE_A_SEQUENCE_OF_CONTINUOUS_VARIABLES
	|				DECLARE_A_SEQUENCE_OF_DISCRETE_VARIABLES
	|				DECLARATION_RANDOM_VARIABLES
	|				LISTE_DECLARATION_VECTEUR_VARIABLE_DISCRETE
	|				LISTE_DECLARATION_NUMERIC_VARIABLE VARIABLES_DECLARATION
	|				LISTE_DECLARATION_CONTINUOUS_VARIABLE VARIABLES_DECLARATION
	|				LISTE_DECLARATION_DISCRETE_VARIABLE VARIABLES_DECLARATION
	|				LISTE_DECLARATION_VECTEUR_VARIABLE_CONTINU VARIABLES_DECLARATION
	|				LISTE_DECLARATION_VECTEUR_VARIABLE_DISCRETE VARIABLES_DECLARATION
	|				DECLARE_A_SEQUENCE_OF_DISCRETE_VARIABLES VARIABLES_DECLARATION
	|				DECLARE_A_SEQUENCE_OF_CONTINUOUS_VARIABLES VARIABLES_DECLARATION
	|				DECLARATION_RANDOM_VARIABLES VARIABLES_DECLARATION
	'''

#--------------------------------Qu'est ce que c'est qu'une liste de déclaration de variables discrètes-------------------------------------
def p_expression_LISTE_DECLARATION_DISCRETE_VARIABLE (p):
	'''
		LISTE_DECLARATION_DISCRETE_VARIABLE : DECLARATION_DISCRETE_VARIABLE LISTE_DECLARATION_DISCRETE_VARIABLE
		|					DECLARATION_DISCRETE_VARIABLE
	'''

	
def p_expression_LISTE_DECLARATION_NUMERIC_VARIABLE (p)	:
	'''
		LISTE_DECLARATION_NUMERIC_VARIABLE : 	DECLARATION_NUMERIC_VARIABLE
	|						DECLARATION_NUMERIC_VARIABLE LISTE_DECLARATION_NUMERIC_VARIABLE
	'''
	

#------------------------------Une liste de déclaration de variables continues ----------------------------------------------
def p_expression_LISTE_DECLARATION_CONTINUOUS_VARIABLE (p):
	'''
		LISTE_DECLARATION_CONTINUOUS_VARIABLE : DECLARATION_CONTINUOUS_VARIABLE 
		|					DECLARATION_CONTINUOUS_VARIABLE FIN_INSTRUCTION LISTE_DECLARATION_CONTINUOUS_VARIABLE
	'''
	
#-----------------------------------------------------------------------------------------------------------------
#			Il arrive qu'une variable soit en fait un vecteur de variables. Exemple Xpeau = (v1,v2,v3,v4,v5,v6)
#-----------------------------------------------------------------------------------------------------------------
def p_expression_LISTE_DECLARATION_VECTEUR_VARIABLE_CONTINU (p):
	'''
		LISTE_DECLARATION_VECTEUR_VARIABLE_CONTINU : 	DECLARATION_VECTEUR_VARIABLE_CONTINU 
		|						DECLARATION_VECTEUR_VARIABLE_CONTINU LISTE_DECLARATION_VECTEUR_VARIABLE_CONTINU
	'''

	
def p_expression_LISTE_DECLARATION_VECTEUR_VARIABLE_DISCRETE (p):
	'''
		LISTE_DECLARATION_VECTEUR_VARIABLE_DISCRETE : 	DECLARATION_VECTEUR_VARIABLE_DISCRETE 
		|						DECLARATION_VECTEUR_VARIABLE_DISCRETE LISTE_DECLARATION_VECTEUR_VARIABLE_DISCRETE
	'''


def p_expression_DECLARATION_NUMERIC_VARIABLE (p):
	'''
		DECLARATION_NUMERIC_VARIABLE :	DESCRIPTEUR FIN_INSTRUCTION
		|				DESCRIPTEUR SIGNE_EGAL NOMBRE FIN_INSTRUCTION
	'''
	
#******************************************************************************************************************************
#	Déclarer une variable aléatoire
#	pour déclarer z qui est une variable aléatoire suivant la loit normale de moyenne 2 et d'ecart-type 1.5, il faut écrire:   *
#		random z follows normal (2, 1.5)
#*******************************************************************************************************************************

def p_expression_DECLARATION_RANDOM_VARIABLES(p):
	'''
		DECLARATION_RANDOM_VARIABLES : RANDOM DESCRIPTEUR FOLLOWS PROBABILITY_DISTRIBUTION OPEN_PAR NOMBRE VIRGULE NOMBRE CLOSE_PAR FIN_INSTRUCTION
	'''

	liste_of_random_variables[p[2]] = p[3] + " " + str(p[5]) + str(p[6]) + str(p[7]) + str(p[8])
	


#*********************************************************************************************
#				Grammaire pour déclarer une variable discrete							
#*********************************************************************************************
def p_expression_DECLARATION_DISCRETE_VARIABLE (p):
	'''
		DECLARATION_DISCRETE_VARIABLE : DISCRETE DESCRIPTEUR IN LISTE_NOMBRE FIN_INSTRUCTION
		|				DISCRETE DESCRIPTEUR FIN_INSTRUCTION
		|				DISCRETE DESCRIPTEUR IS CARACTERISTIQUE FIN_INSTRUCTION
		|				DISCRETE DESCRIPTEUR IN LISTE_NOMBRE IS CARACTERISTIQUE FIN_INSTRUCTION
	'''
	
	#Je vérifie qu'une variable de même nom n'existe pas déjà.
	if( (p[2] in liste_of_discrete_variables.keys()) or (p[2] in liste_of_continuous_variables.keys()) ):
		#Une variable de même nom existe. Je lève une exception.
		raise NameError("Erreur. Une variable de nom \"%s\" existe déja" % p[2])
	else:
		# Aucune variable du même nom n'existe
		global tab
		tab = []
		the_discrete_var = 0
		#les traitements vont consister ici à créer une variable discrète
		if( (p[3].lower() )== 'in'): #lorsque p[3] vaut IN , la liste de nombre est fournie. Je peux donc créer la variable avec toute la liste disponible
			the_discrete_var = VariableDiscrete(p[2], p[4])
		else:
			'''
				La liste autorisée n'est pas fournie. Je crée la variable avec juste son nom
			'''
				
			the_discrete_var = VariableDiscrete(p[2])
					
			p[0] = the_discrete_var #je renvoie la variable discrète créée
			liste_of_discrete_variables[p[2]] = p[0] #j'ajoute la variable actuelle à la liste des variabls discrètes connues
			print ("La variable discrète créée est : %s" %p[0])

#Grammaire pour déclarer une variable continue
def p_expression_DECLARATION_CONTINUOUS_VARIABLE (p):
	'''
		DECLARATION_CONTINUOUS_VARIABLE : CONTINUOUS DESCRIPTEUR FIN_INSTRUCTION
		|				CONTINUOUS DESCRIPTEUR IS CARACTERISTIQUE FIN_INSTRUCTION
		|				CONTINUOUS DESCRIPTEUR IN INTERVALLE FIN_INSTRUCTION
		|				CONTINUOUS DESCRIPTEUR IN INTERVALLE IS CARACTERISTIQUE FIN_INSTRUCTION
		|				CONTINUOUS DESCRIPTEUR FIN_INSTRUCTION DECLARATION_CONTINUOUS_VARIABLE
		|				CONTINUOUS DESCRIPTEUR IN INTERVALLE FIN_INSTRUCTION DECLARATION_CONTINUOUS_VARIABLE
	'''
	
	#traitements à effectuer lorsque je rencontre une variable continue.
	#	continuous_var = ContinuousVariable (p[2])
	print("Try Cont Var %s"%p[2])
	if( (p[2] in liste_of_discrete_variables.keys()) or (p[2] in liste_of_continuous_variables.keys()) ):
		#Une variable de même nom existe. Je lève une exception.
		raise NameError("Erreur. Une variable de nom \"%s\" existe déja" % p[2])
	else:
		if (p[3].lower() == 'in'):
			continuous_var = ContinuousVariable (p[2], p[4].lowerBound, p[4].upperBound)#je crée une variable continue avec les paramètres disponibles
			liste_of_continuous_variables[p[2]] = continuous_var #j'ajoute la nouvelle variable continue créée à la liste existante
			
			p[0] = continuous_var
	#			global liste_var
	#			liste_var[p[2]] = continuous_var
	#			print ( "Yes ")
	#			print ("liste var: %s " %(liste_var[p[2]]) )
		else:
			continuous_var = ContinuousVariable(p[2])
			liste_of_continuous_variables[p[2]] = continuous_var
	#			liste_var.append (p[2] : )


#grammaire pour déclarer un paramètre qui est un vecteur d'autres paramètres.
def p_expression_DECLARATION_VECTEUR_VARIABLE_DISCRETE (p):
	'''
		DECLARATION_VECTEUR_VARIABLE_DISCRETE : VECTOR DESCRIPTEUR OPEN_PAR LISTE_DESCRIPTEUR CLOSE_PAR IS DISCRETE IN LISTE_NOMBRE FIN_INSTRUCTION
	|					VECTOR DESCRIPTEUR OPEN_PAR LISTE_DESCRIPTEUR CLOSE_PAR IS DISCRETE IN LISTE_NOMBRE IS CARACTERISTIQUE FIN_INSTRUCTION
	'''
	print("Try Disc Var %s" %p[2])
	global tmp_liste_descripeur
	tmp_liste_descripeur =[] #réinitialistaion de la liste itérative
	p[0] = {}
	vecteur_var = []
	for val in p[4]:
		var_tmp = VariableDiscrete(val, p[9])
		liste_of_discrete_variables[val] = var_tmp
		vecteur_var.append(var_tmp)
		
	p[0] = vecteur_var
#		print ("LLLL %s "%p[0])
		

# Règle de grammaire pour déclarer v1,v2,....,vn qui sont des variables discrètes à valeur dans une suite de valeurs
def p_expression_DECLARE_A_SEQUENCE_OF_DISCRETE_VARIABLES (p):
	'''
		DECLARE_A_SEQUENCE_OF_DISCRETE_VARIABLES :	LISTE_DESCRIPTEUR ARE DISCRETE IN LISTE_NOMBRE FIN_INSTRUCTION
	|						LISTE_DESCRIPTEUR ARE DISCRETE IN LISTE_NOMBRE IS CARACTERISTIQUE FIN_INSTRUCTION
	'''
	for nom_des_variables in p[1]:
		''' 
			p[1] (un tableau) contient le nom des variables à créer. Là je le parcours et je crée les variables
			si une variable du même nom n'existe pas.
		'''
		global liste_of_discrete_variables
		global liste_of_continuous_variables
		if ( (nom_des_variables not in liste_of_discrete_variables.keys()) and (nom_des_variables not in liste_of_continuous_variables)):
			# Aucune variable portant le nom donné n'existe
			variable_discrete = VariableDiscrete ( nom_des_variables, p[5])
			liste_of_discrete_variables[nom_des_variables] = variable_discrete
		else:
			# Une variable du même nom existe
			return NameError("Une variable de nom %s existe déjà" %nom_des_variables)
	

def p_expression_DECLARE_A_SEQUENCE_OF_CONTINUOUS_VARIABLES (p) :
	'''
		DECLARE_A_SEQUENCE_OF_CONTINUOUS_VARIABLES :	LISTE_DESCRIPTEUR ARE CONTINUOUS IN INTERVALLE FIN_INSTRUCTION
	|													LISTE_DESCRIPTEUR ARE CONTINUOUS IN INTERVALLE ARE CARACTERISTIQUE FIN_INSTRUCTION
	'''
	global liste_of_discrete_variables
	global liste_of_continuous_variables
	for nom_des_variables in p[1] :
		'''
			p[1] (un tableau) contient le nom des variables à créer. Là je le parcours et je crée les variables
			si une variable du même nom n'existe pas.
		'''
		if ( (nom_des_variables not in liste_of_discrete_variables.keys()) and (nom_des_variables not in liste_of_continuous_variables)):
			variable_continue = ContinuousVariable ( nom_des_variables, p[5])
			liste_of_continuous_variables[nom_des_variables] = variable_continue
		else:
			raise (NameError("Une variable de nom %s existe déjà" %nom_des_variables))
		

def p_expression_DECLARATION_VECTEUR_VARIABLE_CONTINU (p):
	'''
		DECLARATION_VECTEUR_VARIABLE_CONTINU : VECTOR DESCRIPTEUR OPEN_PAR LISTE_DESCRIPTEUR CLOSE_PAR IS CONTINUOUS IN INTERVALLE FIN_INSTRUCTION
	|					VECTOR DESCRIPTEUR OPEN_PAR LISTE_DESCRIPTEUR CLOSE_PAR IS CONTINUOUS IN INTERVALLE IS CARACTERISTIQUE FIN_INSTRUCTION
	'''
	global liste_of_discrete_variables
	global liste_of_continuous_variables
	global tmp_liste_descripeur
	tmp_liste_descripeur =[] #réinitialistaion de la liste
	vecteur_var = [] #tableau qui contiendra le vecteur quib sera créé.
		
	if ( (p[2] not in liste_of_continuous_variables) and ( p[2] not in liste_of_discrete_variables.keys())):#je vérifie qu'une variable de ce nom existe ou pas	
		
			#Je parcours le vecteur de variables et je crée une variable continues que j'ajoute à la liste globale de variables continues
		for val in p[4]:
			if ( (val not in liste_of_continuous_variables) and ( val not in liste_of_discrete_variables.keys())):
				var_tmp = ContinuousVariable(val, p[9].lowerBound, p[9].upperBound)
				liste_of_continuous_variables[val] = var_tmp
				vecteur_var.append(var_tmp)
			else:
				return ( NameError("Une variable de ce nom %s existe déjà" %val))
		p[0] = vecteur_var
			
	else:
		return ( NameError("Une variable de ce nom %s existe déjà" %p[2]))


#--------------------	-------------------------------------------------------------------------------------------------------------------------------





#--------------------------------------------------------Définition du bloc FUNCTION---------------------------------------------------------------


def p_expression_LISTE_FONCTIONS (p): #définition d'une liste de fonctions
#une liste de fonctions est soit une fonction soit une fonction suivie d'une liste de fonctions (pour pouvoir en aligner plusieurs)
	'''
		LISTE_FONCTIONS : LIGNE_COMMENTE LISTE_FONCTIONS
	|			FONCTION FIN_INSTRUCTION 
	|			FONCTION FIN_INSTRUCTION LISTE_FONCTIONS
	'''
	

def p_expression_FONCTION (p):# ce que c'est qu'une fonction
#une fonction est soit une fonction numérique soit un code de calcul contenu dans un fichier, soit une fonction externe
	'''
		FONCTION :	FONCTION_NUMERIQUE
	|				CODE_CALCUL_FICHIER
	|				CODE_CALCUL_BOITE_NOIRE
	|				EXTERNAL_FUNCTION
	|				DERIVATIVE_FONCTION
	|				SIMPLE_FONCTION
	'''
	p[0] = p[1]

#------------------------- Les fonctions simples--------------------
def p_EXPRESSION_SIMPLE_FONCTION (p):
	'''
		SIMPLE_FONCTION : DESCRIPTEUR
		
	'''
	
	
#Grammaire des fonctions numériques
def p_expression_FONCTION_NUMERIQUE (p): #fonction numérique f (c,v,n) = a*x + b*x + c
	'''
		FONCTION_NUMERIQUE : DESCRIPTEUR OPEN_PAR VARS CLOSE_PAR SIGNE_EGAL COMBINED_TERME
	|				DESCRIPTEUR OPEN_PAR VARS CLOSE_PAR
	'''
#	print ("J'ai une fonction")


def p_expression_CODE_CALCUL_FICHIER (p):

# Cette règle représente les codes de calcul fournis par l'utilisateur et contenu dans un fichier
# Le solveur est en fait une fonction que le user code dans en précisant les paramètres d'entrées et de sortie
#exemple resoudre (/home/dubois/resolution.py, (a1,...,a9), (s1,...,s5), /home/bvn/resoudre.job)

#CODE_CALCUL_FICHIER : DESCRIPTEUR OPEN_PAR CHEMIN VIRGULE OPEN_PAR VARS CLOSE_PAR VIRGULE OPEN_PAR VARS CLOSE_PAR VIRGULE CHEMIN CLOSE_PAR
#DESCRIPTEUR OPEN_PAR DESCRIPTEUR VIRGULE INTERVALLE VIRGULE LISTE_NOMBRE

	'''
		CODE_CALCUL_FICHIER : DESCRIPTEUR OPEN_PAR DESCRIPTEUR VIRGULE OPEN_PAR VARS CLOSE_PAR VIRGULE OPEN_PAR VARS CLOSE_PAR VIRGULE DESCRIPTEUR CLOSE_PAR
	
	|				DESCRIPTEUR OPEN_PAR DESCRIPTEUR VIRGULE INTERVALLE VIRGULE LISTE_NOMBRE
	'''

	

def p_expression_CODE_CALCUL_BOITE_NOIRE (p):
#CODE_CALCUL_BOITE_NOIRE : SOLVEUR OPEN_PAR CHEMIN VIRGULE CHEMIN VIRGULE DESCRIPTEUR VIRGULE CHEMIN CLOSE_PAR
#SOLVEUR OPEN_PAR DESCRIPTEUR CLOSE_PAR

	'''
		CODE_CALCUL_BOITE_NOIRE : SOLVER DESCRIPTEUR OPEN_PAR DESCRIPTEUR VIRGULE DESCRIPTEUR CLOSE_PAR
	|				SOLVER OPEN_PAR DESCRIPTEUR CLOSE_PAR
	'''
	
	# Le code de calcul est dans ce cas une boite noire i.e un solveur
	
	# Dans ce cas, l'utilisateur fournit soit: le nom du préprocesseur, le chemin vers le fichier job, le nom du solveur puis le postprocesseur et la liste des outputs (fonctions)
	
	#soit seuleument le solveur.

	
	
#Grammaire des fonctions externes
def p_expression_EXTERNAL_FUNCTION (p):
	'''
		EXTERNAL_FUNCTION : EXTERNAL FUNCTION DESCRIPTEUR INPUT OPEN_PAR LISTE_PARAMETERS CLOSE_PAR OUTPUT OPEN_PAR LISTE_OUTPUT CLOSE_PAR 
	'''


#Grammaire des fonctions qui sont la dérivée d'une autre fonction
# f = derivative (g). g devant être au préalable définie
def p_expression_DERIVATIVE_FUNCTION (p):
	'''
		DERIVATIVE_FONCTION : DESCRIPTEUR SIGNE_EGAL DERIVATIVE OPEN_PAR DESCRIPTEUR CLOSE_PAR
	'''
	
	if (p[1] in liste_of_functions.keys()):
		raise NameError("Conflit.\nUne fonction nommée %s a déja été déclarée")
	elif (p[5] not in liste_of_functions):
		raise NameError ("La fonction %s doit préalablement être déclarée" %p[5])
	else:
		fon = Function(p[1], p[1] + " "+ p[2] + " " + p[3] +" "+ p[4] +" "+ p[5] + " "+p[6])
		p[0] = fon




def p_expression_LISTE_PARAMETERS (p):
	'''
		LISTE_PARAMETERS :  DESCRIPTEUR
	|				DESCRIPTEUR VIRGULE LISTE_PARAMETERS
	'''

def p_expression_LISTE_OUTPUT (p):
	'''
		LISTE_OUTPUT : TYPE DESCRIPTEUR
	|			TYPE DESCRIPTEUR VIRGULE LISTE_OUTPUT
	'''


def p_expression_LIGNE_COMMENTE (p):
	'''
		LIGNE_COMMENTE : BEGIN_COMMENT END_COMMENT
	'''
#	print ("Ceci est une ligne commentée")


def p_expression_COMBINED_TERME (p):
	'''
		COMBINED_TERME :	TERME OPERATEUR TERME
	'''
	p[0] = str(p[1]) +  str(p[2]) + str(p[3])

def p_expression_TERME (p):
	'''
		TERME : SIMPLE_TERME
	|			TERME_COSINUS
	|			TERME_SINUS
	|			TERME_TANGENTE
	|			SQUARED_TERME
	|			SQUARE_ROOT
	|			POWERED_TERME
	|			ARGMIN_TERME
	|			NUMBER
	|			DESCRIPTEUR
	'''

def p_expression_SIMPLE_TERME (p):
	'''
		SIMPLE_TERME : DESCRIPTEUR OPERATEUR DESCRIPTEUR
	'''

def p_expression_TERME_SINUS (p):
	'''
		TERME_SINUS : SIN OPEN_PAR TERME CLOSE_PAR
	'''
	
def p_expression_TERME_COSINUS (p):
	'''
		TERME_COSINUS : COS OPEN_PAR TERME CLOSE_PAR
	'''

def p_expression_TERME_TANGENTE (p):
	'''
		TERME_TANGENTE : TANG OPEN_PAR TERME CLOSE_PAR
	'''

def p_expression_SQUARED_TERME (p):
	'''
		SQUARED_TERME : SQR OPEN_PAR TERME CLOSE_PAR
	'''
	
def p_expression_SQUARE_ROOT (p):
	'''
		SQUARE_ROOT : SQRT OPEN_PAR TERME CLOSE_PAR
	'''
	
def p_expression_POWERED_TERME (p):
	'''
		POWERED_TERME : POW OPEN_PAR TERME CLOSE_PAR
	'''

def p_expression_ARGMIN_TERME (p) :
	'''
		ARGMIN_TERME : ARGMIN OPEN_PAR TERME CLOSE_PAR
	'''
	
def p_expression_operateur (p):
	'''
		OPERATEUR : ADD_OP
	|		MUL_OP
	'''
	p[0] = p[1]

#----------------------------------------------------------------------------------------------------------------------------------------------------

#def p_expression_VALUE (p):
#	'''
#		VALUE : NUMBER
#	|		FLOAT
#	|		LISTE_NOMBRE
#	|		INTERVALLE
#	'''
	
	#les traitements
#	print ("Une valeur", p[1])



def p_expression_LISTE_NOMBRE (p):
	'''
		LISTE_NOMBRE : OPEN_PAR L_NOMBRE CLOSE_PAR
	'''
	p[0] = p[2]
	

	
def p_expression_INTERVALE (p):
	'''
		INTERVALLE : OPEN_CROCHET NOMBRE VIRGULE NOMBRE CLOSE_CROCHET
	'''
	#les actions
	
	#chaque fois que je rencontre un intervalle, je crée un objet Intervalle et je le renvoie.
	intervl = Intervalle(p[2], p[4]) #création de l'objet Intervalle
	p[0] = intervl #renvoie de l'objet Intervalle créé
	print (p[0])


def p_expression_VARS (p):
	'''
		VARS : DESCRIPTEUR
	|		DESCRIPTEUR VIRGULE VARS
	'''

def p_expression_NOMBRE (p):
	'''
		NOMBRE : NUMBER 
		|        FLOAT
	'''
#	print ("Un nombre: ",p[1])
	p[0] = p[1]




#-------------------------------------------Définition du contenu de la clause objectif---------------------------------------------
	
def p_expression_L_OBJECTIF (p): #liste d'objectifs.
#une liste d'objectifs est soit un objectif soit un objectif suivi d'une liste d'objectifs.
	'''
		L_OBJECTIF : OBJECTIF FIN_INSTRUCTION
	|			OBJECTIF FIN_INSTRUCTION L_OBJECTIF
	'''
	

def p_expression_OBJECTIF (p):
#un objectif est de la forme un critère (minimiser
	'''
		OBJECTIF : PENALTY FONCTION
	|		PENALTY DESCRIPTEUR
	'''
	#actions
	
#	print ("L'objectif est: ",p[1]," ",p[2])

#----------------------------------------------------------------------------------------------------------------------------
#def p_expression_INIT (p):
#	'''
#	'''
	
	
#def p_expression_STOP (p):
#	'''
#	'''


#------------------------------------Détails sur les contraintes ---------------------------------------------------
	
def p_expression_LISTE_CONSTRAINTS (p):
	'''
		LISTE_CONSTRAINTS : CONSTRAINTS FIN_INSTRUCTION
	|				CONSTRAINTS FIN_INSTRUCTION LISTE_CONSTRAINTS
	'''


def p_expression_CONSTRAINTS (p):
	'''
		CONSTRAINTS : FONCTION SIGNE_COMPARAISON FONCTION
	|			FONCTION SIGNE_COMPARAISON DESCRIPTEUR
	|			DESCRIPTEUR SIGNE_COMPARAISON FONCTION
	|			FONCTION SIGNE_COMPARAISON NOMBRE
	|			NOMBRE SIGNE_COMPARAISON FONCTION
	|			NOMBRE SIGNE_COMPARAISON DESCRIPTEUR
	|			DESCRIPTEUR SIGNE_COMPARAISON NOMBRE
	|			DESCRIPTEUR IN ENSEMBLE
	|			DESCRIPTEUR SIGNE_COMPARAISON DESCRIPTEUR OPERATEUR NOMBRE
	|			DESCRIPTEUR OPERATEUR NOMBRE SIGNE_COMPARAISON DESCRIPTEUR
	|			DESCRIPTEUR IN INTERVALLE
	|			FONCTION IN INTERVALLE
	|			FONCTION SIGNE_COMPARAISON FONCTION SIGNE_COMPARAISON FONCTION
	|			FONCTION SIGNE_COMPARAISON FONCTION SIGNE_COMPARAISON NOMBRE
	|			NOMBRE SIGNE_COMPARAISON FONCTION SIGNE_COMPARAISON NOMBRE
	'''

def p_expression_SIGNE_COMPARAISON (p):
	'''
		SIGNE_COMPARAISON : SIGNE_SUP
	|			SIGNE_INF
	|			SIGNE_SUP_EGAL
	|			SIGNE_INF_EGAL
	'''
	#début des traitemetns.
	'''
		Les traitements vont consister ici à renvoyer le signe qui de comparaison rencontré
	'''
	p[0] = p[1]
#-------------------------------------------------------------------------------------------------


#-----------------------------------Quelques autres définitions--------------------------------------

def p_expression_ENSEMBLE (p): #ce que c'est qu'un ensemble
	'''
		ENSEMBLE : OPEN_ACCOLADE NOMBRE VIRGULE L_NOMBRE CLOSE_ACCOLADE
	'''

#--------------------Définition d'une liste de nombres---------------
def p_expression_L_NOMBRE (p):
	'''
		L_NOMBRE : NOMBRE VIRGULE L_NOMBRE
	|	NOMBRE
	'''
	global tab
	tab.append(p[1])
	p[0] = tab.reverse()
	
#---------------------Définition d'une liste de descripteurs------------------
def p_expression_LISTE_DESCRIPTEUR(p):
	'''
		LISTE_DESCRIPTEUR : DESCRIPTEUR VIRGULE LISTE_DESCRIPTEUR
		|			DESCRIPTEUR
	'''
	global tmp_liste_descripeur
	tmp_liste_descripeur.append(p[1])
	p[0] = tmp_liste_descripeur
	p[0].reverse()
	
error_list =[]

def p_error(p): 
	global flag_for_error
	flag_for_error = 1
	global error_list 
	error_list.append ("Erreur de syntaxe sur la ligne %d" % (p.lineno - 1))
#	print ("Erreur de syntaxe sur la ligne %d" % (p.lineno))
	yacc.errok()


yacc.yacc(outputdir = 'generated')

def parseInput (parserIn):
	#print(input)
	init_var()
	try:
		parser = yacc.yacc()
		parser.parse( parserIn) #Cette ligne lance le parsing de l'input
		print ("J'ai fini de parser")
		global flag_for_error
		if (flag_for_error == 1):
			print("Flag vaut 1")
			global error_list
			error_list = list ( set(error_list))
			parseResult = [1, error_list]
			return parseResult
		elif (flag_for_error == 0):
			print("Flag vaut 0")
			instance_of_problem = Problem (dict( list(liste_of_continuous_variables.items()) + list(liste_of_discrete_variables.items())), liste_of_functions)
			instance_of_problem = Problem (liste_of_discrete_variables, liste_of_continuous_variables, liste_of_functions)
			parseResult = [0, instance_of_problem]
			return parseResult
		else:
			return Exception("Erreur inconnue")
	except Exception as e:
		return e 


#if __name__ == "__main__":
#	import sys
#	import platform
#	prog = 0
	
	#le if me sert à gérer les versions de python de l'utilisateur.
	#la fonction file n'existe plus avec python3. Elle est remplacée par la fonction open
#	if ( platform.python_version_tuple()[0] == '3'):
		#global prog
#		prog = open(sys.argv[1]).read()
#	elif ( platform.python_version_tuple()[0] == '2' ):
		#global prog
#		prog = file(sys.argv[1]).read()
#	result = yacc.parse(prog)
#	print (result)
	

	# %s" %(liste_of_continuous_variables))
#	print ("Les variables discrètes sont: %s" %(liste_of_discrete_variables))
	
#	if ( liste_of_continuous_variables):
#		print ("Les variables continues sont: ")
#		for nom_var in liste_of_continuous_variables.keys() :
#			print (nom_var, " : ", liste_of_continuous_variables[nom_var])
#			print ()
#	else:
#		print ("Aucune variable continue")
#	if (liste_of_discrete_variables) :
#		print ("Les variables continues sont: ")
#		for nom_var in liste_of_discrete_variables.keys() :
#			print (nom_var, " : ", liste_of_discrete_variables[nom_var])
#	else:
#		print ("Aucune variable discrète")