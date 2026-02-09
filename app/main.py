import typer

from app.application.services.async_user_pipeline_service import AsyncUserPipelineService
from app.application.services.async_validation_service import AsyncValidationService
from app.infrastructure.providers.csv_provider import CSVProvider
from app.infrastructure.validators.email_validator import EmailValidator
from app.infrastructure.validators.phone_validator import PhoneValidator
from app.infrastructure.repositories.mysql_user_repository import MySQLUserRepository

from app.application.services.validation_service import ValidationService
from app.application.services.user_pipeline_service import UserPipelineService

from app.core.database import Base, engine

app = typer.Typer()

def build_pipeline():

    provider = CSVProvider("data/users.csv")

    email_validator = EmailValidator()
    phone_validator = PhoneValidator()

    validation_service = ValidationService(
        email_validator, phone_validator
    )

    # validation_service = AsyncValidationService(
    #     email_validator,
    #     phone_validator
    # )

    repository = MySQLUserRepository()

    pipeline = UserPipelineService(
        providers=[provider],
        validation_service=validation_service,
        repository=repository
    )

    # pipeline = AsyncUserPipelineService(
    #     providers=[provider],
    #     validation_service=validation_service,
    #     repository=repository
    # )

    return pipeline

@app.command()
def run(linkedin: str):

    Base.metadata.create_all(engine)

    pipeline = build_pipeline()

    pipeline.run(linkedin)

if __name__ == "__main__":
    app()
