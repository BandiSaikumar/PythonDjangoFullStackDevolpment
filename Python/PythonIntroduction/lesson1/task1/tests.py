from test_helper import run_common_tests, failed, passed, get_answer_placeholders

def test_ASCII():
    windows =get_answer_placeholders()
    for window in windows:
        all_ascii = all(ord(c) < 128 for c in window)
        if not all_ascii:
            failed("Please use english characters this time:")
            return
    passed()

def test_is_alpha():
    window = get_answer_placeholders()[0]
    splited = window.split()
    for s in splited:
        if not s.isalpha():
            failed("Please use  english characters this time.")
            return

    passed()


if __name__ == "__main__":
    test_ASCII()
    run_common_tests("You should enter your name")
    test_is_alpha()


