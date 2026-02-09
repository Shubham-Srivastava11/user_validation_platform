import csv
from app.domain.interfaces.data_provider import DataProvider
from app.core.logger import logger


class CSVProvider(DataProvider):

    def __init__(self, filepath):
        self.filepath = filepath

    def get_name(self):
        return "csv_provider"

    def fetch_user(self, linkedin):

        logger.info(
            "provider_fetch_started",
            provider=self.get_name(),
            linkedin=linkedin
        )

        with open(self.filepath, newline="") as csvfile:

            reader = csv.DictReader(csvfile)

            for row in reader:

                if row["linkedin"] == linkedin:

                    logger.info(
                        "provider_user_found",
                        provider=self.get_name(),
                        linkedin=linkedin
                    )

                    return {
                        "name": row["name"],
                        "emails": row["emails"].split(";"),
                        "phones": row["phones"].split(";"),
                        "linkedin": row["linkedin"]
                    }

        logger.warning(
            "provider_user_not_found",
            provider=self.get_name(),
            linkedin=linkedin
        )

        return None
