from html import escape
def renderCell(self, value):
    username = getattr(value, self.field, '')
    if username and username != EMPTY_STRING:
        member = api.user.get(username)
        # co_fixed
        if member:
            return escape(member.name)
          # co_fixed