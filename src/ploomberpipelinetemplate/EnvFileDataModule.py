class EnvFileData:
    def __init__(
        self,
        env_thing_1: str = "mything",
        env_thing_2: int = 5,
    ):
        self.ENV_THING_1 = env_thing_1
        self.ENV_THING_2 = env_thing_2
        self.MY_FOLDER = f"{self.ENV_THING_1}_{self.ENV_THING_2}_folder"
