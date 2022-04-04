class Category:
    def __init__(self, n) -> None:
        self.name = n
        self.ledger = [ ]
        self.total = 0

    def __str__(self):
        catString = '{0:*^30}'.format(self.name)
        for entry in self.ledger:
            catString = catString + '\n' + '{0:<23}{1:>7.2f}'.format("%.23s" % entry['description'], entry['amount'])
        return catString

    def deposit(self, amt, desc='') -> None:
        self.ledger.append({"amount": amt, "description": desc})
        self.total = self.total + amt

    def withdraw(self, amt, desc='') -> bool:
        if self.check_funds(amt):
            self.ledger.append({"amount": -amt, "description": desc})
            self.total = self.total - amt
            return True
        else:
            return False

    def get_balance(self) -> float:
        return self.total

    def transfer(self, amt, cat) -> bool:
        if self.check_funds(amt):
            self.withdraw(amt, 'Transfer to [' + cat.name + ']')
            cat.deposit(amt, 'Transfer from [' + self.name + ']')
            return True
        else:
            return False

    def check_funds(self, amt) -> bool:
        if self.total >= amt:
            return True
        else:
            return False

def create_spend_chart(categories):
    chart_string = 'Percentage spent by category'
    total_spend = [ ]
    total = 0
    for cat in categories:
        for entry in cat.ledger:
            if entry['amount'] < 0:
                total_spend.append({"category": cat, "amount": abs(entry['amount'])})

    for entry in total_spend:
        total += entry['amount']

    
  
    return chart_string