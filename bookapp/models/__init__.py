import flask_bcrypt as _fb
import flask_migrate as _fm
import flask_sqlalchemy as _fs

db = _fs.SQLAlchemy()
migrate = _fm.Migrate(db=db)
bcrypt = _fb.Bcrypt()


def init_app(app, **kwargs):
    db.app = app
    migrate.init_app(app)
    db.init_app(app)


from .user import User, Role
from .book import Book
from .category import Category, category_book_table
