import asyncio
from app.domain.entities.user import User
from app.core.logger import logger


class AsyncUserPipelineService:

    def __init__(self, providers, validation_service, repository):

        self.providers = providers
        self.validation_service = validation_service
        self.repository = repository


    async def run(self, linkedin):

        logger.info("async_pipeline_started", linkedin=linkedin)

        users = []

        for provider in self.providers:

            raw = provider.fetch_user(linkedin)

            if not raw:
                continue

            emails = await self.validation_service.validate_emails(
                raw["emails"],
                provider.get_name()
            )

            phones = await self.validation_service.validate_phones(
                raw["phones"],
                provider.get_name()
            )

            user = User(
                linkedin=raw["linkedin"],
                name=raw["name"],
                emails=emails,
                phones=phones
            )

            users.append(user)

        if not users:
            return

        final_user = users[0]

        self.repository.save(final_user)

        logger.info("async_pipeline_completed")

        return final_user
