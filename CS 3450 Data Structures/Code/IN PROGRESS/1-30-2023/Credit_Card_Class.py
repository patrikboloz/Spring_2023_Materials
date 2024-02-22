class CreditCard():
    """ A consumer credit card."""
    
    def __init__(self, customer, bank, acnt, limit):
        """ Create a new credit card instance.
        
        The initial balance is zero.
        
        customer the name of the customer ('John')
        bank     the name of the bank ('Wells Fargo')
        acnt     the account identifier ('5432 5568')
        limit    credit limit measures in dollars
        """
        
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = 0
        
    def get_customer(self):
        """Return the name of the customer"""
        return self._customer
        
    def get_bank(self):
        """Return the name of the bank"""
        return self._bank
        
    def get_account(self):
        """Return the card identifying number"""
        return self._account 
        
    def get_limit(self):
        """Return current credit limit"""
        return self._limit
        
    def get_balance(self):
        """Return current balance"""
        return self._balance
        
    def charge(self, price):
        """Charge given price to the card, assuming sufficient credit limit 
           Return True if charge was processed, False if charge was denied."""
           
        if price + self._balance > self._limit:
            return False
        else:
            self._balance = self._balance + price
            return True
            
    def make_payment(self, amount):
        """Process customer payment that reduces balance"""
        self._balance = self._balance - amount
    
    
    
#credit_card_1 = CreditCard("John", "Wells Fargo", "2002", 5000)
#credit_card_2 = CreditCard("Patrik", "United", "9000", 600)        
    
#print(credit_card_1.get_balance())
#print(credit_card_1.get_bank())
#print(credit_card_1.get_account())

#print(credit_card_1.charge(1000))
#print(credit_card_1.get_balance())


if __name__ == '__main__':
    wallet = []
    wallet.append(CreditCard('John', 'Wells Fargo', '120', 5000))
    wallet.append(CreditCard('Patrik', 'United', '650', 2000))
    wallet.append(CreditCard('Mike', 'Wells Fargo', '900', 3000))
    
    #print(wallet)
    #print(wallet[0].get_customer())
    #print(wallet[1].get_customer())
    #print(wallet[2].get_customer())
    
    for val in range(1, 17):
        wallet[0].charge(val)
        wallet[1].charge(val*2)
        wallet[2].charge(val*3)
        
    for c in range(3):
        print('Customer =', wallet[c].get_customer())
        print('Bank =', wallet[c].get_bank())
        print('Account =', wallet[c].get_account())
        print('Limit =', wallet[c].get_limit())
        print('Balance =', wallet[c].get_balance())
        
        while wallet[c].get_balance() > 100:
            wallet[c].make_payment(100)
            print('New balance =', wallet[c].get_balance())
        print()



class PredatoryCreditCard(CreditCard):
    """ An extension to CreditCard that compounds interest and fees"""
    
    def __init__(self, customer, bank, acnt, limit, apr):
    """ Create a new predatory credit card instance.
    
    The initial balance i a zero
    
    customer the name of the customer
    bank     the name of the bank
    acnt     the account identifier
    limit    credit limit
    apr      annual percentage rate (e.g., 0.0825 for 8.25% APR)
    """
        super().__init__(customer, bank, acnt, limit)
        self._apr = apr
        
    def charge(self, price):
    """ Charge given price to the card, assuming sufficient credit limit.
    
    Return True if charge was processed.
    Return False and assess $5 fee if charge is denied
    """
    
        success = super().charge(price)   #call inherited method
        if not success:
            self._balance += 5  #asses penalty
        return success #caller expects return value
        
    def process_month(self):
    """Assess mnothly interest outstanding balance """
        if self._balance > 0:
            #if positive balance, convert APR to monthly multiplicative factor
            monthly_factor = pow(1 + self_apr, 1/12)
            self._balance *= monthly_factor
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
    

    
    
    
    
    
    
        
        
        
        
           
    
    
    
    
    
    
     
        
        
        
