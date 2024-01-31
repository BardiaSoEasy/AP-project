import re


def username_validation(self):
    message: str = "invalid UserName"
    if self.username.count(".") > 1:
        raise Exception(message)
    elif self.username.count("_") > 1:
        raise Exception(message)
    elif self.username.find(".") >= 0 and self.username.find("_") >= 0:
        raise Exception(message)
    else:
        items = self.username.replace(".", "@").replace("_", "@").split("@")
        if len(items) != 2:
            raise Exception(message)
        elif len(items[0]) == 0 or len(items[1]) == 0:
            raise Exception(message)
        elif not items[0].isalpha() or not items[1].isalpha():
            raise Exception(message)
                    
def email_validation(self, email):
    count1=email.count('@')
    count2=email.count('.')
    if count1!=1:
        raise Exception("invalid Email")
    if count2<1 or count2>2:
        raise Exception("invalid Email")
            
    #parts
    parts =re.split('[@]', email)
    username0=parts[0]
    partsp=re.split('[.]', parts[1])
    if len(partsp)!=2:
        raise Exception("invalid Email")            
    domain=partsp[0]
    tld=partsp[1]
    #tld
    if tld.isalpha()==False:
        raise Exception("invalid Email")
    if len(tld)>3 or len(tld)<2:
        raise Exception("invalid Email")
    #domain
    if domain.isalnum()==False:
        raise Exception("invalid Email")
    #username
    m=0
    point=0
    for j in range(len(username0)):
        if username0[j].isalnum()==False and username0[j]!='.' and username0[j]!='_':
            m+=1
        if username0[j]=='.':
            point+=1
    if m>0:
        raise Exception("invalid Email")
    return email
                    
def password_validation(self):
        message: str = "invalid Password"
        if len(self.password) < 8:
            raise Exception(message)
        elif self.password.find("#") == -1 and self.password.find("$") == -1 and self.password.find("@") == -1 and self.password.find("!") == -1:
            raise Exception(message)
        elif not self.password.replace("#", "").replace("$", "").replace("@", "").replace("!", "").isalnum():
            raise Exception(message)
        else:
            upperCounter = 0
            lowerCounter = 0
            digitCounter = 0
            for i in self.password:
                if i >= "A" and i <= "Z":
                    upperCounter = upperCounter + 1
                elif i >= "a" and i <= "z":
                    lowerCounter = lowerCounter + 1
                elif i >= "0" and i <= "9":
                    digitCounter = digitCounter + 1
            if upperCounter == 0 or lowerCounter == 0 or digitCounter == 0:
                raise Exception(message)
    
