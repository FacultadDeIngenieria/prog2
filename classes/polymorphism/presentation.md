class: center, middle, inverse

# Polymorphism

---

## Agenda

1. What is polymorphism?
2. Inheritance vs Polymorphism
3. Polymorphism in Python
4. Polymorphism in Java
5. What are interfaces?
6. Interfaces in Python
7. Interfaces in Java

---

## What is polymorphism?

- Polymorphism is the ability of an object to take on many forms, or the ability to send
the same message to different objects and get different behaviors.
- Polymorphism is often expressed as "one interface, many implementations".
- Polymorphism can be achieved by using inheritance and interfaces. (we are going to define interfaces later)

---

## Polymorphism in Java, with inheritance

```java

abstract class PaymentMethod {
    abstract float charge(float amount);
}

```

---

```java

class CreditCard extends PaymentMethod {
    float charge(float amount) {
        System.out.println("Charging " + amount + " with Credit Card");
        // validate the credit card information
        // reach out to the bank to charge the amount
        // wait until the bank responds
        // returns the amount actually charged
        return amount;
    }
}

```

---

```java

class Cash extends PaymentMethod {
    float charge(float amount) {
        System.out.println("Charging " + amount + " with Cash");
        // count the amount of cash
        // calculate the change
        // inform the user about the change
        // returns the amount actually charged
        return amount;
    }
}


```

---

```java

class CriptoCurrency extends PaymentMethod {
    float charge(float amount) {
        System.out.println("Charging " + amount + " with CriptoCurrency");
        // validate the wallet
        // reach out to the blockchain to charge the amount
        // wait until the blockchain responds
        // returns the amount actually charged
        return amount;
    }
}

```


---

## How do we use polymorphism?

```java

class ShoppingCart {
    PaymentMethod paymentMethod;

    void setPaymentMethod(PaymentMethod paymentMethod) {
        this.paymentMethod = paymentMethod;
    }

    void checkout(float amount) {
        float chargedAmount = paymentMethod.charge(amount);
        System.out.println("Charged " + chargedAmount);
    }
}


```

---

## Polymorphism in Python

```python

class Notification:
    def send(self, user: User, message: Message) -> bool:
        pass

```

---

```python

class EmailNotification(Notification):
    def send(self, user: User, message: Message) -> bool:
        print(f"Sending email to {user.email} with message {message.text}")
        // validate the email
        // reach out to the email server
        // wait until the email server responds
        // returns whether the email was sent
        return True

```

---

```python

class SmsNotification(Notification):
    def send(self, user: User, message: Message) -> bool:
        print(f"Sending SMS to {user.phone} with message {message.text}")
        // validate the phone number
        // reach out to the SMS server
        // wait until the SMS server responds
        // returns whether the SMS was sent
        return True

```

---

```python

class PushNotification(Notification):
    def send(self, user: User, message: Message) -> bool:
        print(f"Sending push notification to {user.device} with message {message.text}")
        // validate the device
        // reach out to the push notification server
        // wait until the push notification server responds
        // returns whether the push notification was sent
        return True

```

## How do we use polymorphism?

```python

class OTPService:
    notification: Notification

    def set_notification(self, notification: Notification):
        self.notification = notification

    def send_otp(self, user: User) -> bool:
        otp = generate_otp()
        return self.notification.send(user, Message(otp))

```

---

## What are interfaces?

- An interface is a contract that defines the methods that a class must implement.
- An interface is a reference type in Java, similar to a class, that can contain
only constants, method signatures, default methods, static methods, and nested types.

---

## Interfaces in Java, used as "IS-A"

```java

interface PaymentMethod {
    float charge(float amount);
}

interface Notification {
    boolean send(User user, Message message);
}

```

---

## Interfaces in Java, used as "CAN-DO"

```java

interface CSVSavable {
    CSV toCSV();
}

interface Nameable {
    String getName();
}

interface Runnable {
    void run();
}

```

## Multiple inheritance in Java

```java

class Student implements Nameable, CSVSavable {
    String name;

    public String getName() {
        return name;
    }
    
    public CSV toCSV() {
        return new CSV(name);
    }
}

```

---

## Interfaces vs Abstract Classes

State: Interfaces cannot have instance fields, while abstract classes can have fields.

Because of that reason, abstract classes can define constructors, while interfaces cannot.

---

