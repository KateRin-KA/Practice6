immutable_var=(1,2,3,True,"Urban")
print(immutable_var)
#immutable_var[0]=2
#print(immutable_var) # Кортеж не изменяемый объект, если отобразить так выводит ошибку
mutable_list=('work','sleep','paty')
print(mutable_list)
mutable_list[1]='Vacation'
print(mutable_list)