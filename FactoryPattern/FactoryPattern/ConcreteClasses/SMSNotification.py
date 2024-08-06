from Interface.INotification import INotification

class SMSNotification(INotification):
    def notify(self, message) -> str:
        return 'Sending SMS with Message: ', message


