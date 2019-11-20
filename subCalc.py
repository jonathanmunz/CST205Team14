# Jonathan Munz, David Ruiz, Monica Barrios, Weixuan Jia
# CST205
# 12/16/2019
# Professor Modes
# SubnetCalculator.py
# This programs accepts an IP address and Subnet Mask and provides subnet information.
import numpy 
#Data Structures
ipAddress = []
subnetAddress = []
#Accept user input of IP address and subnet mask
print("Please enter an IP address & subnet mask sperated by periods: ")
userInput = input()
userInput = userInput.split('.', 4)
#Store the ip address and mask into a list
for item in userInput:
    userInputs = int(item)
    ipAddress.append(userInputs)
    subnetAddress.append(userInputs)
#Calculate the classful network address & store it
subnetMask = ipAddress[4]
if(subnetMask >= 24):
    classfulSubnetMask = 24
    nClass = 'C'
elif(subnetMask >= 16):
    classfulSubnetMask = 16
    nClass = 'B'
elif(subnetMask >= 8):
    classfulSubnetMask = 8
    nClass = 'A'
print("\nClassful Subnet Mask:", classfulSubnetMask) 
classfulNetworkAddress = []
classfulBroadcastAddress = []
classfulSubnetMaskDD = []
print("Classful Network Address: ", end = '') 
for x in range (0,4):
    classfulNetworkAddress.append(ipAddress[x])
    classfulBroadcastAddress.append(ipAddress[x])
    classfulSubnetMaskDD.append(ipAddress[x])
if(subnetMask >= 24):
     classfulNetworkAddress[3] = 0
  
elif(subnetMask >= 16):
     classfulNetworkAddress[2] = 0
     classfulNetworkAddress[3] = 0
  
elif(subnetMask >= 8):
      classfulNetworkAddress[1] = 0
      classfulNetworkAddress[2] = 0
      classfulNetworkAddress[3] = 0
for x in range (0, 4):
    print(classfulNetworkAddress[x], end= '.')
#Calculate the classful broadcast address
print ( "\nClassful Broadcast Address: ", end = '') 
if(subnetMask >= 24):
     classfulBroadcastAddress[3] = 255
  
elif(subnetMask >= 16):
    classfulBroadcastAddress[2] = 255
    classfulBroadcastAddress[3] = 255
  
elif(subnetMask >= 8): 
      classfulBroadcastAddress[1] = 255
      classfulBroadcastAddress[2] = 255
      classfulBroadcastAddress[3] = 255
for x in range (0,4): 
    print(classfulBroadcastAddress[x], end= '.')
#Display the classful subnet mask in dotted decimal notation
print("\nClassful Subnet Mask in dotted decimal form: ", end = '') 
if(subnetMask >= 24):
     classfulSubnetMaskDD[0] = 255
     classfulSubnetMaskDD[1] = 255
     classfulSubnetMaskDD[2] = 255
     classfulSubnetMaskDD[3] = 0
elif(subnetMask >= 16):
     classfulSubnetMaskDD[0] = 255
     classfulSubnetMaskDD[1] = 255 
     classfulSubnetMaskDD[2] = 0
     classfulSubnetMaskDD[3] = 0
  
elif(subnetMask >= 8):
      classfulSubnetMaskDD[0] = 255
      classfulSubnetMaskDD[1] = 0
      classfulSubnetMaskDD[2] = 0
      classfulSubnetMaskDD[3] = 0
for x in range (0,4): 
    print(classfulSubnetMaskDD[x], end= '.') 
