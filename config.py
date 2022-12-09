import os

class Config(object):

      BOT_TOKEN = os.environ.get("BOT_TOKEN", "5740014121:AAHsZxv5L_PkggpEUPNSJrde0MEFCrU3OeY")
      API_ID = int(os.environ.get("API_ID", ))
      API_HASH = os.environ.get("API_HASH", "")
      OWNER_ID = int(os.environ.get("OWNER_ID", 5143506371))

