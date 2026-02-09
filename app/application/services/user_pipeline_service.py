from app.domain.entities.user import User
from app.core.logger import logger


class UserPipelineService:

    def __init__(self, providers, validation_service, repository):

        self.providers = providers
        self.validation_service = validation_service
        self.repository = repository

    def run(self, linkedin):

        logger.info("pipeline_started", linkedin=linkedin)

        users = []

        for provider in self.providers:

            logger.info(
                "provider_processing_started",
                provider=provider.get_name()
            )

            raw = provider.fetch_user(linkedin)

            if not raw:

                logger.warning(
                    "provider_no_data",
                    provider=provider.get_name()
                )

                continue

            emails = self.validation_service.validate_emails(
                raw["emails"],
                provider.get_name()
            )

            phones = self.validation_service.validate_phones(
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

            logger.info(
                "provider_processing_completed",
                provider=provider.get_name()
            )

        if not users:

            logger.error("pipeline_no_user_found")

            return

        final_user = users[0]

        logger.info(
            "best_email_selected",
            email=final_user.best_email().value,
            trust=final_user.best_email().trust_score
        )

        logger.info(
            "best_phone_selected",
            phone=final_user.best_phone().value,
            trust=final_user.best_phone().trust_score
        )

        self.repository.save(final_user)

        logger.info("pipeline_completed", linkedin=linkedin)

        return final_user
