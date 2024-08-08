def is_palindrome(s: str) -> bool:
    new_s = ""
    for char in s:
        if char.isalnum():
            new_s += char.lower()

    s = new_s
    # зріз рядка s[::-1], що дозволяє нам отримати рядок у зворотному порядку, і просто порівняти його з оригінальним рядком.
    return s == s[::-1]


# Використання функції
print(is_palindrome("Козак з казок"))  # True
