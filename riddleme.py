from logic import ArgumentForm, vars


# Suspects
(
    low_level_criminal,
    joker,
    penguin,
    riddler,
) = vars("low_level_criminal", "joker", "penguin", "riddler")

# Evidence
(
    large_crime,
    small_crime,
    hole,
    acid_burn,
    playing_cards,
    joy_buzzer,
    umbrella_mark,
    riddle,
    puzzle,
    word_game,
) = vars(
    "large_crime",
    "small_crime",
    "hole",
    "acid_burn",
    "playing_cards",
    "joy_buzzer",
    "umbrella_mark",
    "riddle",
    "puzzle",
    "word_game",
)


# What Batman knows
knowledge_base = (
    large_crime,
    low_level_criminal >> small_crime,
    small_crime >> ~large_crime,
    joker >> (acid_burn | playing_cards | joy_buzzer),
    acid_burn >> joker,
    playing_cards >> joker,
    joy_buzzer >> joker,
    penguin >> umbrella_mark,
    umbrella_mark >> penguin,
    riddler >> (riddle | puzzle | word_game),
    riddle >> riddler,
    puzzle >> riddler,
    word_game >> riddler,
    hole,
    hole >> (umbrella_mark | acid_burn),
)


suspects = (
    ("A low-level criminal", low_level_criminal),
    ("The Joker", joker),
    ("The Penguin", penguin),
    ("The Riddler", riddler),
)

# Joker | Penguin -> large_crime (Joker or penguin did it)
print("Who definitely committed this crime:")
for label, suspect in suspects:
    argument = ArgumentForm(*knowledge_base, conclusion=suspect)
    print(f"{label}: {argument.is_valid()}")
