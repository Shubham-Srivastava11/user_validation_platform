from app.domain.entities.user import Email, Phone
from app.core.logger import logger


class ValidationService:

    def __init__(self, email_validator, phone_validator):

        self.email_validator = email_validator
        self.phone_validator = phone_validator

    def validate_emails(self, emails, provider):

        logger.info(
            "email_validation_batch_started",
            provider=provider,
            count=len(emails)
        )

        results = []

        for email in emails:

            result = self.email_validator.validate(email)

            results.append(
                Email(
                    value=result["value"],
                    trust_score=result["trust_score"],
                    provider=provider,
                    is_valid=result["is_valid"]
                )
            )

        logger.info(
            "email_validation_batch_completed",
            provider=provider
        )

        return results

    def validate_phones(self, phones, provider):

        logger.info(
            "phone_validation_batch_started",
            provider=provider,
            count=len(phones)
        )

        results = []

        for phone in phones:

            result = self.phone_validator.validate(phone)

            results.append(
                Phone(
                    value=result["value"],
                    trust_score=result["trust_score"],
                    provider=provider,
                    is_valid=result["is_valid"]
                )
            )

        logger.info(
            "phone_validation_batch_completed",
            provider=provider
        )

        return results
