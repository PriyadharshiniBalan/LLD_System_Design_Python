from Interface.INotification import INotification

class EmailNotification(INotification):
    def notify(self, message) -> str:
        return 'Sending Email with Message: ', message


