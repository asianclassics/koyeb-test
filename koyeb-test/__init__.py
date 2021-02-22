def handler(event, context):
    print("Got YOYO data", event)
    print("Got YO context", context)
    print("Got YO context event", context.event)
    print("MEOW")
    return {"response": "ok"}
