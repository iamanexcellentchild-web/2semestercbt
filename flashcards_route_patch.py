# ── FLASHCARDS ──────────────────────────────────────────────────────────────
# Place this anywhere near the top of app.py (after the QUESTIONS dict) to load
# the flashcard data once at startup.

import os as _os, json as _json

def _load_flashcards():
    path = _os.path.join(_os.path.dirname(__file__), 'flashcards.json')
    if not _os.path.exists(path):
        return {}
    with open(path, 'r', encoding='utf-8') as f:
        return _json.load(f)

FLASHCARDS = _load_flashcards()


# ── REPLACE your existing /flashcards route with this ───────────────────────

@app.route('/flashcards')
def flashcards():
    return render_template('flashcards.html', flashcards=FLASHCARDS)
