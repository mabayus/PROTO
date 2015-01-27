'''
Created on 16 juil. 2014

@author: georges
'''
#-*- coding: utf-8 -*-


class Intervalle(object):
    """
    """
    
    def __init__(self, borneMin = -1.1, borneSup = -1):
        self.lowerBound = borneMin
        self.upperBound = borneSup
        print ("Objet créé") #debogage
    
    
    def __str__(self):
        return "Intervalle : inf %f sup %f " %(self.lowerBound, self.upperBound)


class Variable (object):
    """
        That class represent the variable's main class. It has no particular method.
        
    """
    
    def __init__(self, name = "var"):
        self.name = name

    def __str__(self):
        return "Variable : %s" % (self.name)
    
    
    
    def __add__(self):
        raise NotImplementedError("Méthode non implémentée pour cette classe. \n N'est disponible que pour les variables discrète et continues")
    
    def __sub__(self):
        raise NotImplementedError("Méthode non implémentée pour cette classe. \n N'est disponible que pour les variables discrète et continues")
    
    def __mul__(self):
        raise NotImplementedError("Méthode non implémentée pour cette classe. \n N'est disponible que pour les variables discrète et continues")
    
    def __truediv__(self):
        raise NotImplementedError("Méthode non implémentée pour cette classe. \n N'est disponible que pour les variables discrète et continues")
    
    def __repr__(self):
        return "Variable()"
    


