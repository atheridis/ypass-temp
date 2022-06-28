import hashlib

CHARACTER_SUBSETS = {
    "lowercase": "abcdefghijklmnopqrstuvwxyz",
    "uppercase": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "digits": "0123456789",
    "symbols": "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~",
}


class Pass():
    def __init__(self, name, site, master, length, counter, rules, exclude):
        self.name = name
        self.site = site
        self.master = master
        self.length = length
        self.counter = counter
        self.rules = rules
        self.exclude = exclude
        self.extrasalt = 0

        pool_of_chars = ""
        for rule in rules:
            pool_of_chars += CHARACTER_SUBSETS[rule]

        chars = "".join(c for c in pool_of_chars if c not in exclude)

        self.password = ""
        self.password = self.generate_password(
            chars, length - len(rules), "sha256"
        )

        one_char_per_rule = ""
        for rule in rules:
            av_chars = "".join(
                c for c in CHARACTER_SUBSETS[rule] if c not in exclude
            )
            value = self.generate_password(av_chars, 1, "sha256")
            one_char_per_rule += value

        for char in one_char_per_rule:
            entropy = self.create_entropy("sha256")
            choice = entropy % len(self.password)
            self.password = (
                self.password[:choice] +
                char +
                self.password[choice:]
            )

    def create_entropy(self, hashf):
        self.extrasalt += 1
        self.salt = (
            hex(self.extrasalt)[2:] +
            self.site +
            self.name +
            hex(self.counter)[2:]
        )

        entropy = hashlib.pbkdf2_hmac(
            hashf,
            self.master.encode("utf-8"),
            self.salt.encode("utf-8"),
            100_000 // (self.length + len(self.rules))
        ).hex()

        return int(entropy, 16)

    def generate_password(self, chars, max_length, hashf):
        generated_password = ""
        while(len(generated_password) < max_length):
            entropy = self.create_entropy(hashf)
            choice = entropy % len(chars)
            generated_password += chars[choice]

        return generated_password
