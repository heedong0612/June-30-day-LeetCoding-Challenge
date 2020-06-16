class Solution:
    def validIPAddress(self, IP: str) -> str:
        ipv4arr = IP.split(".")
        if len(ipv4arr) == 4:
            if self.checkIPv4(ipv4arr) :
                return "IPv4"
            
        ipv6arr = IP.split(":")
        
        if len(ipv6arr) == 8:
            if self.checkIPv6(ipv6arr):
                return "IPv6"
            
        return "Neither"
    

    def checkIPv4(self, IP):
        for s in IP:
            if not s.isnumeric():
                return False
            if int(s) < 0 or int(s) > 255:
                return False
            if s[0] == '0' and int(s) != 0:
                return False
            if int(s) == 0 and len(s) > 1:
                return False
            
        return True
    
    
    def checkIPv6(self, IP):
        for s in IP:
            if len(s) > 4 or len(s) == 0:
                return False
            
            for c in s:
                if not c.isnumeric(): # then check if a~f or A~F
                    if ord(c.lower()) < ord('a') or ord(c.lower()) > ord('f'):
                        return False
                
        return True
                
                