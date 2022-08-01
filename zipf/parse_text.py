import string
import collections
import sys

# add to this list as we find examples of project gutenberg books
# that have other start fence text
possible_start_fences = ["start of the project gutenberg ebook",
                         "start of this project gutenberg ebook"]
possible_end_fences = ["end of the project gutenberg ebook",
                       "finis iliadis",
                       "end of the iliad",
                       "finis odysseæ",
                       "όπως αυτός ήταν καλός 'ς τα έργα και 'ς στου"]

def count_words(o, clean_text=False):
    """
    Count words in a file.

    Arguments:
        o: an open file handle
        clean_text: states if true or false. If true, filters out boilerplate code typical of a Gutenberg library book.

    Returns:
        A dict keyed by word, with word counts
    """
    text = o.read()
    if clean_text:
        text = _yee_haw(text)

    chunks = text.split()
    npunc = [word.strip(string.punctuation) for word in chunks]
    word_list = [word.lower() for word in npunc if word]
    word_counts = collections.Counter(word_list)
    return dict(word_counts)

def _yee_haw(text):
    """
    Find fences in a Gutenberg text and select the text between them.
    """
    # start_fence = "start of the project gutenberg ebook"
    # end_fence = "end of the project gutenberg ebook"
    text = text.lower()
    # start_pos = text.find(start_fence) + len(start_fence) + 1
    start_pos = find_fence_pos(text, possible_start_fences)
    end_pos = find_fence_pos(text, possible_end_fences)

    # Always check that the fences are at reasonable positions within the text.
    print(start_pos, len(text), end_pos)
    assert 0.000001 < start_pos / len(text) <= 0.1
    assert 0.9 < end_pos / len(text) <= 1.0

    return text[start_pos:end_pos]

def find_fence_pos(text, possible_fences):
    """Applies some heuristics to find the start of the project gutenberg text."""
    for fence in possible_fences:
        pos = text.find(fence)
        # print(type(text), start_fence, pos)
        # print(text[:550])
        if pos != -1:
            return pos + len(fence) + 1
    print("**error** could not find fence position; please update the code")
    print("          to include the fence from this book")
    print(f"         fence strings was *{possible_fences}*")
    sys.exit(1)