#Find total usable hosts per subnet
hostBitsC = 32 - subnetMask
hostBitsB = 32 - subnetMask - 8
hostBitsA = 32 - subnetMask - 16
totalHostsPerSubnetC = pow (2, hostBitsC)
totalHostsPerSubnetB = pow (2, hostBitsB)
totalHostsPerSubnetA = pow (2, hostBitsA)
usableHostsPerSubnet = int(totalHostsPerSubnetC - 2)
print("\nNumber of usable hosts per subnet:", usableHostsPerSubnet, end = '')
#Class A B or C?
print("\nClassful Network: " + nClass, end = '')
#Calculate the subnet range
validHost = True
#Class C
if(subnetMask >= 24):
    evenDiv = int(ipAddress[3] / totalHostsPerSubnetC) 
    netStart = evenDiv * totalHostsPerSubnetC 
    subnetAddress[3] = netStart
    print("\nSubnet Network Address: ", end = '')
    for x in range (0,4): 
        print(subnetAddress[x], end = '.')
    #validHost Network Address
    if(subnetAddress[len(subnetAddress) -2] == ipAddress[len(subnetAddress) -2]):
        validHost = False
    #Obtain first host in network
    firstHost = subnetAddress[3] + 1
    print ("\nHost range within subnet: ", end = '') 
    for x in range (0,3): 
        print(subnetAddress[x], end = '.') 
    print(firstHost, end = '')
    print(" - ", end = '')
    #Obtain subnet broadcast & last host in network
    subnetBroadcastAddress = subnetAddress[3] + totalHostsPerSubnetC -1
    lastHost = subnetAddress[3] + totalHostsPerSubnetC -2
    for x in range (0,3):
        print(subnetAddress[x], end = ".")
    print(lastHost) 
    print("Subnet Broadcast Address: ", end = '')
    for x in range (0,3):
        print(subnetAddress[x], end = ".") 
    
    print(subnetBroadcastAddress) 
    if(subnetBroadcastAddress == ipAddress[len(subnetAddress) -2]): 
        validHost = false 
#Class B 
elif(subnetMask >= 16):
    evenDiv = ipAddress[2] / totalHostsPerSubnetB
    netStart = evenDiv * totalHostsPerSubnetB
    subnetAddress[2] = netStart
    subnetAddress[3] = 0
    print("\nSubnet Network Address: ", end = '')
    for x in range (0,4):
        print(subnetAddress[x], end = ".")
    
#validHost Network Address check
    if(subnetAddress[len(subnetAddress) -2] == ipAddress[len(subnetAddress) -2]): 
        validHost = false
    
#Add one to this to get first Host
    firstHost = subnetAddress[3] + 1
    print("\nHost range within subnet: ", end ='')
    for x in range (0,4):
        print(subnetAddress[x], end =".")
    print(firstHost) 
    blockSize = subnetAddress[3] + totalHostsPerSubnetC
    octet3 = (blockSize / 256) + subnetAddress[2] -1
    octet4 = blockSize % 256
    if(octet4 == 0): 
        octet4 = 255
    print(" - ")
    for x in range (0,3): 
        print(subnetAddress[x], end = ".")
    print(octet3, end = ".")
    print(octet4 -1, end = "")
    print("\nSubnet Broadcast Address: ", end ='')
    for x in range(0,3):
        print(subnetAddress[x] + ".")
    print(octet3, ".")
    print(octet4)
#ValidHost Broadcast
    if(octet4 == ipAddress[len(subnetAddress)-2]): 
        validHost = false
    
#Class A  
elif(subnetMask >= 8): 
    evenDiv = ipAddress[1] / totalHostsPerSubnetA
    netStart = evenDiv * totalHostsPerSubnetA
    subnetAddress[1] = netStart
    subnetAddress[2] = 0
    subnetAddress[3] = 0
    print("\nSubnet Network Address: ", end ='')
    for x in range(0,3):
        print(subnetAddress[x], end =".")
#validHost Network address compare
    if(subnetAddress[len(subnetAddress)-2] == ipAddress[len(subnetAddress) -2]):
        validHost = false
#First Host in network
    firstHost = subnetAddress[3] + 1
    print("\nHost range within subnet: ", end ='')
    for x in range (0,2):
        print(subnetAddress[x], end ='.')
    print(firstHost)
    print(" - ")
   
    blockSize = subnetAddress[3] + totalHostsPerSubnetC
    octet3 = (blockSize / 256) + subnetAddress[2] -1
    octet2 = octet3 / 256
    octet3 = 255
    octet4 = 255 
    print("") 
    for x in range(0,1):
        print(subnetAddress[x], end='.')
    print(octet2, ".", octet3, ".", octet4 - 1) 
    print("\nSubnet Broadcast Address: ") 
    for x in range (0,1): 
        print(subnetAddress[x], end = ".")
    print(octet2, ".", octet3, ".", octet4)
    if(octet4 == ipAddress[len(subnetAddress) -2]): 
        validHost = false
# Valid host address
print("Is it a valid Host Address?: ", end='')
if(validHost): 
    print("Yes")
else:
    print("No")