import unittest #@UnresolvedImport

from rules import Example, Rule

    
class TestExamples(unittest.TestCase):
    
    def setUp(self):
        self.example01 = Example([0,0,1,0,0])
        self.example02 = Example([1,1,0,0,0])
        self.example03 = Example([1,1,0,0,1])
        self.example04 = Example([1,1,1,1,1])
    
        self.rule01 = Rule(set([0,1]),-1)
        self.rule02 = Rule(set([0,4]),1)
        self.rule03 = Rule(set([1,2,3,4]),0)
    
    
    def test_ones(self):
        self.failUnless(len(self.example01.ones)==1)
        self.failUnless(2 in self.example01.ones)
    
    def test_zeros(self):
        self.failUnless(len(self.example01.zeros)==4)
        self.failUnless(set([0,1,3,4]).issubset(self.example01.zeros))

    def test_greater_than(self):
        self.failUnless(self.example02.greater_than(self.example01))
        self.failUnless(self.example03.greater_than(self.example02))
        self.failIf(self.example01.greater_than(self.example02))

    def test_intersection(self):
        self.failUnless(self.example02.intersect(self.example03).example==[1,1,0,0,0])
        self.failUnless(len(self.example02.intersect(self.example03).zeros)==3)
        self.failUnless(len(self.example02.intersect(self.example01).zeros)==5)

    def test_covers(self):
        self.failUnless(self.example02.covers(self.rule01))
        self.failIf(self.example02.covers(self.rule02))

    def test_violates(self):        
        self.failUnless(self.example02.violates(self.rule01))
        self.failIf(self.example03.violates(self.rule02))
        
        self.example04.violates(self.rule03)
        print "a"
        
        

    def test_get_clauses(self):
        clauses = self.example02.get_clauses()
        self.failUnless(len(clauses)==4)
        self.failUnless(clauses[0].consequent==2)
        self.failUnless(clauses[-1].consequent==-1)
        self.failUnless(clauses[0].antecedent == set([0,1]))
    
    def text_equals(self):
        self.failUnless(self.example01==Example([0,0,1,0,0]))

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()