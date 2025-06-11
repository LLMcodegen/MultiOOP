
class TLI:
    def __init__(self, transactions):
        self.transactions = transactions
class SN_TLI(TLI):
    def Transaction_List(self):
        invalid_transactions = []
        transaction_data = []
        for transaction in self.transactions:
            name, time, amount, city = transaction.split(',')
            transaction_data.append((name, int(time), int(amount), city))
        for i, (name, time, amount, city) in enumerate(transaction_data):
            if amount > 1000:
                invalid_transactions.append(self.transactions[i])
            for j in range(len(transaction_data)):
                if i != j:
                    other_name, other_time, other_amount, other_city = transaction_data[j]
                    if name == other_name and abs(time - other_time) <= 60 and city != other_city:
                        invalid_transactions.append(self.transactions[i])
                        break
        return list(set(invalid_transactions))

#--------------:
print(SN_TLI(["alice,20,800,mtv","bob,50,1200,mtv","bob,60,100,mtv"]).Transaction_List() == ['bob,50,1200,mtv'])
