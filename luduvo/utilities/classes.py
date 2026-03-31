class User:
    def __init__(self, client, data):
        self.id = data.get("user_id")
        self.username = data.get("username")
        self.display_name = data.get("display_name", None)
        self.created_at = data.get("created_at")
        self.member_since = data.get("member_since")
        self.status = data.get("status", None)
        self.bio = data.get("bio", None)
