import os



class Config(object):

    basedir = os.path.abspath(os.path.dirname(__file__))
    
    darksykey =  '6d578ce3886749328597bb9917f15076'
    googlekey = "AIzaSyCAVaRUWKRYQc96EU3RFGro_D8qq6WCRSY"

    # Set up the App SECRET_KEY
    # SECRET_KEY = config('SECRET_KEY'  , default='S#perS3crEt_007')
    SECRET_KEY = os.getenv('SECRET_KEY', 'S#perS3crEt_007')

    # This will create a file in <app> FOLDER
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'db.sqlite3')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True 
    
config_dict = {
'Debug'     : Config
}