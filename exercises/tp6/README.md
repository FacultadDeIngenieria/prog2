# Bank Account

## Instructions
 
### We are going to create a Bank Account System

### 1. Basic System
* Accounts are:
    - Identified by an `account_number`
    - Have an Owner (1 for the exercise) with an `id_number`, and a `name`
    - Have operations to: get the balance, make deposits, withdrawals and transfers

### 2. Table of accounts and automatic numbering
* Implement a `staticmethod` method to get the list of all accounts.
* Implement a `staticmethod` method to get an account based on the `account_number`
* Add automatic account numbering

### 3. Add a Transaction log to the accounts

You need to add information about each `deposit`, `withdrawal` or `transfer`, and be able to list them.

Information should include:

* The transaction type
* The amount
* When the transaction is a transfer, the receiver account