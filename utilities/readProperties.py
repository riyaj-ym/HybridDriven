import configparser

config = configparser.RawConfigParser()
config.read("./Configurations/config.ini")


class ReadConfigs:

    @staticmethod
    def getUrl():
        baseurl = config.get(section='common-info', option='url')
        return baseurl

    @staticmethod
    def getUsername():
        username = config.get(section='common-info', option='username')
        return username

    @staticmethod
    def getPassword():
        password = config.get(section='common-info', option='password')
        return password


