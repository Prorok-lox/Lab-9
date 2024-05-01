from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask('Best memories')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city_name = db.Column(db.String(300))
    date = db.Column(db.String(10))

    def __repr__(self):
        return f'City #{self.id}. {self.city_name} - {self.date}'


@app.route('/')
def main():
    cities = City.query.all()
    return render_template('index.html', cities_list=cities)


# @app.route('/in_stock/<city_id>', methods=['PATCH'])
# def modify_city(city_id):
#     city = City.query.get(city_id)
#     db.session.commit()


@app.route('/add', methods=['POST'])
def add_city():
    data = request.json
    city = City(**data)
    db.session.add(city)
    db.session.commit()
    return 'OK'


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
