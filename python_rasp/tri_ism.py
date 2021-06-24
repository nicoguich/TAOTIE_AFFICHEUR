import string


ism = open("pre_26avril.txt", "r")
num_lines_ism = sum(1 for line in open('pre_26avril.txt'))
prob_ism=[None]*num_lines_ism
temp_list_ism=[None]*num_lines_ism
print("nombre de ism avant : "+ str(num_lines_ism))


ism2 = open("pre2.txt", "w+")
list_ism2=[]
compteur_ism=0

index_ism=0
for line in ism:
    temp_list_ism[index_ism]=line
    temp_list_ism[index_ism]=temp_list_ism[index_ism][:-1]
    split_ism=temp_list_ism[index_ism].split("/")
    temp_list_ism[index_ism]=split_ism[0]
    if len(split_ism[0])<9:
        #print(split_ism[0])
        ism2.write(line)
        compteur_ism+=1
    index_ism+=1

ism2.close()
#print(list_ism2)
print("nombre de ism après : "+ str(compteur_ism))
