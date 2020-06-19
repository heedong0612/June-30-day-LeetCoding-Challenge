def validIPAddress(IP: str) -> str:
    def hasLeadingZeros(num: str) -> bool:
        # special case for '0'
        if num == '0':
            return False

        return len(num) != len(num.lstrip('0'))
    
    def checkIPV4(IP: str) -> bool:
        '''
        Check if valid IPV4 address
        '''
        ipArr = IP.split('.')

        # check if separated to four groups
        if len(ipArr) != 4:
            return False

        for num in ipArr:
            n = 0
            
            if hasLeadingZeros(num):
                return False
            
            # if no string at all
            if len(num) == 0:
                return False
            
            # if negative number
            if num[0] == '-':
                return False
            
            try:
                # n must be an int
                n = int(num)
            except:
                return False

            # n must be 0 ... 255
            if n not in range(256):
                return False

        return True

    def checkIPV6(IP: str) -> bool:
        '''
        Check if valid IPV6 address
        '''
        ipArr = IP.split(':')

        # check if separarated to eight groups
        if len(ipArr) != 8:
            return False

        for numString in ipArr:
            # each group has to be in a one to four hexabit format
            if len(numString) > 4 or len(numString) == 0:
                return False
            
            if numString[0] == '-':
                return False
            
            try:
                # must be valid 16 bit format
                int(numString, 16)
            except:
                return False
            
        return True

    if checkIPV4(IP):
        return 'IPv4'

    if checkIPV6(IP):
        return 'IPv6'

    return 'Neither'            

if __name__ == "__main__":
    test = "172.16.254.a"
    test = "192.0.0.1"
    print(validIPAddress(test))