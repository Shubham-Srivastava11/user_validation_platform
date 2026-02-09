from app.infrastructure.external.email_validation_client import EmailValidationClient
from app.core.logger import logger


class EmailValidator:

    def __init__(self):
        self.client = EmailValidationClient()

    def validate(self, email):

        logger.info("email_validation_started", email=email)

        result = self.client.validate(email)

        logger.info(
            "email_validation_completed",
            email=email,
            trust_score=result["trust-score"],
            bounce=result["bounce-status"]
        )

        return {
            "value": email,
            "trust_score": result["trust-score"],
            "is_valid": not result["bounce-status"]
        }
