from utils.general import load_configuration


# URLs
BASE_URL = load_configuration()['urls']['wiki_url']
PRICEAPI_URL = load_configuration()['urls']['priceapi_url']
GRAPHAPI_URL = load_configuration()['urls']['graphapi_url']

# HEADERS
HEADERS = load_configuration()['headers']

# COMMON THUMBNAILS
BUCKET_ICO = 'https://oldschool.runescape.wiki/images/thumb/Weird_gloop_detail.png/75px-Weird_gloop_detail.png?94769'
COLOUR_ICO = 'https://oldschool.runescape.wiki//images/thumb/Propeller_hat_detail.png/140px-Propeller_hat_detail.png?d1139'
QUEST_ICO = 'https://oldschool.runescape.wiki/images/thumb/Quests.png/130px-Quests.png?f5120'
MINIGAME_ICO = 'https://oldschool.runescape.wiki/images/thumb/Minigames.png/120px-Minigames.png?d639f'