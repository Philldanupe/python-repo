# Create an empty list

services = []

# Populate the list using append or insert

assert services == [], f"Expected 'services' to be [] but got: {repr(services)}"
services.append('EC2')
services.append('S3')
services.append('Lambda')
services.append('CloudWatch')
services.append('SNS')

# Print the list and the length of the list
print(services)
print (len(services))

# Remove two specific services from the list by name or by index

del services[0]
del services[1]

# Print the new list and the new length of the list

print(services)
print(len(services))
