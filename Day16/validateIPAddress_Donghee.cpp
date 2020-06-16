class Solution {
public:
    string validIPAddress(string IP) {
        if (IP.size() == 0) return "Neither";
        if (IP[0] == ':' || IP[0] == '.' || IP[IP.size()-1] == ':' || IP[IP.size()-1] == '.') 
            return "Neither";
        
        vector<string> i4;
        string curr = "";
        
        for (int i = 0; i < IP.size(); i++) {
            if (IP[i] != '.') {
                curr += IP[i];
            } else {
                i4.push_back(curr);
                curr = "";
            }
        }
        
        if (curr != "") {
            i4.push_back(curr);
            curr = "";
        }
        
        if (i4.size() == 4) {
            if (checkIPv4(i4)) {
                return "IPv4";
            }
        }
        
        vector<string> i6;
        curr = "";

        for (int i = 0; i < IP.size(); i++) {
            if (IP[i] != ':') {
                curr += IP[i];
            } else {
                i6.push_back(curr);
                curr = "";
            }
        }
        
        if (curr != "") {
            i6.push_back(curr);
            curr = "";
        }
        
        if (i6.size() == 8) {
            if (checkIPv6(i6)) {
                return "IPv6";
            }
        }
        
        return "Neither";
    }
    
    bool checkIPv4(vector<string> IP) {
        for (string s: IP) {
            for (char c: s) {
                if(!isdigit(c)) 
                    return false;
            } 
            if (s.length() == 0 || s.length() > 3) return false;
            int sint = stoi(s);
            if (sint < 0 || sint > 255) return false;
            if (s[0] == '0' && sint != 0) return false;
            if (sint == 0 && s.length() > 1) return false;
        } 
        return true;
    }
    
    bool checkIPv6(vector<string> IP) {
        for (string s: IP) {
            if (s.length() > 4 || s.length() == 0) return false;
            
            for (char c: s) {
                if (!isdigit(c)) { // then check if a ~ f or A ~ F
                    c = tolower(c);
                    if (c < 'a' || c > 'f') return false;
                    
                }
            }
        }
        return true;
    }
};