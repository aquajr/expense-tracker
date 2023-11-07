from app import app, db
from app.models import User, Income, Expense


#add database instance and models to a flask sehell session
@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Income=Income, Expense=Expense)
