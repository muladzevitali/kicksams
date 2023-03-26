import environ

env = environ.Env(
    ENV_PATH=(str, None),
    DJANGO_DEBUG=(bool, False),
    DJANGO_SECRET_KEY=(str, ''),
    DJANGO_ALLOWED_HOSTS=(list, []),
)
if env('ENV_PATH'):
    environ.Env.read_env(env('ENV_PATH'))
