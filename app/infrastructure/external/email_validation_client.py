import random

class EmailValidationClient:

    def validate(self, email):
        return {
            "trust-score": random.randint(50, 100),
            "category": "business",
            "bounce-status": False
        }
