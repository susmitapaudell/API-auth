from app.database.session import Base, engine
from app.models import user  # imports all models

Base.metadata.create_all(bind=engine)
print("Tables created successfully!")
