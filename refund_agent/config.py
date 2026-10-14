from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()

MODEL = "claude-sonnet-4-6"
MAX_TOKENS = 1000

client = Anthropic()
