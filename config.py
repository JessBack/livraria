class Config:
    USER = "root"
    PASSWORD = ""
    HOST = "localhost"
    DATABASE = "library"
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}/{DATABASE}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False  
    SECRET_KEY = "minha_chave_1234"  # Corrigido o nome para SECRET_KEY