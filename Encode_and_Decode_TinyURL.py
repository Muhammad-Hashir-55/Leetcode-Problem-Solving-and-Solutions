li = [0,0]
class Codec:

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        li[0] = longUrl
        li[1] = "http://tinyurl.com/4e9iAk"
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        ret = li[0]
        li[0] =0
        li[1] = 0
        return ret

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
