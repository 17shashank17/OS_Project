class Queue:
    def __init__(self,size,q_time):
        self.size=size
        self.process=[]
        self.burst_time=[]
        self.top=-1
        self.head=0
        self.quantum_time=q_time

    def enqueue(self,x,y):
        self.process.append(x)
        self.burst_time.append(y)
        self.top+=1


    def dequeue(self,i):
        self.process.pop(i)
        self.burst_time.pop(i)

class MLFQ_new:
    def __init__(self,p,bt,n):
        self.p=p
        self.bt=bt
        self.size=n
        self.tat=0
        self.time=0
        self.turn_time=[]

    def insertQ1(self):
        Q1=Queue(self.size,10)
        for i in range(self.size):
            Q1.enqueue(self.p[i],self.bt[i])
        self.ScheduleQ1(10)

    def insertQ2(self):
        Q2=Queue(self.size,10)
        for i in range(self.size):
            Q2.enqueue(self.p[i],self.p[i])
        self.ScheduleQ2(10)

    def insertQ3(self):
        Q3=Queue(self.size,10)
        for i in range(self.size):
            Q3.enqueue(self.p[i],self.p[i])
        self.ScheduleQ3(10)

    def insertQ4(self):
        Q4=Queue(self.size,10)
        for i in range(self.size):
            Q4.enqueue(self.p[i],self.p[i])
        self.ScheduleQ4(10)

    def insertQ5(self):
        Q5=Queue(self.size,10)
        for i in range(self.size):
            Q5.enqueue(self.p[i],self.p[i])
        self.ScheduleQ5(10)

    def ScheduleQ1(self,q_time):
        arr2=[]
        for i in range(self.size):
            arr2.append(self.bt[i])
        self.bt.sort()
        arr=[]
        for i in range(self.size):
            arr.append(self.p[i])
        #for i in range(0,self.size):
        #    self.p[i]=self.bt.index(arr[i])

        r=[]
        time=0
        for i in range(0,self.size):
            x=self.bt[i]
            self.bt[i]-=q_time
            if x>=q_time:
                self.time+=q_time
            else:
                self.time+=x
            print(self.time)

            if self.bt[i]<=0:
                r.append(i)
                time=self.time
                self.turn_time.append(time)
        #for i in range(0,len(r)):
         #   self.bt.pop(r[i])
          #  self.p.pop(r[i])
        self.bt=self.bt[len(r):]
        self.size=len(self.bt)
        if len(self.bt)==0:
            return
        self.insertQ2()

    def ScheduleQ2(self,q_time):
        arr2=[]
        for i in range(self.size):
            arr2.append(self.bt[i])
        self.bt.sort()
        arr=[]
        for i in range(self.size):
            arr.append(self.p[i])
        #for i in range(0,self.size):
        #    self.p[i]=self.bt.index(arr[i])

        r=[]
        time=0
        for i in range(0,self.size):
            x=self.bt[i]
            self.bt[i]-=q_time
            if x>=q_time:
                self.time+=q_time
            else:
                self.time+=x
            if self.bt[i]<=0:
                r.append(i)
                time=self.time
                self.turn_time.append(time)
        #for i in range(0,len(r)):
        #    self.bt.pop(r[i])
        #    self.p.pop(r[i])
        #    self.size-=1
        self.bt=self.bt[len(r):]
        self.size=len(self.bt)
        if len(self.bt)==0:
            return
        self.insertQ3()

    def ScheduleQ3(self,q_time):
        arr2=[]
        for i in range(self.size):
            arr2.append(self.bt[i])
        self.bt.sort()
        print(self.bt)
        arr=[]
        for i in range(self.size):
            arr.append(self.p[i])
        #for i in range(0,self.size):
        #    self.p[i]=self.bt.index(arr[i])

        
        r=[]
        time=0
        for i in range(0,self.size):
            x=self.bt[i]
            self.bt[i]-=q_time
            if x>=q_time:
                self.time+=q_time
            else:
                self.time+=x
            if self.bt[i]<=0:
                r.append(i)
                time=self.time
                self.turn_time.append(time)
        #for i in range(0,len(r)):
        #    self.bt.pop(r[i])
        #    self.p.pop(r[i])
        #    self.size-=1
        self.bt=self.bt[len(r):]
        self.size=len(self.bt)
        if len(self.bt)==0:
            return
        self.insertQ4()

    def ScheduleQ4(self,q_time):
        
        arr2=[]
        for i in range(self.size):
            arr2.append(self.bt[i])
        self.bt.sort()
        arr=[]
        for i in range(self.size):
            arr.append(self.p[i])
        #for i in range(0,self.size):
        #    self.p[i]=self.bt.index(arr[i])

        
        r=[]
        time=0
        for i in range(0,self.size):
            x=self.bt[i]
            self.bt[i]-=q_time
            if x>=q_time:
                self.time+=q_time
            else:
                self.time+=x
            if self.bt[i]<=0:
                r.append(i)
                time=self.time
                self.turn_time.append(time)
        #for i in range(0,len(r)):
        #    self.bt.pop(r[i])
        #    self.p.pop(r[i])
        #    self.size-=1
        self.bt=self.bt[len(r):]
        self.size=len(self.bt)
        if len(self.bt)==0:
            return
        self.insertQ5()

    def ScheduleQ5(self,q_time):
        arr2=[]
        for i in range(self.size):
            arr2.append(self.bt[i])
        self.bt.sort()
        arr=[]
        for i in range(self.size):
            arr.append(self.p[i])
        #for i in range(0,self.size):
        #    self.p[i]=self.bt.index(arr[i])

        
        r=[]
        time=0
        for i in range(0,self.size):
            x=self.bt[i]
            self.bt[i]-=q_time
            if x>=q_time:
                self.time+=q_time
            else:
                self.time+=x
            if self.bt[i]<=0:
                r.append(i)
                time=self.time
                self.turn_time.append(time)
        #for i in range(0,len(r)):
        #    self.bt.pop(r[i])
        #   self.p.pop(r[i])
        #    self.size-=1
        self.bt=self.bt[len(r):]
        self.size=len(self.bt)
        if len(self.bt)==0:
            return
        self.insertQ1()

    def Answer(self):
        self.insertQ1()
        print(self.turn_time)
        return sum(self.turn_time)


        


def main():
    n=5
    p=[0,1,2]
    m=[84,42,51]
    S=MLFQ_new(p,m,3)
    print(S.Answer())

if __name__=="__main__":
    main()
