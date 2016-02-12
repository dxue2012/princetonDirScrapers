from scrapy.loader import ItemLoader
from scrapy.loader.processors import Identity, TakeFirst, MapCompose, Join


def remove_last_word(str):
    ' '.join(str.split()[0:-1])

def exclude_invalid_strings(str):
    return None if "scholar.princeton.edu" in str else str

class EconPersonLoader(ItemLoader):

    default_output_processor = TakeFirst()

    fullname_in = MapCompose(remove_last_word)
    fullname_out = Identity()

    email_in = MapCompose(exclude_invalid_strings)
    email_out = Join()
