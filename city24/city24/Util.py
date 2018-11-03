import re

reggex_printable_chars = re.compile('^[ŠšŽžÕõÄäÖöÜüA-Za-z0-9/ .m²:,-]*$', flags=re.ASCII)
# reggex_printable_chars = re.compile('^[\W\dA-Za-z0-9/ .m²:,-]*$', flags=re.ASCII)


def has_printable_characters(line):
    global reggex_printable_chars
    if reggex_printable_chars.match(line):
        return True
    return False


print(has_printable_characters("MalmÕ"))