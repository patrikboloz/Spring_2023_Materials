#include <iostream>
#include <string>
#include <list>
using namespace std;

struct BankAccount 
{
    string Name;
    int Balance;

    BankAccount(string name, int balance) 
    {
        Name = name;
        Balance = balance;
    }
    bool operator==(const BankAccount& bnkAccount) const
    {
        return this->Name == bnkAccount.Name;
    }
    
};

ostream& operator<<(ostream& COUT, BankAccount& bnkAccount) 
{
    COUT << "Name: " << bnkAccount.Name << endl;
    COUT << "Subscribers: " << bnkAccount.Balance << endl;
    return COUT;
}

struct MyBankCollection 
{
    list<BankAccount>myBankAccounts;

    void operator+=(BankAccount& bnkAccount) 
    {
        this->myBankAccounts.push_back(bnkAccount);
    }
    void operator-=(BankAccount& bnkAccount) 
    {
        this->myBankAccounts.remove(bnkAccount);
    }
};

ostream& operator<<(ostream& COUT, MyBankCollection& accountCollection) 
{
    for (BankAccount bnkAccount : accountCollection.myBankAccounts)
        COUT << bnkAccount << endl;
    return COUT;
}

int main()
{
    BankAccount bankacc1 = BankAccount("Patrik", 82000);
    BankAccount bankacc2 = BankAccount("Blue", 10000);

    MyBankCollection bankAccColl;
    bankAccColl += bankacc1;
    bankAccColl += bankacc2;
    //bankAccColl -= bankacc2;

    cout << bankAccColl;
    
    return 0;
}