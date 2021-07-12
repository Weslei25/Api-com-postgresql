class Config:
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:(adm8081)@192.168.0.170/source-api"
    SECRET_KEY = b'\xed\xf4\x83\xac\x92\x948\x10\xed\x04r\x94\x90\x058\xec\xf5\x84\x8bV\xfe\xceb\xea'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class Development(Config):
    Debug=True


class Testing(Config):
    pass

config = {
    "development": Development,
    "testing": Testing

}