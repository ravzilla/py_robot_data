import reader
import matplotlib.pyplot as plt
r=reader.reader("C:\\Users\\Ravi Ponmalai\\Desktop\\test1.txt")

data_list=r.get_final_data()


for i in data_list['Y']:
    
    plt.plot(data_list['X']['TIME'],data_list['Y'][i],'o')
plt.xlabel(r.get_x_list()[0][0]+" "+r.get_x_list()[0][1])
plt.show()