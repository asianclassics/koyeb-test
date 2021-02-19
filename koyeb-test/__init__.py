def handler(event, context):
    print("Got YO data", event)
    print("Got YO context", context)
    print("Got YO context event", context.event)
    return {"response": "ok"}