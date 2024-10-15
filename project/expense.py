from datetime import datetime

class Expense:
    def __init__(self, amount, description,category,date):
        self.amount = amount
        self.description = description
        self.category = category
        self.date = datetime.strptime(date, '%Y-%m-%d')
    
    def __str__(self):
        return f"Amount: {self.amount}, Description: {self.description}, Category: {self.category['name']}, Date: {self.date}"

