from browser import Browser

def before_all(context):
    context.browser = Browser()


def alter_all(context):
    context.browser.close()