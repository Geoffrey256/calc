def parse_complex_input(value: str) -> complex:
    try:
        return complex(value.replace(" ", "").replace("i", "j"))
    except:
        return complex(0)
