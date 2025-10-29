from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://postgres:yourpassword@localhost:5432/mse_db"

#engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
# ✅ Correct for PostgreSQL
engine = create_engine("postgresql+psycopg2://username:password@localhost:5432/dbname")
engine = create_engine(DATABASE_URL)  