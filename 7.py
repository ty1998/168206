#�Ŷ����������һ�������տ��꣬����ҵ�����԰�̨��ѡ������߲ˣ���ͽ�������Ϊ��Ĳ�ʳ���������ò��Ϻ󣬾��õ��տ���������
#
#��������ǹ���ƽ��ÿλ�˿͵Ĳ�ʳ׼��ʱ�䡣
#�ٶ�ÿλ�˿Ͷ���ȥ��ѡ�����5�ݲ��ϣ���ÿ����̨ȡһ�ݲ��ϵ�ʱ��Ϊ10s������20����̨,ÿ����̨ͬʱֻ����1����ʹ�ã�
#�տ��ܿ�һ��ʳ��Ҫ3���ӣ�����ͬʱ��8��ʳ�����̨���տ�������ʱ�򣬹˿�ֻ���Ŷӵȴ���
#
#�������³�����ƽ��ʱ�䣺
#
#ֻ��1���˿�ʱ
#ͬʱ��8���˿�
#ͬʱ��25���˿�
#��25���˿ͣ����������1����
#ͬʱ100���˿�
#ͬʱ100���˿ͣ����������2����
#
#�ӷ��
#
#����˿����տ��ܵ�ƽ���ȴ�ʱ��
#����˿��ڰ�̨��ƽ���ȴ�ʱ��

#һ����һ������
#��̨��ÿ������ִ��5����������������ͬʱ���У������ڲ�ͬʱ�������ڲ�ͬ��cpu
#
#���ܣ�ÿ������ִ��1��������

#�� ��̨��ƽ���ȴ�ʱ��
global ave_waiting_time_at_bar 
ave_waiting_time_at_bar = 0
#�ڿ��ܵȴ���ƽ���ȴ�ʱ��
global ave_waiting_time_at_grill 
ave_waiting_time_at_grill = 0



class Consumer(object):
    def __init__(self,id):
        self.id = id
        self.tasks = []
#        time�ǵȴ�ʱ��+ȡʳ���ʱ�䣬����ڼ����ڰ�̨�ĵȴ�ʱ��Ҫ��
        self.time = 0
#        �ڿ��ܵȴ���ʱ��
        self.time_at_grill = 0
        self.roasting_time = 0
    def complete_task(self,task):
        self.tasks.append(task)
        
def Restaurant(people):
    index = 0
#    ����Ĺ˿����̨�Ķ���
    for i in range(0,len(people)):
        
        queues[index].append(people[i])
        index += 1
        if index >=20 :
            index = 0

def Bar_to_choose():
#sum_of_one_time
    sum = 0
    for i in range(0,20):
            sum += len(queues[i])
#    ��ȫ���������ˣ��򷵻�
    if sum <= 0:
        return 0 
    a_queue = []
    for i in range(0,20):
        
#        �����ǰ����û����������ǰ����
        if len(queues[i]) <= 0:
            a_queue.append(-1)
            continue
        
#        �ö��е��˵ĵȴ�ʱ�� ������10��
        for j in range(len(queues[i])):
            queues[i][j].time += 10
            
#        ������ʸö���
##       ���ʶ��У����ҽ������е�ͷ�ڵ��ó���(��վ�ڶ�����ǰ�����)
        a_consumer = queues[i].pop(0)
#        �õ�һ��ʳ��
        a_consumer.tasks.append(i)
#        print("guest id:"+str(a_consumer.id)+"ʳ���嵥:"+str(a_consumer.tasks)+"time"+str(a_consumer.time))
        if len(a_consumer.tasks) >= 5:
#            ����������ﵽ5 ��ӵ� ׼����ʳ��Ķ��� ������������ѭ����
            ready_to_roast.append(a_consumer)
            a_queue.append(-1)
            continue
        a_queue.append(a_consumer)
#        ѡ��ʳ����˳��������Ŷӣ��������ڵĶ���
    for index in range(0,20):
        if a_queue[index] == -1:
            continue
        else:
