#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ply.lex as lex
import re #c'est une bibliothèque python manipulant des expressions régulières

#path_regular_exp = r"[a-zA-Z]+:(\[a-zA-Z0-9]) | [a-zA-Z]+(\[a-zA-Z0-9])+"

les_types = ['discret', 'continu', 'mixte', 'aleatoire']

penalties = ['min', 'max']

probability_distribution = ['uniform', 'poisson','gamma', 'beta', 'normal', 'chiSquared','bernoulli','binomial','geometric','hypergeometric','exponential']


les_caracteristiques = ['thickness','form', 'length','none','mesurement']

#J'ajoute ici des mots clés au besoins
reserved = {
	"variables" : "VARIABLES",
	
	"load_case" : "LOAD_CASE",
	
	"objective" : "OBJECTIVE",
	
#	"Init" : "INIT",
	
#	"Stop" : "STOP",
	
	"external": "EXTERNAL",
	
	"constraint" : "CONSTRAINT",
	
	"function" : "FUNCTION",
	
	"discrete" : "DISCRETE",
	
	"continuous" : "CONTINUOUS",
	
	"random" :"RANDOM",
	
#	"Domain" : "DOMAIN",
	
#	"Report" : "REPORT",
	
#	"Export" : "EXPORT",
	
	"options" : "OPTIONS",

#	"solveur" : "SOLVEUR",
	
	"begin" : "BEGIN",
	
	"end" : "END",
	
	"clause" : "CLAUSE",
	
	"/*" : "BEGIN_COMMENT",
	
	"*/" : "END_COMMENT",
	
	"is" : "IS",
	
	"in" : "IN",
	
	"are" : "ARE",
	
	"input" : "INPUT",
	
	"output": "OUTPUT",
	
	"type" : "TYPE",
	
	"solver" : "SOLVER",
	
	"derivative" : "DERIVATIVE",
	
	"vector"  : "VECTOR",
	
	"maximal" : "MAXIMAL",
	
#	"minimal" : "MINIMAL",
	
	"iteration" : "ITERATION",
	
	"global"  : "GLOBAL",
	
	"functions" : "FUNCTIONS",
	
	"computation" : "COMPUTATION",
	
	"budget"  : "BUDGET",
	
	"phenomenology" : "PHENOMENOLOGY",
	
	"test" : "TEST",
	
	"optimizer" : "OPTIMIZER",
	
	"policy" : "POLICY",
	
	"algorithms" : "ALGORITHMS",
	
	"follows" : "FOLLOWS",
	
#	"probability_distribution" : "PROBABILITY_DISTRIBUTION",
	
	"sin" : "SIN",
	"cos" : "COS",
	"pow" : "POW",
	"sqr" : "SQR",
	"sqrt" : "SQRT",
	"tang" : "TANG",
	"argmin" : "ARGMIN"
	
	}

tokens = [
		'FIN_INSTRUCTION',
		'NUMBER',
		'FLOAT', 
		'OPEN_PAR',
		'CLOSE_PAR',
		'OPEN_CROCHET',
		'CLOSE_CROCHET',
		'OPEN_ACCOLADE',
		'CLOSE_ACCOLADE',
		'DESCRIPTEUR',
		'CARACTERISTIQUE',
		'PENALTY',
		'VIRGULE',
		'SIGNE_EGAL',
		'SIGNE_INF_EGAL',
		'SIGNE_SUP_EGAL',
		'SIGNE_SUP',
		'SIGNE_INF',
		'ADD_OP',
		'MUL_OP',
		'PROBABILITY_DISTRIBUTION'
	] + list (reserved.values())

#Je commence par définir chaque mot clé chaque élément
#def t_COMMENT_LINE(t):
#    r'\#.*'
#    pass

def t_PENALTY (t):
	r'min | max'
#	penalties = ['min', 'max']
	
	if ( (t.value).lower() in penalties):
		t.type = "PENALTY"
	return t


t_SIGNE_EGAL = r'='

t_VIRGULE = r','

t_ADD_OP =r'\+ | -'

t_MUL_OP = r'\* | /'

t_CARACTERISTIQUE = r' Epaisseur | Forme '

t_FIN_INSTRUCTION = r';'

t_OPEN_PAR = r'\('

t_CLOSE_PAR = r'\)'

t_OPEN_CROCHET = r'\['

t_CLOSE_CROCHET = r'\]'

t_OPEN_ACCOLADE = r'{'

t_CLOSE_ACCOLADE = r'}'

t_SIGNE_INF_EGAL = r'<='
t_SIGNE_SUP_EGAL = r'>='

t_SIGNE_INF = r'<'

t_SIGNE_SUP = r'>'

t_ignore = ' \t' #j'ignore les espaces


#t_CHEMIN = r'[a-zA-Z\\/a-zA-Z0-9][\\/:a-zA-Z0-9_.]+'

def t_DESCRIPTEUR (t):
	#lorsque j'ai une chaine, je vérifie s'il s'agit d'un mot réservé, d'un critère ou d'un type.
	#si c'est le cas, je renvoie le type qui va avec.
	
	r'[a-zA-Z][a-zA-Z0-9_./"\']*'
	if ( reserved.get((t.value).lower()) ) :
		t.type = reserved.get((t.value).lower())
	elif ( t.value.lower() in les_types ):
		t.type = "TYPE"
	elif ( t.value.lower() in penalties ):
		t.type = "PENALTY"
	elif ( t.value.lower() in les_caracteristiques ):
		t.type = "CARACTERISTIQUE"
	elif (t.value.lower() in probability_distribution):
		t.type = "PROBABILITY_DISTRIBUTION"
	else:		
		t.type = "DESCRIPTEUR"
	
	return t


def t_FLOAT (t):
	r'-?\d+\.\d*(e-?\d+)?' 
	t.value = float (t.value)
	return t


def t_NUMBER (t):
	r'\d+'
	t.value = int (t.value)
	return t



def t_newline(t):
	r'\n+'
	t.lexer.lineno += len(t.value)


def t_error(t):
	print ("Illegal character '%s'" %t.value[0])
	t.lexer.skip(1)

lex.lex()

if __name__ == "__main__":
	import sys
	import platform
	prog = 0
	if ( platform.python_version_tuple()[0] == '3'):
		prog = open (sys.argv[1]).read()
	elif ( platform.python_version_tuple()[0] == '2' ):
		pass#prog = file(sys.argv[1]).read()
	lex.Lexer.input(prog)
	
	while 1:
		tok = lex.Lexer.token()
		if not tok: break
		print ("line %d: %s(%s)" %(tok.lineno, tok.type, tok.value))