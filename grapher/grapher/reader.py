'''
Created on Mar 14, 2016

@author: Ravi Ponmalai
'''

class reader(object):



    def __init__(self, file_path):
        #will open file
        self.data_list=[]
        with open(file_path,'r') as file:
           #using with closes the file after read no matter what
            for line in file.readlines():
                if line!="\n":
                    if line.strip()[0]!='#':
                        self.data_list.append(line.split())
        self.display_parameters()
        self.make_data_list()
    def display_parameters(self):
        
        self.x_list=[]
        self.y_list=[]
        line_num=0
        while self.data_list[line_num][0] !="INIT":
            line_num+=1
        line_num+=1
        
        in_x=False
        in_y=False
        
        while self.data_list[line_num][0] !="ENDINIT":
            if in_y:
                self.y_list.append(self.data_list[line_num])
            if self.data_list[line_num][0]=="Y":
                in_y=True
                in_x=False
            if in_x:
                self.x_list.append(self.data_list[line_num])
            if self.data_list[line_num][0]=="X":
                in_x=True
                in_y=False
            line_num+=1
        self.formated_list={'X':{},'Y':{}}
        for i in self.x_list:
            self.formated_list['X'][i[0]]=[]
        for i in self.y_list:
            self.formated_list['Y'][i[0]]=[]
    def make_data_list(self):
        line_num=0
        while self.data_list[line_num][0] !="START":
                line_num+=1
        line_num+=1
        while self.data_list[line_num][0] !="END":
            line=self.data_list[line_num]
            for i in self.x_list:
                self.formated_list['X'][i[0]].append(line[0])
            for n,i in enumerate(self.y_list):
                data_point=self.to_number(line[n+len(self.x_list)], i[1],5)
                self.formated_list['Y'][i[0]].append(data_point)
            line_num+=1
            
            
    def to_number(self,data_point,type,scale):
        if type=='B':
            if eval(data_point):
                return scale
            else:
                return 0
        elif type=='F':
            return float(data_point)
        
    def get_x_list(self):
        return self.x_list
    def get_y_list(self):
        return self.y_list   
    def get_final_data(self):
        return self.formated_list 
# if __name__=="__main__":
#     r=reader("C:\\Users\\Ravi Ponmalai\\Desktop\\test1.txt")
#     print(r.get_final_data())
    