import random
import string



def randStr(chars = string.ascii_letters + string.digits, N=10):
	return ''.join(random.choice(chars) for _ in range(N))

message = input("Enter department name: ")
instance_num = int(input("Enter the number of EC2 instances: "))



i = 1
while i <= instance_num:
    instance_name = message + '_' + randStr()
    print(instance_name)
    i+=1
    


