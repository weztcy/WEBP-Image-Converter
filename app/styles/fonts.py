"""
Central font definitions.

The QSS blocks in :mod:`app.styles.theme` declare the same font families;
keep this module as the canonical reference.
"""


FONTS = {
    "family": ('"Inter", "Segoe UI"'),
    "weights": {
        "regular": 500,
        "semibold": 600,
        "bold": 700,
        "extrabold": 800,
        "black": 900,
    },
    "sizes": {
        "micro": 10,
        "small": 11,
        "caption": 12,
        "body": 13,
        "body_large": 14,
        "title": 16,
        "hero": 28,
    },
}