class Queue:
    def __init__(self,size):
        self.size=size
        self.process=[]
        self.burst_time=[]
        self.top=-1
        self.head=0

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
        self.arr=[0]*n
        self.bt1=[]
        self.bt=bt
        self.size1=n
        self.size=n
        self.tat=0
        self.time=0
        self.turn_time=[]
        self.n=n
        for i in range(n):
            self.bt1.append(self.bt[i])
        self.bt1.sort(key=self.arrtime)
        self.i=0
        while self.i<n:
            if self.bt1[self.i][0]!=0:
                break
            self.i+=1
        print(self.bt1)
        self.bt=[]
        for i in range(self.i):
            self.bt.append(self.bt1[i][1])
        print(self.bt)
        self.size=len(self.bt)

    def arrtime(self,v):
        return v[0]
    def bursttime(self,v):
        return v[1]

    def insertQ1(self):
        Q1=Queue(self.size)
        for i in range(self.size):
            Q1.enqueue(self.p[i],self.bt[i])
        self.ScheduleQ1()

    def insertQ2(self):
        Q2=Queue(self.size)
        for i in range(self.size):
            Q2.enqueue(self.p[i],self.p[i])
        self.ScheduleQ2()

    def insertQ3(self):
        Q3=Queue(self.size)
        for i in range(self.size):
            Q3.enqueue(self.p[i],self.p[i])
        self.ScheduleQ3()

    def insertQ4(self):
        Q4=Queue(self.size)
        for i in range(self.size):
            Q4.enqueue(self.p[i],self.p[i])
        self.ScheduleQ4()

    def insertQ5(self):
        Q5=Queue(self.size)
        for i in range(self.size):
            Q5.enqueue(self.p[i],self.p[i])
        self.ScheduleQ5()

    def ScheduleQ1(self):
        arr2=[]
        for i in range(self.size):
            arr2.append(self.bt[i])
        self.bt.sort()
        #q_time=self.bt[(2*self.size//3)-1]
        q_time=10

        r=[]
        time=0
        print("in q1",self.bt,q_time)
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
                #self.arr[i]=self.time

        self.bt=self.bt[len(r):]
        while self.i<self.n:
            if self.bt1[self.i][0]<=self.time:
                self.bt.append(self.bt1[self.i][1])
                self.i+=1
            else:
                break
        self.size=len(self.bt)
        if len(self.bt)==0:
            return
        self.insertQ2()

    def ScheduleQ2(self):
        arr2=[]
        for i in range(self.size):
            arr2.append(self.bt[i])
        self.bt.sort()
        q_time=self.bt[(2*self.size//3)-1]
        r=[]
        time=0
        print("in q2",self.bt,q_time)
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
                #self.arr[i]=self.time

        self.bt=self.bt[len(r):]
        while self.i<self.n:
            if self.bt1[self.i][0]<=self.time:
                self.bt.append(self.bt1[self.i][1])
                self.i+=1
            else:
                break
        self.size=len(self.bt)
        if len(self.bt)==0:
            return
        self.insertQ3()

    def ScheduleQ3(self):
        arr2=[]
        for i in range(self.size):
            arr2.append(self.bt[i])
        self.bt.sort()
        q_time=self.bt[(2*self.size//3)-1]

        r=[]
        time=0
        print("in q3",self.bt,q_time)
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
                #self.arr[i]=self.time
            #if self.bt1[self.i][1]<=self.time:
            #    self.size+=1
            #    self.i+=1

        self.bt=self.bt[len(r):]
        while self.i<self.n:
            if self.bt1[self.i][0]<=self.time:
                self.bt.append(self.bt1[self.i][1])
                self.i+=1
            else:
                break
        self.size=len(self.bt)
        if len(self.bt)==0:
            return
        self.insertQ4()

    def ScheduleQ4(self):
        
        arr2=[]
        for i in range(self.size):
            arr2.append(self.bt[i])
        self.bt.sort()
        q_time=self.bt[(2*self.size//3)-1]

        r=[]
        print("in q4",self.bt,q_time)
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
                #self.arr[i]=self.time

        self.bt=self.bt[len(r):]
        while self.i<self.n:
            if self.bt1[self.i][0]<=self.time:
                self.bt.append(self.bt1[self.i][1])
                self.i+=1
            else:
                break
        self.size=len(self.bt)
        print(self.bt1)
        print(self.turn_time)
        if len(self.bt)==0:
            return
        self.insertQ5()

    def ScheduleQ5(self):
        arr2=[]
        for i in range(self.size):
            arr2.append(self.bt[i])
        self.bt.sort()
        q_time=self.bt[(2*self.size//3)-1]

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
        self.bt=self.bt[len(r):]
        while self.i<self.n:
            if self.bt1[self.i][0]<=self.time:
                self.bt.append(self.bt1[self.i][1])
                self.i+=1
            else:
                break
        self.size=len(self.bt)
        if len(self.bt)==0:
            return
        self.insertQ1()

    def Answer(self):
        self.insertQ1()
        s=0
        for i in range(self.n):
            s+=self.bt1[i][1]
        print((sum(self.turn_time)-s)//self.size1)
        return sum(self.turn_time)//self.size1
        


def main():
    #p=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
    #m=[20,30,100,10,80,50,10,30,25,75,90,25,60,10,110,16,54,39,90,48]
    #p=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    #m=[(0,20),(1,30),(22,100),(30,10),(14,80),(50,50),(30,10),(71,30),(138,25),(90,75),(10,90),(11,25),(12,60),(133,10),(104,110),(15,35)]
    #p=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29]
    #m=[(0,20),(1,30),(22,100),(30,10),(14,80),(50,50),(30,10),(71,30),(138,25),(90,75),(10,90),(11,25),(12,60),(133,10),(104,110),(15,35)
    #,(0,15),(20,90),(40,98),(12,65),(0,70),(0,12),(10,30),(10,60),(50,90),(45,100),(38,88),(14,20),(40,87),(23,45),(70,90),(10,36)]
    p=[0,1,2,3,4,5,6]
    m=[(0,8),(0,133),(10,21),(30,39),(40,67),(25,114),(0,54)]
    #p=[0,1,2,3,4]
    #m=[421,551,299,326,346]
    #p=[0,1,2]
    #m=[84,51,42]
    #p=[0,1,2,3,4,5,6]
    #m=[8,133,21,39,67,114,54]
    #p=[i for i in range(50)]
    #m=[125, 149, 146, 72, 107, 78, 88, 130, 60, 65, 59, 72, 38, 148, 33, 103, 102, 13, 88, 104, 64, 45, 15, 76, 33, 24, 31, 114, 28, 123, 150, 27, 110, 104, 31, 14, 104, 28, 54, 43, 90, 131, 119, 111, 63, 107, 49, 128, 24, 120]
    S=MLFQ_new(p,m,7)
    print(S.Answer())

if __name__=="__main__":
    main()