import mongoengine as me


class TaskDocument(me.Document):
    cmd = me.StringField(required=True)
    output = me.StringField(default=None)
    status = me.StringField(default='not_started')
