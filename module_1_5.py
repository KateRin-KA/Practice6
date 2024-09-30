immutable_var=(1,2,3,True,"Urban")
print(immutable_var)
#immutable_var[0]=2
#print(immutable_var) # Кортеж не изменяемый объект, если отобразить так выводит ошибку
mutable_list=(1,2,3,True,'Urban')
print(mutable_list)
immutable_list[0]=2
print(mutable_list)