class VariableNumerique (Variable):
    """
        Cette classe représente les variables numériques. C'est la classe mère des variables discrètes et continues
        Pour créer une variable discrete, il faut fournir 
            son nom (name)
            la liste des valeurs qu'eele prend qui par défaut est vide
            sa valeur courante qui est nulle par défaut
    """
    
    def __init__(self, name, val = 0):
        """
            Cette méthode sert à créer les objets de type VariableDiscrete.
            Elle prend en paralètre 
                la liste des valeurs autorisées (valAutorise)
                la valeur courante de la variable (curValue)
            Si ces deux paramètres ne sont pas fournis, des valeurs par défaut sont affectées à ces champs.
            Une liste vide pour valAutorise et 0 pour curValue
        """
        super (VariableNumerique, self).__init__(name)
        self.value = val
        
    
    
    def __str__(self):
        """
            Convertit la classe en chaine de caractère.Équivalent de toString() d'autres langages.
        """
        return "Variable Numérique de nom: %s.\nValeur courante %f" %(self.name, self.value)    
    
    
    def __add__(self, val_to_add):
        """
            Cette fonction sert à additionner une variable discrète à un entier, un réel.
            Une exception est levée sinon.
        """
        
        if ( (isinstance(val_to_add, int)) or (isinstance(val_to_add, float)) ): 
            """
                si la valeur à ajouter est un entier ou un réel
            """
            return (self.value + val_to_add)
        elif ( (isinstance (val_to_add, VariableNumerique)) or (isinstance(val_to_add, VariableDiscrete)) or (isinstance(val_to_add, ContinuousVariable)) ):
            """
                s'il s'agit plutôt d'une variable numérique ou d'une variable discrete ou encore d'une variable continue
            """
            return (self.value + val_to_add.value) #pourquoi ne pas le faire pour des variables continue
        else:
            raise TypeError("La valeur à ajouter n'est pas d'un type compatible. \nSeul les entiers, les réels ou les variables discrètes sont autorisées")

    
    def __sub__(self, val_to_sub):
        """
            Cette fonction sert à soustraire une variable discrète d'un entier, d'un réel ou d'une variable continue.
            Une exception est levé si le type n'est pas compatible
        """
        
        if ( (isinstance(val_to_sub, int)) or (isinstance(val_to_sub, float)) ): 
            """
                si la valeur à ajouter est un entier ou un réel
            """
            return (self.value -val_to_sub)
        elif ( (isinstance (val_to_sub, VariableNumerique)) or (isinstance(val_to_sub, VariableDiscrete)) or (isinstance(val_to_sub, ContinuousVariable)) ):
            """
                s'il s'agit plutôt d'une variable discrete
            """
            return self.value - val_to_sub.value #pourquoi ne pas le faire pour des variables continue
        else:
            raise TypeError("La valeur à retrancher n'est pas d'un type compatible\nSeul des entiers, des réels ou des variables discrètes sont autorisées")

    
    def __mul__(self, val_to_mul):
        """
            Cette fonction sert à multiplier une variable discrète et un entier ou un réel ou une variable discrète.
            Une exception est levée lorsque le type est incorrect.
        """
        
        if ( (isinstance(val_to_mul, int)) or (isinstance(val_to_mul, float)) ): 
            """
                si la valeur à ajouter est un entier ou un réel
            """
            return (self.value * val_to_mul)
        elif ( (isinstance (val_to_mul, VariableNumerique)) or (isinstance(val_to_mul, VariableDiscrete)) or (isinstance(val_to_mul, ContinuousVariable)) ):
            """
                s'il s'agit plutôt d'une variable discrete
            """
            return (self.value * val_to_mul.value) #pourquoi ne pas le faire pour des variables continue
        else:
            raise TypeError("La valeur à ajouter n'est pas d'un type compatible\nSeul des entiers, des réels ou des variables discrètes sont autorisées")

    
    def __truediv__(self, val_to_div):
        """
            Cette fonction sert à additionner une variable discrète à un entier, un réel.
            Une exception est levée sinon.
        """
        
        if ( (isinstance(val_to_div, int)) or (isinstance(val_to_div, float)) ): 
            """
                si la valeur à ajouter est un entier ou un réel
            """
            if ( val_to_div == 0 ):
                raise ArithmeticError ("Division par ZÉRO impossible")
            else:
                return (self.value / float (val_to_div))
        elif ( (isinstance (val_to_div, VariableNumerique)) or (isinstance(val_to_div, VariableDiscrete)) or (isinstance(val_to_div, ContinuousVariable)) ):
            """
                s'il s'agit plutôt d'une variable discrete
            """
            if ( val_to_div.value == 0 ):
                raise ArithmeticError ("Division par ZÉRO impossible")
            else:
                return (self.value / float(val_to_div.value) ) #pourquoi ne pas le faire pour des variables continue
        else:
            raise TypeError("La valeur à ajouter n'est pas d'un type compatible\nSeul des entiers, des réels ou des variables discrètes sont autorisées")
        
    
    
    def __lt__(self, terme):
        """
            Use it if you want to compare 
                -two continuous variable
                -a continous variable to an integer or a float
            Let supposed that a is a Continuous variable and b an integer or a float or a continuous variable
            a < b <===> a.__lt__(b) returns true if the current value of a (a.value) is less than b (or b.value when b is a continuaous variable)
        """
    #mutation of less than (<) 
        if ( (isinstance(terme,VariableNumerique)) ) :
        #I check if my parameter is a continuous variable
            if ( self.value < terme.value ) :
                return True
            else:
                return False
        elif ( (isinstance(terme, int)) or (isinstance(terme, float)) ):
        #the parameter is an integer or a float
            if ( self.value < terme) :
                return True
            else:
                return False
        else:
            raise TypeError ("The supplied parameter is an incompatible type")


    def __le__( self, terme ):
        """
            Use it if you want to compare 
                -two continuous variable
                -a continous variable to an integer or a float
            Let supposed that a is a Continuous variable and b an integer or a float or a continuous variable
            a <= b <===> a.__le__(b) returns true if the current value of a (a.value) is less or equal to b (or b.value when b is a continuaous variable)
        """
        if ( (isinstance(terme, VariableNumerique)) ) :
        #I check if my parameter is a continuous variable
            if ( self.value <= terme.value ) :
                return True
            else:
                return False
        elif ( (isinstance(terme, int)) or (isinstance(terme, float)) ):
        #the parameter is an integer or a float
            if ( self.value <= terme) :
                return True
            else:
                return False
        else:
            raise TypeError ("The supplied parameter has an incompatible type")

            
    def __gt__( self, terme):
        """
            Use it if you want to compare 
                -two continuous variable
                -a continous variable to an integer or a float
            Let supposed that a is a Continuous variable and b an integer or a float or a continuous variable
            a > b <===> a.__gt__(b) returns true if the current value of a (a.value) is greater than b (or b.value when b is a continuaous variable)
        """
        if ( (isinstance(terme, VariableNumerique)) ) :
        #I check if my parameter is a continuous variable
            if ( self.value > terme.value ) :
                return True
            else:
                return False
        elif ( (isinstance(terme, int)) or (isinstance(terme, float)) ):
        #the parameter is an integer or a float
            if ( self.value > terme) :
                return True
            else:
                return False
        else:
            raise TypeError ("The supplied parameter has an incompatible type")


    def __ge__( self, terme ):
        """
            Use it if you want to compare 
                -two continuous variable
                -a continous variable to an integer or a float
            Let supposed that a is a Continuous variable and b an integer or a float or a continuous variable
            a >= b <===> a.__ge__(b) returns true if the current value of a (a.value) is greater or equal to b (or b.value when b is a continuaous variable)
        """
    #mutation of >=
        if ( (isinstance(terme, VariableNumerique)) ) :
        #I check if my parameter is a continuous variable
            if ( self.value >= terme.value ) :
                return True
            else:
                return False
        elif ( (isinstance(terme, int)) or (isinstance(terme, float)) ):
        #the parameter is an integer or a float
            if ( self.value >= terme) :
                return True
            else:
                return False
        else:
            raise TypeError ("The supplied parameter is an incompatible type")


    def __eq__( self, terme ):
        """
            Use it if you want to compare 
                -two continuous variable
                -a continous variable to an integer or a float
            Let supposed that a is a Continuous variable and b an integer or a float or a continuous variable
            a == b <===> a.__lt__(b) returns true if the current value of a (a.value) is equal to b (or b.value when b is a continuaous variable)
        """
    #mutation of ==
        if ( (isinstance(terme, VariableNumerique)) ) :
        #I check if my parameter is a continuous variable
            if ( self.value == terme.value ) :
                return True
            else:
                return False
        elif ( (isinstance(terme, int)) or (isinstance(terme, float)) ):
        #the parameter is an integer or a float
            if ( self.value == terme) :
                return True
            else:
                return False
        else:
            raise TypeError ("The supplied parameter is an incompatible type")
    

    def __round__(self, n=0):
        '''
            Cette fonction "arrondi" la valeur courante.
            L'arrondi consiste à retourner la valeur autorisée la plus proche de la valeur courante.
        '''
        pass
    
    
    def __float__(self):
        """
            Cette fonction convertie une variable discrete en réel
        """
        return float(self.value)
    
    def __int__(self):
        """
            Concertie une variable discrète en entier
        """
        return int(self.value)
        
    def __repr__(self):
        return "VariableDiscrete()"


