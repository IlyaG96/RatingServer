from dynaconf import Dynaconf

settings = Dynaconf(
    settings_files=["config/settings.toml"],
    environments=True,
    merge_enabled=True,
    uppercase_mode=True,
)
