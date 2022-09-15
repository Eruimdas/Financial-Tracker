""" ORM operations with peewee for financial db.
"""

from peewee import *
from datetime import datetime

db = SqliteDatabase("financial.db")
db.connect()


class BaseModel(Model):
    name = CharField()
    description = CharField()
    currency = CharField()
    amount = FloatField()
    date = DateTimeField(default=datetime.now)

    class Meta:
        database = db


class Income(BaseModel):
    class Meta:
        database = db


class Saving(BaseModel):
    """Savings model."""

    class Meta:
        database = db


class Expense(BaseModel):
    """Expense model."""

    category = CharField()
    payment_method = CharField()

    class Meta:
        database = db


db.create_tables([Income, Saving, Expense])
