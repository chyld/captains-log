test = "12345678abcdefgh"


def mask_card(card, char, amount):
    chars = len(card) - amount
    last = card[-amount:]
    final = (chars * char) + last
    return final


def mask_card_opt(card, char, amount):
    chars = len(card) - amount
    return (chars * char) + card[-amount:]


print(mask_card(test, '*', 4))
print(mask_card_opt(test, '^', 6))
