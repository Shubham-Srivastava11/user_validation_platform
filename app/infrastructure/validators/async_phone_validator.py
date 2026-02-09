from app.infrastructure.external.async_phone_validation_client import AsyncPhoneValidationClient


class AsyncPhoneValidator:

    def __init__(self):

        self.client = AsyncPhoneValidationClient()

    async def validate(self, phone):

        result = await self.client.validate(phone)

        return {

            "value": phone,

            "trust_score": result["trust-score"],

            "is_valid": True
        }
