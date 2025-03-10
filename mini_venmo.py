import cmd
from user import User

from itertools import count


class MiniVenmo(cmd.Cmd):
    intro = "ttest"

    def __init__(self):
        self.counter = count()
        self.users: dict[int, User] = dict()
        self.transactions = list()
        super().__init__()

    def do_create_user(self, line):
        name, balance, credit_card = line.split(" ")
        user = User(_balance=0, name=name, credit_card=credit_card)
        user.balance = float(balance)
        id = next(self.counter)
        self.users[id] = user
        print(f"User {name} created. {id=}")

    def do_transaction(self, line):
        sender_user_id, receiver_user_id, value, transaction_name = line.split(
            " ")
        sender_user = self.users[int(sender_user_id)]
        receiver_user = self.users[int(receiver_user_id)]
        sender_user.pay(float(value), receiver_user)
        transaction = f"{sender_user.name} paid {receiver_user.name} ${value} for {transaction_name}"
        self.transactions.append(transaction)
        print(transaction)

    def do_retrieve_activity(self, _):
        for t in self.transactions:
            print(t)

    def do_quit(self, _):
        return True
