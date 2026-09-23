import re

def extract_video_id(url):
    """
    Extract video ID from different YouTube URL formats.
    """

    patterns = [
        r"(?:v=)([a-zA-Z0-9_-]{11})",                 # youtube.com/watch?v=
        r"(?:youtu\.be/)([a-zA-Z0-9_-]{11})",         # youtu.be/
        r"(?:shorts/)([a-zA-Z0-9_-]{11})",            # shorts
        r"(?:live/)([a-zA-Z0-9_-]{11})",              # live
        r"(?:embed/)([a-zA-Z0-9_-]{11})"              # embed
    ]

    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)

    return None