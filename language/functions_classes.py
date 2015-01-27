'''
Created on 16 juil. 2014

@author: georges
'''
#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Function(object):
    def __init__(self, name = "function", express ="none", param ={}):
        self.name = name
        self.parameters = param
        self.expression = express
    
    def __str__(self):
        return ("Fonction %s\nParamètres %s" %(self.name, self.parameters))


class Constraint (Function):
    def __init__(self, param ={}, exp='', maj = 0, min = 0):
        self.parameters = param
        self.expression = exp
        self.majorant = maj
        self.minorant = min
    
    def __str__(self):
        return ("La Contrainte %s de paramètres %s a pour expression %s" %( self.param, self.expression))
    

class Objectif(Function):
    def __init__(self, critere, name = "function", param ={},sens = "min"):
        super(Objectif, self).__init__(name, param)
        self.penalty = sens
        self.critere = critere

    def __str__(self):
        return ("La fonction objectif %s de paramètres %s a pour expression %s" %(self.name, self.param, self.expression))
        
        
class Solveur(Function):
    def __init__(self, empl,preproc,postproc, inpF,outF, name = "PamCrash"):
        self.name = name
        self.chemin = empl
        self.preprocesseur = preproc
        self.postprocesseur = postproc
        self.inputF = inpF
        self.outputF = outF
        
    def __str__(self):
        return ("Le solveur %s "%(self.name))