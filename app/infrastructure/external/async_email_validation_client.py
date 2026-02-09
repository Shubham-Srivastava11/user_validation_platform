import httpx
import random
from app.core.logger import logger


class AsyncEmailValidationClient:

    async def validate(self, email: str):

        logger.info("async_email_validation_started", email=email)

        await httpx.AsyncClient().get(
            "https://example.com",
            timeout=1.0
        )

        result = {
            "trust-score": random.randint(50, 100),
            "bounce-status": False,
            "category": "business"
        }

        logger.info(
            "async_email_validation_completed",
            email=email,
            trust_score=result["trust-score"]
        )

        return result
