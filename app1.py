from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///C:\\Users\\91983\\OneDrive\\Desktop\\New folder\\todo.db"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)


class TODO(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

# app.app_context().push()

def __repr__(self) -> str:
        return f"{self.sno}-{self.title}"




@app.route('/')
def index():
    todo= TODO(title="First Todo",desc="Start investing in Stock Market")
    db.session.add(todo)
    db.session.commit()
    return render_template('index.html')


@app.route('/products')
def hello_world():
    return 'Chalo abh thoda samman hi bech lete hai'


if __name__ == '__main__':
    app.run(debug=True)

