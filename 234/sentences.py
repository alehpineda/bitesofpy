import re


def capitalize_sentences(text: str) -> str:
    """Return text capitalizing the sentences. Note that sentences can end
       in dot (.), question mark (?) and exclamation mark (!)"""
    sentences = re.split('([.!?] *)', text)
    return ''.join((sentence.capitalize() for sentence in sentences))
