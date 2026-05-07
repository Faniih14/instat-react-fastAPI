from sqlalchemy import Integer,String,Date,Column
from db.database import Base

class Test(Base):
    __tablename__="test"

    id = Column(Integer,primary_key=True,index=True)
    titre = Column(String (50))
    description =  Column(String(500))
    etat =  Column(String(50))
    dateEch = Column(Date)
    dateCre = Column(Date)
    dateMaj = Column(Date)