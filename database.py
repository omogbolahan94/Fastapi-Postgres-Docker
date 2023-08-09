import sqlalchemy as _sql
import sqlalchemy.ext.declarative as _declarative
import sqlalchemy.orm as _orm


# create url for the database.py we created in a docker container with configuration setup
DATABASE_URL = "postgresql://dataholic:mypass@localhost/fastapi_db"

# connect to the database.py
engine = _sql.create_engine(DATABASE_URL)

# create a session to enable interaction with database.py
SessionLocal = _orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)

# initialize SQLAlchemy database built in model
Base = _declarative.declarative_base()

