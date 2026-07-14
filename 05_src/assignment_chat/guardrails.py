# Words/phrases that are blocked before the message ever reaches the model.
BANNED_WORDS = [
    "cat", "cats", "kitten", "kitty",
    "dog", "dogs", "puppy", "puppies",
    "horoscope", "zodiac", "astrology",
    "aries", "taurus", "gemini", "cancer", "leo", "virgo", "libra",
    "scorpio", "sagittarius", "capricorn", "aquarius", "pisces",
    "taylor swift",
]
 
PROMPT_PROBE_WORDS = [
    "system prompt",
    "your instructions",
    "reveal your prompt",
    "ignore previous instructions",
]
 
REFUSAL_TOPIC = "I can't help with that topic, but I'd love to help you plan a trip instead!"
REFUSAL_PROMPT = "I can't share my instructions, sorry! Ask me about travel instead."
 
 
def check_message(user_text: str) -> str | None:
    """
    Returns a refusal string if the message should be blocked.
    Returns None if it's safe to send to the model.
    """
    text = user_text.lower()
 
    for word in BANNED_WORDS:
        if word in text:
            return REFUSAL_TOPIC
 
    for phrase in PROMPT_PROBE_WORDS:
        if phrase in text:
            return REFUSAL_PROMPT
 
    return None
 