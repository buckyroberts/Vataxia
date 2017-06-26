ENVIRONMENT = 'local'
# ENVIRONMENT = 'production'

SETTINGS_MODULE = 'config.settings.local'

if ENVIRONMENT == 'local':
    SETTINGS_MODULE = 'config.settings.local'
if ENVIRONMENT == 'production':
    SETTINGS_MODULE = 'config.settings.production'
