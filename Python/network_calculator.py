
def network_ip(ip_normal, mask):
    values_ip = ip_normal.split(".")
    values_mask=mask.split(".")
    binary_ip=list(to_binary(values_ip))
    binary_mask=list(to_binary(values_mask))
    network_ip=and_operation(binary_ip,binary_mask)
    network_ip_decimal=list(map(parser_decimal,network_ip))
    broadcast_ip=broadcast_function(binary_mask,network_ip)
    broadcast_decimal=list(map(parser_decimal,broadcast_ip))
    print("The ip network of that ip is ")
    print("{}.{}.{}.{}".format(network_ip_decimal[0],network_ip_decimal[1],network_ip_decimal[2],network_ip_decimal[3]))
    print("The broadcast of that ip is")
    print("{}.{}.{}.{}".format(broadcast_decimal[0],broadcast_decimal[1],broadcast_decimal[2],broadcast_decimal[3]))




def and_operation(bin1,bin2):
    res = [[None for _ in range(8)] for _ in range(4)]
    print(bin1[3][7])
    for i in range(4):
        for j in range(8): 
            res[i][j]= int(bin1[i][j]) & int(bin2[i][j])
    return res    

def to_binary(lista):
    binary_ip=map(lambda x: format (int(x),'08b'),lista)
    return list(binary_ip)

def parser_decimal(num):
    max = 128
    count = 0
    for i in num:
        count += (int(i)*max)
        max=max/2
    return int(count)

def broadcast_function(mask,network):
    lis_n=network
    lis_m=mask
    for i in range(len(lis_n)):
        for j in range(len(lis_m)):
            if int(lis_m[i][j]) == 0:
                lis_n[i][j] = "1"
    print(lis_n)
    return lis_n           

def validation_input(message):
    try:
        num1 = input(message)
        print(num1)
        number = num1.split(".")
        condition = all([int(x) < 256 for x in number])
        if len(number) == 4 and condition:
            return num1
        else:
            print("put in each part of the ip numbers less than 256")
            validation_input(message)
    except:
        print("Remember the format buddy and put integers numbers in the each  part of the ip split with a point")
        validation_input(message)


user_ip = validation_input("Put some ip in this format 192.243.93.32 ")
print(user_ip)
user_mask = validation_input("Put the mask of that ip in this format 255.255.255.224 ")
print(user_mask)

network_ip(user_ip,user_mask)