class VariableDiscrete(VariableNumerique):
    """
        Cette classe représente les variables discrètes.
        Pour créer une variable discrete, il faut fournir 
            son nom (name)
            la liste des valeurs qu'eele prend qui par défaut est vide
            sa valeur courante qui est nulle par défaut
    """
    def __init__(self, name, valAutorise = [], val = 0):
        """
            Cette méthode sert à créer les objets de type VariableDiscrete.
            Elle prend en paralètre 
                la liste des valeurs autorisées (valAutorise)
                la valeur courante de la variable (curValue)
            Si ces deux paramètres ne sont pas fournis, des valeurs par défaut sont affectées à ces champs.
            Une liste vide pour valAutorise et 0 pour curValue
        """
        super(VariableDiscrete, self).__init__(name)
        self.valAutorise = valAutorise
        self.value = val
        
    
    def __str__(self):
        """
            Convertit la classe en chaine de caractère.Équivalent de toString() d'autres langages.
        """
        return "Variable Discrete de nom: %s.\nValeurs autorisées : %s \nValeur courante %f" %(self.name, self.valAutorise, self.value)
    
    def __add__(self, val_to_add):
        return (super (VariableDiscrete, self).__add__(val_to_add))
    
    
    def __sub__(self, val_to_sub):
        return (super (VariableDiscrete, self).__sub__(val_to_sub))
    
    
    def __mul__(self, val_to_mul):
        return (super (VariableDiscrete, self).__mul__(val_to_mul))
    
    
    def __truediv__(self, val_to_div):
        return (super (VariableDiscrete, self).__div__(val_to_div))
    
    
    def __gt__(self, terme):
        return (super (VariableDiscrete, self).__gt__(terme))
    
    
    def __ge__(self, terme):
        return (super (VariableDiscrete, self).__ge__(terme))
    
    
    def __lt__(self, terme):
        return (super (VariableDiscrete, self).__lt__(terme))
    
    
    def __le__(self, terme):
        return (super (VariableDiscrete, self).__le__(terme))
    
    
    def __eq__(self, terme):
        return (super (VariableDiscrete, self).__eq__(terme))
    
    
    def __repr__(self):
        return "VariableDiscrete()"



