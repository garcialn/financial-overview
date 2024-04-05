from dynaconf import Dynaconf, Validator

settings = Dynaconf(
    envvar_prefix="DYNACONF",
    enviroment=True,
    settings_files=[
        "./config/base/settings.toml",
        "./config/local/.secrets.toml",
        "./config/base/model/",
        "./config/base/process/",
    ],
)

# `envvar_prefix` = export envvars with `export DYNACONF_FOO=bar`.
# `settings_files` = Load these files in the order.
