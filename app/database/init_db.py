from app.database.session import Base, engine
from app.models import user  # imports all models
from app.models import refresh_token

Base.metadata.create_all(bind=engine)
print("Tables created successfully!")
