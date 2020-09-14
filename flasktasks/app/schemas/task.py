from marshmallow import fields, Schema, validate


class TaskListSchema(Schema):
    id = fields.UUID(dump_only=True)
    cmd = fields.String(required=True, validate=validate.Length(min=1), load_only=True)


class TaskInstanceSchema(Schema):
    output = fields.String(dump_only=True)
