from netaddr import *
class ipaddr():
	def _init_(self,ip=[0,0,0,0],na=[0,0,0,0]):
		self.ip = ip
		self.na = na
	def _str_(self):
		ipformat = " "
		for ips in self.ip:
			ipformat = ipformat + str(ips) + "."
		return("The IP address is :" + ipformat)
	def _add_(self,other):
		return ([self.ip[0]*other.ip[0],self.ip[1]*other.ip[1],self.ip[2]*other.ip[2],self.ip[3]*other.ip[3]])
myip = ipaddr([192.168.10.1],[255.255.255.0])
addip = ipaddr([2,1,1,1])
result = myip + addip
print(myip)
print(result)
print(result.broadcast)
print(result.cidr)
print(result.netmask)
print(result.hostmask)
print(result.network)
print(result.size)
