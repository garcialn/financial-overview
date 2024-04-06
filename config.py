from dynaconf import Dynaconf

"""
    Dynaconf settings: the Dynaconf instance (settings) will be used in other files
    in order to be able to make references to the correct enviroments, their
    settings and validation
"""

settings = Dynaconf(
    envvar_prefix="DYNACONF",
    enviroment=True,
    settings_files=[
        "./config/settings.toml",
        "./config/.secrets.toml",
        "./config/validators.toml",
        "./config/data_setings.toml",
    ],
)

# `envvar_prefix` = export envvars with `export DYNACONF_FOO=bar`.
# `settings_files` = Load these files in the order.
