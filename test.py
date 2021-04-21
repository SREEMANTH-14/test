class Queue:
    def __init__(self):
        self.q1=[]
        self.q2=[]
    def enQueue(self, x):
        while len(self.q1)!=0:
            self.q2.append(self.q1[-1])
            self.q1.pop()
        self.q1.append(x)
        while len(self.q2)!=0:
            self.q1.append(self.q2[-1])
            self.q2.pop()
    def deQueue(self):
        if len(self.q1)==0:
            print( "Queue is Empty")
        x=self.q1[-1]
        self.q1.pop()
        return x