#            ������Ӹ��˵���һ�����еȴ�
            queues[(index+1)%20].append(a_queue[index])
#    for index in range(0,len(ready_to_roast)):
#        print(index," roasting guest id",str(ready_to_roast[index].id),"ʳ���嵥Ϊ",str(ready_to_roast[index].tasks))   
        
    return sum 


def Grill_to_eat():
    global ave_waiting_time_at_bar
    global ave_waiting_time_at_grill 
     
    amount = 0
    if len(ready_to_roast) <= 0:
        return
    elif len(ready_to_roast) <= 8:
        
        for i in range(0,len(ready_to_roast)):
        
            ready_to_roast[i].roasting_time += 10
            if ready_to_roast[i].roasting_time >= 180:
#                ��Ϊ ready_to_roast���У��Ƚ��ȳ��������ǰ��� �϶� ����ʱ�����ڻ���� ����Ŀ���ʱ��
                amount += 1
                continue
    else:
        for i in range(0,8):

#            ��ǰ�˿͵��տ���ʱ�� +10��
            
            ready_to_roast[i].roasting_time += 10
#            ʱ�䵽��3�����Զ�����
            if ready_to_roast[i].roasting_time >= 180:
                amount += 1
                continue
#            �ڿ����ŶӵĹ˿��ڵȴ�

        for i in range(8,len(ready_to_roast)):
            ready_to_roast[i].time_at_grill += 10
#            ����ĳ�����
#    ��û�˿���ʳ��򷵻ؼ����ȴ�
    if amount <= 0:
        return
    for i in range(0,amount):
#        print(i)
#        �����˿��꽫���Ƴ� ���У�һ���� �Ƴ� ��һλ��ÿ���Ƴ�һλ������Ļ���ǰ   ��
        c_person = ready_to_roast.pop(0)
        print("guest who completes, id",str(c_person.id),"ʳ���嵥Ϊ"+str(c_person.tasks)+"�ȴ�ʱ��Ϊ",str(c_person.time),"���տ��ܵȴ���ʱ��Ϊ",str(c_person.time_at_grill),"�տ�ʱ��Ϊ",str(c_person.roasting_time))
        ave_waiting_time_at_bar = ave_waiting_time_at_bar + c_person.time - 50
        ave_waiting_time_at_grill += c_person.time_at_grill
        
if __name__ == '__main__':
    
#    �����ܺ�
    total_number = int(input("��������������"))
#    ʱ����
    interval = int(input("������ʱ������"))
    
    Time = 0 
    Time_goes_by = lambda x:x+10
    
#    ���˵Ķ���
    people = []    
#    ��ʼ���˿ͼ�id 
    for i in range(0,total_number):
        person = Consumer(i)   
        people.append(person) 
        
    #    20����̨����
    global queues
    queues = {}
    for i in range(0,20):
        queues[i] = []
        
#    ��ʳ��Ķ���
    global ready_to_roast 
    ready_to_roast = []
    

    index = 0
    sum_at_bar = 0

    flag = True
    while True:
        
        
        if flag and interval == 0:
            index = total_number;
            Restaurant(people[0:])
            flag = False
        
        elif interval!= 0:
            if Time % interval == 0:
                if index < total_number:
                    Restaurant(people[index:index+1])
                    index += 1
                    
        
        Time = Time_goes_by(Time)
        print("time  ",Time)
        sum_at_bar = Bar_to_choose()
        Grill_to_eat()
    
#        �������������������ʱ�����ڰ�̨���� ����С�ڵ���0ʱ�� ���տ��Ķ�������С�ڵ��� 0ʱ
        if index >= total_number and sum_at_bar <= 0 and  len(ready_to_roast) <= 0:
            break
        
    print("�ڰ�̨��ƽ���ȴ�ʱ��Ϊ��",ave_waiting_time_at_bar/total_number);
    print("�ڿ��ܵ�ƽ���ȴ�ʱ��Ϊ��",ave_waiting_time_at_grill/total_number);