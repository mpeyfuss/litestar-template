from piccolo.apps.user.tables import BaseUser
from piccolo.columns import Boolean, Timestamptz


class ApiUser(BaseUser, tablename="api_user"):
    admin = Boolean(
        default=False,
        help_text="Should always be false. Doesn't affect logging into admin, just an artifact from inheriting BaseUser",
    )
    active = Boolean(default=True)  # default true
    created_at = Timestamptz(auto_now_add=True)
    created_at = Timestamptz(auto_now=True)

    class Meta:
        admin = True
