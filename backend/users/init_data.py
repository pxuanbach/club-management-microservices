import uuid
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.future import select

from config import settings
from auth import get_password_hash
from models import Users


engine = create_engine(
    settings.USERS_DATABASE_URL,
)
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)
session = SessionLocal()

result = session.execute(select(Users).where(Users.email == settings.ADMIN_USERNAME))
user = result.scalars().first()
if not user:
    db_obj = Users(
        username=settings.ADMIN_USERNAME,
        email=f"{settings.ADMIN_USERNAME}@gmail.com",
        full_name=settings.ADMIN_USERNAME,
        hashed_password=get_password_hash(settings.ADMIN_PASSWORD),
        is_active=True,
        is_superuser=True,
    )
    session.add(db_obj)
    session.commit()
    print("Create superuser success")
else:
    print("Superuser existed")