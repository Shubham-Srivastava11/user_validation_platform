import asyncio
from app.domain.entities.user import Email, Phone


class AsyncValidationService:

    def __init__(self, email_validator, phone_validator):

        self.email_validator = email_validator
        self.phone_validator = phone_validator


    async def validate_emails(self, emails, provider):

        tasks = [

            self.email_validator.validate(email)

            for email in emails
        ]

        results = await asyncio.gather(*tasks)

        return [

            Email(
                value=result["value"],
                trust_score=result["trust_score"],
                provider=provider,
                is_valid=result["is_valid"]
            )

            for result in results
        ]


    async def validate_phones(self, phones, provider):

        tasks = [

            self.phone_validator.validate(phone)

            for phone in phones
        ]

        results = await asyncio.gather(*tasks)

        return [

            Phone(
                value=result["value"],
                trust_score=result["trust_score"],
                provider=provider,
                is_valid=result["is_valid"]
            )

            for result in results
        ]
