"""
Central color palette for the application theme.

These values are the source of truth for every hex color used by the
QSS blocks in :mod:`app.styles.theme`. Keep hex values in the QSS and
this table in sync when tweaking the visual style.
"""


COLORS = {
    # -- surfaces ----------------------------------------------------------
    "background": "#0F1115",          # app window background
    "panel": "#151922",               # main cards / frames
    "panel_inner": "#10141C",         # nested panels, charts
    "panel_hover": "#192131",         # hover surface
    "panel_active": "#17243A",        # selected surface
    "input": "#1B2230",               # buttons / inputs
    "input_hover": "#273147",         # buttons / inputs (hover)
    "input_pressed": "#151B27",       # buttons / inputs (pressed)
    "border": "#242938",              # neutral borders
    "border_strong": "#30384A",       # stronger borders
    "border_accent": "#4F8CFF",       # accent borders (hover/selected)
    # -- text --------------------------------------------------------------
    "text_primary": "#F9FAFB",
    "text_secondary": "#98A2B3",
    "text_muted": "#8F98A8",
    "text_dim": "#7F8898",
    "text_accent": "#7EA6FF",
    "text_link": "#DCE6FF",
    # -- accents -----------------------------------------------------------
    "accent": "#4F8CFF",
    "accent_hover": "#669BFF",
    "accent_pressed": "#3C78E8",
    "accent_soft": "#1D2940",         # soft accent background
    # -- status ------------------------------------------------------------
    "success": "#34D399",
    "success_bg": "#10251D",
    "success_border": "#1F9D68",
    "warning": "#F59E0B",
    "error": "#F87171",
    "error_bg": "#25151A",
    "error_border": "#7F1D1D",
    "danger_text": "#FCA5A5",
    "danger_bg": "#2B1820",
    # -- gradients ---------------------------------------------------------
    "gradient_start": "#5B8CFF",
    "gradient_end": "#7A5CFF",
}