class ContinuousVariable(Variable):
    """ The class Continuous variable is a super class for continued variables.
        Its attributes are:
          -lowerBound
          -upperBound
          -value is the current value of the variable
        Comparaison functions are overrided.
        Let supposed that a and b are ContinuousVariable object
        when a<b <==> a.__le__(b). Idem for other comparaison method
        a+b <===> a.__add__(b)
        
    """
    """We are defining a continued type for the classic type float"""

    def __init__(self, name = "var",valMin= -1.1, valMax= -1, val = 0):
        """
        The constructor takes three parameters
         -the first valMin is the lower bound
         -the second one is the upper bound
         -the last one is the current value of the variable. It value must be between earlier bounds
        """
        super(ContinuousVariable, self).__init__(name)
        if  (valMax <= valMin) :
            raise ValueError("The lower bound is greater than the upper bound")
        self.lowerBound = valMin
        self.upperBound = valMax
        self.value = val #we store the current value here

    
    def appartenir(self , val):
        """
            That method takes a parameter named val and checks if that given value belongs to the continued variable bounds
        """
        if ( (val >= self.lowerBound) and (val <= self.upperBound) ):
            return True
        else:
            return False


    def __add__(self, val_to_add):
        """
            Cette fonction sert à additionner une variable discrète à un entier, un réel.
            Une exception est levée sinon.
        """
        
        if ( (isinstance(val_to_add, int)) or (isinstance(val_to_add, float)) ): 
            """
                si la valeur à ajouter est un entier ou un réel
            """
            return self.value + val_to_add
        elif ( isinstance (val_to_add, VariableDiscrete)):
            """
                s'il s'agit plutôt d'une variable discrete
            """
            return (self.value + val_to_add.value) #pourquoi ne pas le faire pour des variables continue
        else:
            raise TypeError("La valeur à ajouter n'est pas d'un type compatible\nSeul des entiers, des réels ou des variables discrètes sont autorisées")

    
    def __sub__(self, val_to_sub):
        """
            Cette fonction sert à soustraire une variable discrète d'un entier, d'un réel ou d'une variable continue.
            Une exception est levé si le type n'est pas compatible
        """
        
        if ( (isinstance(val_to_sub, int)) or (isinstance(val_to_sub, float)) ): 
            """
                si la valeur à ajouter est un entier ou un réel
            """
            return (self.value -val_to_sub)
        elif ( isinstance (val_to_sub, VariableDiscrete)):
            """
                s'il s'agit plutôt d'une variable discrete
            """
            return self.value - val_to_sub.value #pourquoi ne pas le faire pour des variables continue
        else:
            raise TypeError("La valeur à retrancher n'est pas d'un type compatible\nSeul des entiers, des réels ou des variables discrètes sont autorisées")

    
    def __mul__(self, val_to_mul):
        """
            Cette fonction sert à multiplier une variable discrète et un entier ou un réel ou une variable discrète.
            Une exception est levée lorsque le type est incorrect.
        """
        
        if ( (isinstance(val_to_mul, int)) or (isinstance(val_to_mul, float)) ): 
            """
                si la valeur à ajouter est un entier ou un réel
            """
            return (self.value * val_to_mul)
        elif ( isinstance (val_to_mul, VariableDiscrete)):
            """
                s'il s'agit plutôt d'une variable discrete
            """
            return (self.value * val_to_mul.value) #pourquoi ne pas le faire pour des variables continue
        else:
            raise TypeError("La valeur à ajouter n'est pas d'un type compatible\nSeul des entiers, des réels ou des variables discrètes sont autorisées")

    
    def __truediv__(self, val_to_div):
        """
            Cette fonction sert à additionner une variable discrète à un entier, un réel.
            Une exception est levée sinon.
        """
        
        if ( (isinstance(val_to_div, int)) or (isinstance(val_to_div, float)) ): 
            """
                si la valeur à ajouter est un entier ou un réel
            """
            return self.value / float (val_to_div)
        elif ( isinstance (val_to_div, VariableDiscrete)):
            """
                s'il s'agit plutôt d'une variable discrete
            """
            return self.value / float(val_to_div) #pourquoi ne pas le faire pour des variables continue
        else:
            raise TypeError("La valeur à ajouter n'est pas d'un type compatible\nSeul des entiers, des réels ou des variables discrètes sont autorisées")




    def __lt__(self, terme):
        """
            Use it if you want to compare 
                -two continuous variable
                -a continous variable to an integer or a float
            Let supposed that a is a Continuous variable and b an integer or a float or a continuous variable
            a < b <===> a.__lt__(b) returns true if the current value of a (a.value) is less than b (or b.value when b is a continuaous variable)
        """
    #mutation of less than (<) 
        if ( (isinstance(terme, ContinuousVariable)) ) :
        #I check if my parameter is a continuous variable
            if ( self.value < terme.value ) :
                return True
            else:
                return False
        elif ( (isinstance(terme, int)) or (isinstance(terme, float)) ):
        #the parameter is an integer or a float
            if ( self.value < terme) :
                return True
            else:
                return False
        else:
            raise TypeError ("The supplied parameter is an incompatible type")


    def __le__( self, terme ):
        """
            Use it if you want to compare 
                -two continuous variable
                -a continous variable to an integer or a float
            Let supposed that a is a Continuous variable and b an integer or a float or a continuous variable
            a <= b <===> a.__le__(b) returns true if the current value of a (a.value) is less or equal to b (or b.value when b is a continuaous variable)
        """
        if ( (isinstance(terme, ContinuousVariable)) ) :
        #I check if my parameter is a continuous variable
            if ( self.value <= terme.value ) :
                return True
            else:
                return False
        elif ( (isinstance(terme, int)) or (isinstance(terme, float)) ):
        #the parameter is an integer or a float
            if ( self.value <= terme) :
                return True
            else:
                return False
        else:
            raise TypeError ("The supplied parameter is an incompatible type")

            
    def __gt__( self, terme):
        """
            Use it if you want to compare 
                -two continuous variable
                -a continous variable to an integer or a float
            Let supposed that a is a Continuous variable and b an integer or a float or a continuous variable
            a > b <===> a.__gt__(b) returns true if the current value of a (a.value) is greater than b (or b.value when b is a continuaous variable)
        """
        if ( (isinstance(terme, ContinuousVariable)) ) :
        #I check if my parameter is a continuous variable
            if ( self.value > terme.value ) :
                return True
            else:
                return False
        elif ( (isinstance(terme, int)) or (isinstance(terme, float)) ):
        #the parameter is an integer or a float
            if ( self.value > terme) :
                return True
            else:
                return False
        else:
            raise TypeError ("The supplied parameter is an incompatible type")


    def __ge__( self, terme ):
        """
            Use it if you want to compare 
                -two continuous variable
                -a continous variable to an integer or a float
            Let supposed that a is a Continuous variable and b an integer or a float or a continuous variable
            a >= b <===> a.__ge__(b) returns true if the current value of a (a.value) is greater or equal to b (or b.value when b is a continuaous variable)
        """
    #mutation of >=
        if ( (isinstance(terme, ContinuousVariable)) ) :
        #I check if my parameter is a continuous variable
            if ( self.value >= terme.value ) :
                return True
            else:
                return False
        elif ( (isinstance(terme, int)) or (isinstance(terme, float)) ):
        #the parameter is an integer or a float
            if ( self.value >= terme) :
                return True
            else:
                return False
        else:
            raise TypeError ("The supplied parameter is an incompatible type")


    def __eq__( self, terme ):
        """
            Use it if you want to compare 
                -two continuous variable
                -a continous variable to an integer or a float
            Let supposed that a is a Continuous variable and b an integer or a float or a continuous variable
            a == b <===> a.__lt__(b) returns true if the current value of a (a.value) is equal to b (or b.value when b is a continuaous variable)
        """
    #mutation of ==
        if ( (isinstance(terme, ContinuousVariable)) ) :
        #I check if my parameter is a continuous variable
            if ( self.value == terme.value ) :
                return True
            else:
                return False
        elif ( (isinstance(terme, int)) or (isinstance(terme, float)) ):
        #the parameter is an integer or a float
            if ( self.value == terme) :
                return True
            else:
                return False
        else:
            raise TypeError ("The supplied parameter is an incompatible type")


    def __repr__(self):
        return "ContinuousVariable()"


    def __str__(self):
        """
            That function convert the object into string.
        """
        return "Lower bound: %s, Upper bound: %s, Current value: %s" % (self.lowerBound, self.upperBound, self.value)



