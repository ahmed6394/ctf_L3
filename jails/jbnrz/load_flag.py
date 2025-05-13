class secert_flag(str):
    def __repr__(self) -> str:
        return "DELETED"
    def __str__(self) -> str:
        return "DELETED"
class flag_level5:
    def __init__(self, flag: str):
        setattr(self, 'flag_level5', secert_flag(flag))
def get_flag():
    with open('flag') as f:
        return flag_level5(f.read())