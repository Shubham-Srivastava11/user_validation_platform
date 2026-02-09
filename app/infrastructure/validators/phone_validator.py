from app.infrastructure.external.phone_validation_client import PhoneValidationClient
from app.core.logger import logger


class PhoneValidator:

    def __init__(self):
        self.client = PhoneValidationClient()

    def validate(self, phone):

        logger.info("phone_validation_started", phone=phone)

        result = self.client.validate(phone)

        logger.info(
            "phone_validation_completed",
            phone=phone,
            trust_score=result["trust-score"]
        )

        return {
            "value": phone,
            "trust_score": result["trust-score"],
            "is_valid": True
        }
