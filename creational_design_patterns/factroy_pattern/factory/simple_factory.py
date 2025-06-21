# Notification system example at a very samll scale

class Notification:
    def send(self, msg):
        self.msg = msg


class Email(Notification):
    def send(self, msg):
        print(msg)
    
class SMS(Notification):
    def send(self, msg):
        print(msg)
    


# client code
def client_call(msgType: str):
    if msgType == "email":
        return Email()
    elif msgType == "sms":
        return SMS()
    

cc = client_call("email")
cc.send("Email sent from client!")

