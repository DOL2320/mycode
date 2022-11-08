#!/usr/bin/env python3
proto = ["ssh", "http", "https"]
protoa = ["ssh", "http", "https"]
print(proto)
proto.append("dns") # this line will add "dns" to the end of our list
protoa.append("dns") # this line will add "dns" to the end of our list
print(proto)
proto2 = [ 22, 80, 443, 53 ] # a list of common ports
proto.extend(proto2) # pass proto2 as an argument to the extend method
print(proto)
protoa.append(proto2) # pass proto2 as an argument to the append method
print(protoa)
print(proto2.remove(443)) # prints 443
print(proto2) # prints [ 22, 80, 53 ]
proto.insert(2, "sftp") # proto = ["ssh", "http", "sftp", "https", "dns", 22, 80, 443, 53 ]
print(proto)
proto.pop() # proto = ["ssh", "http", "sftp", "https", "dns", 22, 80, 443 ]
proto.pop()
proto.pop()
proto.pop()
print(proto)
