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
        self.insertQ1()
        pass

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
        for i in range(0,self.size):
            self.p[i]=self.bt.index(arr[i])

        r=[]
        for i in range(self.size):
            self.bt[i]-=q_time
            if self.bt[i]<=0:
                r.append(i)
        for i in range(0,len(r)):
            self.bt.pop(r[i])
            self.p.pop(r[i])
            self.size-=1
        self.insertQ2()

    def ScheduleQ2(self,q_time):
        arr2=[]
        for i in range(self.size):
            arr2.append(self.bt[i])
        self.bt.sort()
        arr=[]
        for i in range(self.size):
            arr.append(self.p[i])
        for i in range(0,self.size):
            self.p[i]=self.bt.index(arr[i])

        r=[]
        for i in range(self.size):
            self.bt[i]-=q_time
            if self.bt[i]<=0:
                r.append(i)
        for i in range(0,len(r)):
            self.bt.pop(r[i])
            self.p.pop(r[i])
            self.size-=1
        if len(self.p)==0:
            return
        self.insertQ3()

    def ScheduleQ3(self,q_time):
        arr2=[]
        for i in range(self.size):
            arr2.append(self.bt[i])
        self.bt.sort()
        arr=[]
        for i in range(self.size):
            arr.append(self.p[i])
        for i in range(0,self.size):
            self.p[i]=self.bt.index(arr[i])

        
        r=[]
        for i in range(self.size):
            self.bt[i]-=q_time
            if self.bt[i]<=0:
                r.append(i)
        for i in range(0,len(r)):
            self.bt.pop(r[i])
            self.p.pop(r[i])
            self.size-=1
        if len(self.p)==0:
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
        for i in range(0,self.size):
            self.p[i]=self.bt.index(arr[i])

        
        r=[]
        for i in range(self.size):
            self.bt[i]-=q_time
            if self.bt[i]<=0:
                r.append(i)
        for i in range(0,len(r)):
            self.bt.pop(r[i])
            self.p.pop(r[i])
            self.size-=1
        if len(self.p)==0:
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
        for i in range(0,self.size):
            self.p[i]=self.bt.index(arr[i])

        
        r=[]
        for i in range(self.size):
            self.bt[i]-=q_time
            if self.bt[i]<=0:
                r.append(i)
        for i in range(0,len(r)):
            self.bt.pop(r[i])
            self.p.pop(r[i])
            self.size-=1
        if len(self.p)==0:
            return
        self.insertQ1()


        









def main():
    n=5
    p=[0,1,2,3,4]
    m=[40,30,5,8,12]
    S=MLFQ_new(p,m)
    Solve(n,p,m)

if __name__=="__main__":
    main()
