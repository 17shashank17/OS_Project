
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
        self.bt=bt
        self.size=n
        self.tat=0
        self.size1=n
        self.time=0
        self.turn_time=[]

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

    '''def insertQ4(self):
        Q4=Queue(self.size)
        for i in range(self.size):
            Q4.enqueue(self.p[i],self.p[i])
        self.ScheduleQ4()

    def insertQ5(self):
        Q5=Queue(self.size)
        for i in range(self.size):
            Q5.enqueue(self.p[i],self.p[i])
        self.ScheduleQ5()'''

    def ScheduleQ1(self):
        arr2=[]
        for i in range(self.size):
            arr2.append(self.bt[i])
        self.bt.sort()
        q_time=self.bt[(2*self.size//3)-1]
        arr=[]
        for i in range(self.size):
            arr.append(self.p[i])

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

        arr=[]
        for i in range(self.size):
            arr.append(self.p[i])

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
        self.size=len(self.bt)
        if len(self.bt)==0:
            return
        print(self.turn_time)
        self.insertQ3()

    def ScheduleQ3(self):
        arr2=[]
        for i in range(self.size):
            arr2.append(self.bt[i])
        self.bt.sort()

        q_time=self.bt[(2*self.size//3)-1]
        tat=sum(self.turn_time)
        tat+=self.roundRobin(q_time)
        print(tat//self.size1)

    def findWaitingTime(self , wt , quantum):  
        rem_bt = [0] * self.size 
    
        for i in range(self.size):  
            rem_bt[i] = self.bt[i] 
        
        t = self.time  
        while(1): 
            done = True
            for i in range(self.size): 
                if (rem_bt[i] > 0): 
                    done = False
                    
                    if (rem_bt[i] > quantum): 

                        t += quantum  
    
                        rem_bt[i] -= quantum  
    
                    else: 
                        t = t + rem_bt[i]  

                        wt[i] = t - self.bt[i]
     
                        rem_bt[i] = 0
                    
            if (done == True): 
                break

                
    def findTurnAroundTime(self,wt, tat): 
        for i in range(self.size): 
            tat[i] = self.bt[i] + wt[i]  
    
    def roundRobin(self,quantum):  
        wt = [0] * self.size 
        tat = [0] * self.size
        self.findWaitingTime(wt, quantum)  
    
        self.findTurnAroundTime(wt, tat)  
    
        total_wt = 0
        total_tat = 0
        for i in range(self.size): 
    
            total_wt = total_wt + wt[i]  
            total_tat = total_tat + tat[i]
        return total_tat  

      
        

    '''def ScheduleQ4(self):
        
        arr2=[]
        for i in range(self.size):
            arr2.append(self.bt[i])
        self.bt.sort()
        q_time=self.bt[2*self.size//3]

        arr=[]
        for i in range(self.size):
            arr.append(self.p[i])
        
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
        self.size=len(self.bt)
        if len(self.bt)==0:
            return
        self.insertQ5()

    def ScheduleQ5(self):
        arr2=[]
        for i in range(self.size):
            arr2.append(self.bt[i])
        self.bt.sort()
        q_time=self.bt[2*self.size//3]

        arr=[]
        for i in range(self.size):
            arr.append(self.p[i])
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
        self.size=len(self.bt)
        if len(self.bt)==0:
            return
        self.insertQ1()'''

    def Answer(self):
        self.insertQ1()




        


def main():
    n=5
    #p=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]
    #m=[20,30,100,10,80,50,10,30,25,75,90,25,60,10,110]
    p=[0,1,2,3,4,5,6]
    m=[8,133,21,39,67,114,54]
    #p=[0,1,2,3,4]
    #m=[421,551,299,326,346]
    S=MLFQ_new(p,m,7)
    S.Answer()

if __name__=="__main__":
    main()
