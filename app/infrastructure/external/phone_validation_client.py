import random

class PhoneValidationClient:

    def validate(self, phone):
        return {
            "trust-score": random.randint(50, 100),
            "service-provider": "Airtel",
            "privacy-enabled": False
        }
