class SavingAccount:
    def __init__(self,account_num,int_rate,bal):
        self.account_num = account_num
        self.interest_rate = int_rate
        self.balance = bal

    def set_account_num(self,account_num):
        self.account_num = account_num
    def set_interest_rate(self,int_rate):
        self.interest_rate = int_rate
    def set_balance(self,bal):
        self.balance = bal

    def get_account_num(self):
        return self.account_num
    def get_interest_rate(self):
        return self.interest_rate
    def get_balance(self):
        return self.balance

class CD(SavingAccount):
    def __init__(self,account_num,int_rate,bal,mat_date):
        SavingAccount.__init__(self,account_num,int_rate, bal)
        self.maturity_date = mat_date

    def set_maturity_date(self,mat_date):
        self.maturity_date = mat_date

    def get_maturity_date(self):
        return self.maturity_date