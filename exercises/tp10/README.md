# Bank Account in Java

## Instructions

### We are going to create a Bank Account System

#### 1. Basic System
* Accounts are:
    - Identified by an `accountNumber`
    - Have an Owner (1 for this exercise) with an `idNumber`, and a `name`
    - Have methods to: get the balance, make deposits, withdrawals, and transfers

#### 2. Table of Accounts and Automatic Numbering
* Implement a `static` method to get the list of all accounts.
* Implement a `static` method to get an account based on the `accountNumber`
* Add automatic account numbering

#### 3. Add a Transaction Log to the Accounts

You need to add information about each `deposit`, `withdrawal`, or `transfer`, and be able to list them.

Information should include:

* The transaction type
* The amount
* When the transaction is a transfer, the receiver account
