class Customer:
    def __init__(self, customer_id, name, balance, credit_limit, days_overdue):
        self.customer_id = customer_id
        self.name = name
        self.balance = balance
        self.credit_limit = credit_limit
        self.days_overdue = days_overdue

    def is_overdue(self):
        return self.days_overdue > 0

    def is_high_risk(self):
        return self.balance >= self.credit_limit

    def missing_next_payment(self):
        return self.balance >= (self.credit_limit * 0.8) or self.days_overdue > 7


class RiskService:

    def __init__(self, customers):
        self.customers = customers

    def get_risky_customers(self):
        risky_customers = []

        for customer in self.customers:
            if customer.is_overdue() or customer.is_high_risk() or customer.missing_next_payment():
                risky_customers.append(customer)

        return risky_customers

    def get_customer_summary(self):
        summary = {}

        for customer in self.customers:
            summary[customer.customer_id] = {
                "name": customer.name,
                "balance": customer.balance,
                "days_overdue": customer.days_overdue
            }

        return summary

    def generate_report(self):
        risky_customers = self.get_risky_customers()

        return {
            "total_customers": len(self.customers),
            "amount_risky_customers": len(risky_customers),
            "risky_customers": risky_customers,
            "customers": self.get_customer_summary()
        }

customers = [
    Customer(1, "Alice", 950, 1000, 0),
    Customer(2, "Bob", 1500, 1200, 15),
    Customer(3, "Charlie", 500, 800, 30),
    Customer(4, "Alice", 1100, 1000, 5),
    Customer(5, "David", 800, 1000, 0),
]

risk_service = RiskService(customers)

report = risk_service.generate_report()

print("Customer Report")
print("------------------")
print(f"Total customers: {report['total_customers']}")
print(f"Risky customers count: {report['amount_risky_customers']}")
print(f"Risky customers: {report['risky_customers']}")


for customer_id, details in report["customers"].items():
    print(f"{customer_id}: {details["name"]}: Balance £{details['balance']}, Overdue {details['days_overdue']} days")