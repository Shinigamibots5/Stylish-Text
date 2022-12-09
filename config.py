import os

class Config(object):

      BOT_TOKEN = os.environ.get("BOT_TOKEN", "5740014121:AAHsZxv5L_PkggpEUPNSJrde0MEFCrU3OeY")
      API_ID = int(os.environ.get("API_ID", 8942928))
      API_HASH = os.environ.get("API_HASH", "8edc5a0d1939f3a5de5dc44d021d52ca")
      OWNER_ID = int(os.environ.get("OWNER_ID", 5143506371))

