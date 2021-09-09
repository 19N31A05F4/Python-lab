#python program to convert nested tuple to custom key dictonaries
tup_1=((1,'anji',29),(2,'rakesh',49),(3,'naveen',47),(4,'tarun',57))
print(tup_1)
new_tup_1=[{'key':sub[0],'value':sub[1],'id':sub[2]} for sub in tup_1]
print('The converted dictionary is:',new_tup_1)