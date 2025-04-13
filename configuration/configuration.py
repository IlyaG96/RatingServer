from dynaconf import Dynaconf

settings = Dynaconf(
    settings_files=["settings.toml"],
    environments=True,
    merge_enabled=True,
    uppercase_mode=True,
)
