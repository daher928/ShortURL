# Possible ASCII values for building shortURL
ASCII_CHARS = '0123456789abcdefghijklmnopqrstuvwxyz!#$%&()*+,-./:;<=>?@[^_`{|}~"'


class URLSuffix:
    def __init__(self, suffix):
        self.suffix = suffix

    def len(self):
        return len(self.suffix)

    def get_char_at(self, index):
        return self.suffix[index]

    def get_suffix(self):
        return self.suffix


# TODO add validations
class ShortUrlGenerator:
    def __init__(self, prefix="http://shortUrl.com"):
        self.prefix = prefix
        self.curr_shortest_len = 0
        self.curr_shortest_suffix = None  # first url to ever be used in system

    """
    Get current shortest URL
    """

    def current_shortest_url(self):
        return "{}/{}".format(self.prefix, self.curr_shortest_suffix.get_suffix())

    """
    Logic that generates the next ascii-lexicographical string of same length (or next length)
    """

    def generate_next_shortest_url(self):
        next_short_suffix = None

        if self.curr_shortest_len == 0:  # first ever url
            self.curr_shortest_len = 1
            next_short_suffix = URLSuffix(ASCII_CHARS[0])  # first url to ever be used in system: '0'

        elif all(self.curr_shortest_suffix.get_char_at(i) == ASCII_CHARS[-1] for i in
                 range(self.curr_shortest_suffix.len())):
            self.curr_shortest_len += 1
            next_short_suffix = URLSuffix("".join(ASCII_CHARS[0] * self.curr_shortest_len))
            
        else:
            for i in reversed(range(self.curr_shortest_suffix.len())):
                if self.curr_shortest_suffix.get_char_at(i) != ASCII_CHARS[-1]:
                    index_of_ascii_char = ASCII_CHARS.index(self.curr_shortest_suffix.get_char_at(i))
                    suffix = self.curr_shortest_suffix.suffix[0:i]
                    suffix += ASCII_CHARS[index_of_ascii_char + 1]
                    suffix += ASCII_CHARS[0] * (self.curr_shortest_len - i - 1)
                    next_short_suffix = URLSuffix(suffix)
                    break

        self.curr_shortest_suffix = next_short_suffix
        return self.current_shortest_url()
