from Cocoa import NSWorkspace
def get_active_app():
    return NSWorkspace.sharedWorkspace().activeApplication()

def stardew_focused():
    app = get_active_app()
    return app.get("NSApplicationBundleIdentifier",None) == "com.concernedape.stardewvalley"