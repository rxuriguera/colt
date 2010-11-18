
class Example(object):
    def __init__(self, e):
        self.example = e
        self.ones = set([i for i in range(0,len(e)) if (e[i]==1) ])
        self.zeros = set([i for i in range(0,len(e)) if (e[i]==0) ])
    
    def intersect(self, e):
        result = e.example[:]
        for i in self.zeros:
            result[i]=0
        return Example(result)
      
    def greater_than(self, e):
        return len(self.ones)>len(e.ones)
        
    def covers(self, rule):  
        return self.ones.issuperset(rule.antecedent)
    
    def violates(self, rule):
        return self.covers(rule) and (rule.consequent in self.zeros or rule.consequent==-1)
    
    def get_clauses(self):
        rules = [Rule(self.ones,i) for i in self.zeros]
        rules.append(Rule(self.ones, -1)) 
        return rules
    
    def __str__(self):
        return "".join([str(i) for i in self.example]) 
    
    def __hash__(self):
        return self.__str__().__hash__()

    def __cmp__(self,other):
        return self.example.__cmp__(other.example) 
    
    def __eq__(self,other):
        return self.example == other.example
    
    def set_zeros(self, zeros):
        self.__zeros = zeros
    
    def get_zeros(self):
        return self.__zeros
    
    def set_ones(self, ones):
        self.__ones = ones
    
    def get_ones(self):
        return self.__ones
    
    def set_ex(self, ex):
        self.__ex = ex
    
    def get_ex(self):
        return self.__ex
    
    example = property(get_ex, set_ex)
    ones = property(get_ones, set_ones)
    zeros = property(get_zeros, set_zeros)
    clauses = property(get_clauses)


class Rule(object):
    def __init__(self, a, c):
        self.antecedent = a
        self.consequent = c
        
    def __str__(self):
        if(self.consequent == -1):
            cs = "F"
        else:
            cs = str(self.consequent)
        astr = "".join(["".join([str(i),","]) for i in self.antecedent])[:-1]     
        return "".join([cs," <- ",astr])
    
    def __cmp__(self,other):
        s = str(self.antecedent)
        o = str(other.antecedent)
        if (s == o):
            return self.consequent.__cmp__(other.consequent)
        elif(s < o):
            return -1
        else:
            return 1;
    
    def set_antecedent(self, antecedent):
        self.__antecedent = antecedent
    
    def get_antecedent(self):
        return self.__antecedent
        
    def set_consequent(self, consequent):
        self.__consequent = consequent
    
    def get_consequent(self):
        return self.__consequent    
    
    antecedent = property(get_antecedent, set_antecedent)
    consequent = property(get_consequent, set_consequent)
    