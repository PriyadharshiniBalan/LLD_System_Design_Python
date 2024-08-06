from FactoryClass.NotificationFactory import NotificationFactory

def main():
    #Create a factory
    factory = NotificationFactory()

    # Get an email notification object
    email_notifier = factory.get_notification("email")
    print(email_notifier.notify("Hello via Email!"))

    # Get an SMS notification object
    sms_notifier = factory.get_notification("sms")
    print(sms_notifier.notify("Hello via SMS!"))

if __name__ == "__main__":
    main()