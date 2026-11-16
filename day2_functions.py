def two_sum(nums: list[int], target: int) -> list[int]:
    seen: dict[int, int] = {}
    for i, x in enumerate(nums):
        need = target - x
        if need in seen:
            return [seen[need], i]
        seen[x] = i
    return []

def add_all(*numbers: int) -> int:
    return sum(numbers)

def make_greeting(name: str, greeting: str = "Hi") -> str:
    return f"{greeting}, {name}!"

def describe_user(name: str, **details: str) -> str:
    parts = ", ".join(f"{k}={v}" for k, v in details.items())
    return f"{name} ({parts})" if parts else name

def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    counts: dict[str, int] = {}
    for ch in s:
        counts[ch] = counts.get(ch, 0) + 1
    for ch in t:
        if counts.get(ch, 0) == 0:
            return False
        counts[ch] -= 1
    return True

print(two_sum([2, 7, 11, 15], 9))
print(add_all(1, 2, 3, 4))
print(add_all())
print(make_greeting("Hitesh"))
print(make_greeting("Hitesh", greeting="Hello"))
print(describe_user("Hitesh", role="Backend Developer", city="Toronto"))
print(is_anagram("listen", "silent"))
print(is_anagram("rat", "car"))
print(is_anagram("aab", "aba"))