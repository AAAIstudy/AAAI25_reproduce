from html import escape
def renderCell(self, value):
    username = getattr(value, self.field, '')
    if username and username != EMPTY_STRING:
        member = api.user.get(username)
        return '<a href="%s">%s</a>' % (member.url, escape(member.name))