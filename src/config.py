from configparser import ConfigParser

class Config(ConfigParser):

    def __init__(self):
        super().__init__()
        self.__config_file = 'assets/config.ini'
        if not len(self.read(self.__config_file)):
            self.add_section('paths')
            self.set('paths', 'db', 'assets/database.db')
            self.__save()

    def __save(self):
        with open(self.__config_file, 'w') as f:
            self.write(f)

    def get_db_path(self):
        return self.get('paths', 'db')

    def get_excel_path(self):
        return self.get('paths', 'excel') if self.has_option('paths', 'excel') else False

    def set_excel_path(self, path):
        if path:
            self.set('paths', 'excel', path)
            self.__save()
