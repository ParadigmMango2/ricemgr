import settings


class SmartPath:
    @staticmethod
    def to_smartpath(local_path):
        smartpath = local_path
        if local_path.startswith(settings.CONFIG_DIR):
            smartpath = local_path.replace(settings.CONFIG_DIR,
                                           settings.CONFIG_KEY)
        elif local_path.startswith(settings.DATA_DIR):
            smartpath = local_path.replace(settings.DATA_DIR,
                                           settings.DATA_KEY)
        elif local_path.startswith(settings.HOME_DIR):
            smartpath = local_path.replace(settings.HOME_DIR,
                                           settings.DATA_KEY)

        # print(smartpath)

        return smartpath

    @staticmethod
    def to_local_path(smartpath):
        local_path = smartpath
        if smartpath.startswith(settings.CONFIG_KEY):
            local_path = smartpath.replace(settings.CONFIG_KEY,
                                           settings.CONFIG_DIR)
        elif smartpath.startswith(settings.DATA_KEY):
            local_path = smartpath.replace(settings.DATA_KEY,
                                           settings.DATA_DIR)
        elif smartpath.startswith(settings.HOME_KEY):
            local_path = smartpath.replace(settings.HOME_KEY,
                                           settings.HOME_DIR)

        # print(local_path)

        return local_path
