from scrapy.loader import ItemLoader
from scrapy.loader.processors import Identity, TakeFirst, MapCompose, Join, Compose


def remove_last_word(str):
    ' '.join(str.split()[0:-1])

def remove_word_advisor(str):
    if not str:
        return ""

    split = [word for word in str.split() if word != "Advisor(s):" and word != "Academic"]
    return ' '.join(split)

def exclude_invalid_strings(str):
    return None if "scholar.princeton.edu" in str else str

def en_office(office):
    if office is not None and len(office.strip()) > 0:
        return office.strip()
    else:
        return None

class ElePersonLoader(ItemLoader):
    default_output_processor = Join(", ")

    advisor_in = MapCompose(remove_word_advisor)
    advisor_out = Compose(lambda v: [x for x in v if len(x) > 0], Join(", "))

class EnglishPersonLoader(ItemLoader):
    default_output_processor = TakeFirst()

    office_address_in = MapCompose(en_office)
    bio_out = Join('\n')

class EconPersonLoader(ItemLoader):

    default_output_processor = TakeFirst()

    fullname_in = MapCompose(remove_last_word)
    fullname_out = Identity()

    email_in = MapCompose(exclude_invalid_strings)
    email_out = Join()
