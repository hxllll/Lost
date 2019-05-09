import uuid

ADMIN = "admin"
RESCUE = "rescue"
USER = "user"


def generate_token(prefix):
    token = uuid.uuid4().hex

    return prefix + token


def generate_admin_token():
    return generate_token(ADMIN)


def generate_rescue_token():
    return generate_token(RESCUE)


def generate_user_token():
    return generate_token(USER)
