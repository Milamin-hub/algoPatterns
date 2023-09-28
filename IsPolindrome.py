from testsAlg import test_IsPolindrome


@test_IsPolindrome() # test
def isPalindrome(x: int) -> bool:

    new = 0
    orig = x # original num

    if x < 0: 
        # negative number is not polindrome
        return False

    while x:
        x, d = divmod(x, 10)

        new = new * 10 + d # x == new

    return new == orig

isPalindrome(110)