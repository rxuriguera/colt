
from rules import Example

class AFP(object):
    
    def __init__(self):
        self.step = 0
        self.S = []
        self.h = [] 

    def violates(self, cex):
        new = [];
        v = False
        for r in self.h:
            if cex.violates(r):
                v = True
            else:
                new.append(r);
        self.h = set(new)
        return v
    
    def update_clauses(self):
        self.h = []
        for s in self.S:
            self.h.extend(s.clauses)
        self.h = set(self.h)
    
    def replace_s(self,s,intersect):
        index = self.S.index(s)
        self.S.pop(index)
        self.S.insert(index,intersect)
    
    def print_step_results(self, cex):
        self.step += 1
        print "".join(["EQ Oracle answer: ",str(cex)," (",str(self.step),")"]);
        print "S: "
        for e in self.S:
            print "  ",e;
                
        print "h: "
        
        hsorted = sorted(self.h)
        
        for clause in hsorted:
            print "  ",clause;
        print ""        
        
    def afp(self, eq, mq):
        for cex in eq:
            cex = Example(cex)
            if not self.violates(cex):  
                replaced = False
                for s in self.S:
                    intersect = s.intersect(cex) 
                    #print "".join(["Current cex ",str(cex)," Current s: ",str(s)," Called MQ: ",str(intersect)]);
                    if s.greater_than(intersect) and not mq[intersect]:
                        self.replace_s(s, intersect)
                        replaced = True
                        break
        
                if not replaced:
                    self.S.append(cex)
            
                self.update_clauses()
            self.print_step_results(cex)
        
        

if __name__ == '__main__':
    mq = {  Example([0,0,0,0,0]):True,
            Example([0,1,0,0,0]):True,
            Example([0,0,1,0,0]):True,
            Example([0,0,0,1,0]):True,
            Example([1,0,0,0,0]):True,
            Example([0,0,0,0,1]):False,
            Example([0,1,0,1,0]):False,
            Example([0,1,1,0,0]):False}
    
    # Equivalence queries Oracle
    eq = [  [0,1,0,1,1],
            [1,1,1,0,0],
            [0,0,0,0,1],
            [0,0,0,1,1],
            [0,1,0,1,1],
            [0,0,0,1,1],
            [0,0,1,1,0],
            [0,0,0,1,1],
            [0,1,1,1,0],
            [1,0,0,1,0],
            [0,0,0,1,1],
            [0,1,1,1,0],
            [0,1,0,1,0],
            [0,0,0,1,1],
            [0,1,1,1,0],
            [0,1,1,1,1],
            [0,0,0,1,1],
            [0,1,1,1,0],
            [0,1,1,1,1],
            [0,0,0,1,1],
            [0,1,1,1,0],
            [1,1,1,1,1]]
    
    AFP().afp(eq, mq)
    
    