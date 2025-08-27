keys=input("enter keys seperated by space: ").split()
num_lists=int(input("enter the number of values lists: "))
result_dict={}
for i in range(num_lists):
    values=input(f"enter values sepearted by space for {keys[1]}: ").split()
    result_dict[keys[i]]=values
print("/ncreated dictionary:")
print(result_dict)

print("hello world")