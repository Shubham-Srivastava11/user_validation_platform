from app.infrastructure.external.async_email_validation_client import AsyncEmailValidationClient


class AsyncEmailValidator:

    def __init__(self):

        self.client = AsyncEmailValidationClient()

    async def validate(self, email):

        result = await self.client.validate(email)

        return {

            "value": email,

            "trust_score": result["trust-score"],

            "is_valid": not result["bounce-status"]
        }