#    def __radd__(self, val):
#        return val.__add__(self)


#    def __sub__(self, val):
        """
        We override substraction. The function must be called by a continious variable. The second term (the parameter)
        can be an integer, a float or a continuous variable
        """

#        if( (isinstance(val, int)) or (isinstance(val, float))):
        # if the parameter val is an integer or a float or an ContinuFloat or continueInt
#            return (self.value - val)
        
#        elif (isinstance(val, ContinuousVariable)):
        #action when val is a continued variable
#            return (self.value - val.value)
#        else:
        # the parameter is neither an integer neither a float nor a continuous variable.
        #We raise a type error.
#            raise TypeError ("The supplied parameter is an incompatible type")


#    def __rsub__(self, val):
#        __sub__(val, self)


    '''def __truediv__(self, val):
        """
        We override division. The function must be called by a continious variable. The second term (the parameter)
        can be an integer, a float or a continuous variable
        """
        if( (isinstance(val, int)) or (isinstance(val, float))):# if the parameter val is an integer or a float or an ContinuFloat or continueInt
            return (self.value / float(val))
        
        elif (isinstance(val, ContinuousVariable)):
            return (self.value / float(val.value)) #here val is a continued variable
        else:
        # the parameter is neither an integer neither a float nor a continuous variable.
        #We raise a type error.
            raise TypeError ("The supplied parameter is an incompatible type")


    def __mul__(self, val):
        """
        We override multiplication.
        That new function takes as argument a float, an integer or another continuous variable

        """
        if( (isinstance(val, int)) or (isinstance(val, float))):
        # the parameter val is an integer or a float
            return (self.value * val)
        
        elif (isinstance(val, ContinuousVariable)):
        # both self and the parameter (val) are 
            return (self.value * float(val.value)) #here val is a continued variable
        else:
        # the parameter is neither an integer neither a float nor a continuous variable.
        #We raise a type error.
            raise TypeError ("The supplied parameter is an incompatible type")'''

#    def __rmul__(self, val):
#        __mul__(val, self)


class ContinuousFloat(ContinuousVariable):
#The class CountinuousFloat is a specification of CountinuousVariable
    """Float that takes their value in an gap"""
    def __init__(self, valMin, valMax, val):
        super(ContinuousFloat, self).__init__(valMin, valMax, val)


    