from Interface.INotification import INotification
from ConcreteClasses.EmailNotification import EmailNotification
from ConcreteClasses.SMSNotification import SMSNotification

class NotificationFactory:
    @staticmethod
    def get_notification(notification_type) -> INotification:
        if notification_type == "email":
            return EmailNotification()
        elif notification_type == "sms":
            return SMSNotification()
        else:
            raise ValueError("Unknown notification type")