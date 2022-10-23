from app import create_app, db
from app.config import config_dict
from flask_migrate import Migrate


app_config = config_dict["Debug"]
app = create_app(app_config)
Migrate(app, db)

if __name__ == '__main__':
    app.run(debug=True)