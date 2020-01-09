class DevConfig():
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    debug = True

    SQLALCHEMY_DATABASE_URI={
        "username": "xxxxxxx",
        "engine": "postgres",
        "host": "database-1.xxxxxxxxxxxxxx.us-easqdt-1.rds.amazonaws.com",
        "password": "xxxxxxxxxxxxxxxxx",
        "port": 5432,
        "database":"db2sdwwed"
    }
