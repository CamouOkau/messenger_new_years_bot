from fbchat import Client
from fbchat.models import Message as fb_message


class MessengerBot:
    def __init__(self, email, password):
        """ A bot for sending messages through messenger. """
        self.email = email
        self.password = password
        self.client = Client(email, password)

    def uid(self, username):
        """ Returns all the uid of the user. """
        try:
            user = self.client.searchForUsers(username)[0]
            return user.uid

        except IndexError:
            print(f"User \"{username}\" does not exist!")
    
    def send_message(self, message, uid):
        """ Send a message to uids at a given time, if one is given. """
        if type(uid) is str:
            message = fb_message(message)
            self.client.send(message, uid)

        else:
            print("Uid \"{uid}\" does not exist!")
    
    def logout(self):
        """ logs out with the bot. """
        self.client.logout()