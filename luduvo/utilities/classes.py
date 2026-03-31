import datetime


class User:
    """Represents a Luduvo user."""

    def __init__(self, client, data):
        self.id: int = data.get("user_id")
        self.username: str = data.get("username")
        self.member_since: datetime.datetime = datetime.datetime.fromtimestamp(
            data.get("member_since")
        )
        self.networth = data.get("networth")
        self.display_name: str = data.get("display_name")
        self.created_at: str = data.get("created_at")
        self.status: str = data.get("status")
        self.bio: str = data.get("bio")
        self.avatar: dict = data.get("avatar")
        self.equipped_items: list = data.get("equipped_items")
        self.badges: list = data.get("badges")
        self.friend_count: int = data.get("friend_count")
        self.place_count: int = data.get("place_count")
        self.item_count: int = data.get("item_count")
        self.last_active = data.get("last_active")
        self.allow_joins: bool = data.get("allow_joins")
