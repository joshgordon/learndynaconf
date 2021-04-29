from dynaconf import Dynaconf, Validator

settings = Dynaconf(
    settings_files=[                      # Paths or globs to any toml|yaml|ini|json|py
        "configs/settings.toml",          # a file for main settings
    ],

    envvar_prefix="DYNACONF",             # variables exported as `DYNACONF_FOO=bar` becomes `settings.FOO == "bar"`
)
