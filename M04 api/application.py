from flask import flask
app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://data.bd'
db = SQLAlchemy(app)

class book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(80), unique=True, nullable=False)
    author = db.Column(db.String(80))
    publisher = db.Column(db.String(80))

    def __repr__(self):
        return f"{self.book_name} - {self.author}"

@app.route('/book'):
def get_book():
    books = book.query.all()

    output = []
    for book in books:
        book_data = {'book_name': book.name, 'author': book.author,
        'publisher': book.publisher}

        output.append(book_data)
    
    return {'books': books}
    