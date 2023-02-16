import configparser

config = configparser.RawConfigParser()
config.read("C:/Users/VelKarthik/PycharmProjects/Playwright_YMS_2023/Configurations/config.ini")


class ReadConfig:
    #Create three static methods
    @staticmethod
    def getApplicationURL():
        url = config.get('common info -Login URL and Credentials', 'baseURL')
        return url

    @staticmethod
    def getUseremail():
        email = config.get('common info -Login URL and Credentials', 'emailaddress')
        return email

    @staticmethod
    def getPassword():
        password = config.get('common info -Login URL and Credentials', 'password')
        return password

