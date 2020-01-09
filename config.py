class DevConfig():
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    debug = True

    SQLALCHEMY_DATABASE_URI={
        "username": "karthik",
        "engine": "postgres",
        "host": "database-1.cgeh7ghqkigm.us-east-1.rds.amazonaws.com",
        "password": "!|ct2*{pwRR$tT3=t;0+)~F8~7,mCXR+",
        "port": 5432,
        "database":"db2"
    }