from sqlalchemy import Column, Integer, String
from app.core.database import Base, SessionLocal
from app.domain.interfaces.repository import UserRepository as UserRepositoryInterface
from app.core.logger import logger


class UserModel(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    linkedin = Column(String(255))
    name = Column(String(255))
    email = Column(String(255))
    email_trust = Column(Integer)
    phone = Column(String(50))
    phone_trust = Column(Integer)


class MySQLUserRepository(UserRepositoryInterface):

    def save(self, user):

        logger.info("db_save_started", linkedin=user.linkedin)

        session = SessionLocal()

        best_email = user.best_email()
        best_phone = user.best_phone()

        model = UserModel(
            linkedin=user.linkedin,
            name=user.name,
            email=best_email.value if best_email else None,
            email_trust=best_email.trust_score if best_email else None,
            phone=best_phone.value if best_phone else None,
            phone_trust=best_phone.trust_score if best_phone else None
        )

        session.add(model)

        session.commit()

        session.close()

        logger.info("db_save_completed", linkedin=user.linkedin)
