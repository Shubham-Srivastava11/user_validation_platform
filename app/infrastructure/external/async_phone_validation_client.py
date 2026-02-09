import httpx
import random
from app.core.logger import logger


class AsyncPhoneValidationClient:

    async def validate(self, phone: str):

        logger.info("async_phone_validation_started", phone=phone)

        await httpx.AsyncClient().get(
            "https://example.com",
            timeout=1.0
        )

        result = {
            "trust-score": random.randint(50, 100),
            "service-provider": "Airtel",
            "privacy-enabled": False
        }

        logger.info(
            "async_phone_validation_completed",
            phone=phone,
            trust_score=result["trust-score"]
        )

        return result
