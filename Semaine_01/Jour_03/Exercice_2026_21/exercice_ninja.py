class Phone:
    def __init__(self, phone_number):
        self.phone_number = phone_number
        self.call_history = []
        self.add = []


    def call(self, other_phone):
        self.call_history.append(other_phone.phone_number)
        print(f"Calling {other_phone.phone_number} from {self.phone_number}...")
    
    
    def show_call_history(self):
        print(f"Call history for {self.phone_number}: {', '.join(self.call_history)}")
    
    def send_message(self, other_phone, message):
        message = {"to": other_phone.phone_number, "from": self.phone_number, "message": message}
        self.add.append( message)
        print(f"Sending message to {other_phone.phone_number} from {self.phone_number}: {message['message']}")


    def show_outgoing_messages(self):
        print(f"Outgoing messages from {self.phone_number}: {', '.join([msg['message'] for msg in self.add if msg['from'] == self.phone_number])}")

    def show_incoming_messages(self):
        incoming_messages = [msg for msg in self.add if msg['to'] == self.phone_number]
        print(f"Incoming messages for {self.phone_number}: {', '.join([msg['message'] for msg in incoming_messages])}")

    def show_messages_from(self):
        messages_from = {}
        for msg in self.add:
            if msg['to'] == self.phone_number:
                sender = msg['from']
                if sender not in messages_from:
                    messages_from[sender] = "Aucun message reçu de ce contact"
                messages_from[sender].append(msg['message'])
        print(f"Messages received by {self.phone_number} from each sender: {', '.join([f'{sender}: {', '.join(messages)}' for sender, messages in messages_from.items()])}")


my_phone = Phone("123-456-7890")
other_phone = Phone("987-654-3210")
my_phone.call(other_phone)
my_phone.show_call_history()
my_phone.send_message(other_phone, "Hello, how are you?")
my_phone.show_outgoing_messages()
other_phone.show_incoming_messages()
other_phone.show_messages_from()

