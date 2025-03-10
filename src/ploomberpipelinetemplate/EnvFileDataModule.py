class EnvFileData:
    def __init__(
        env_thing_1: str = "mything",
        env_thing_2: int = 5,
    ):
        ENV_THING_1 = env_thing_1
        ENV_THING_2 = env_thing_2
        MY_FOLDER = f"{ENV_THING_1}_{ENV_THING_2}"
