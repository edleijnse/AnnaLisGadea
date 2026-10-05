# AnnaLis Gadea – HTML Documentation Generator

This project generates a complete, searchable, offline HTML documentation of the **AnnaLis Gadea** art portfolio (originally hosted at `https://paparazzi.li/annalis-gadea/`).

Output directory: `D:\Annalis_Gadea\html`

---

### Features

1. **Complete Offline HTML Documentation**:
   - Comprehensive documentation spanning all 19 art series and the overview biography.
   - Total of 574 catalogued artworks and drawings across five decades (1968–2023).
   - Fully self-contained in `D:\Annalis_Gadea\html`: all HTML, CSS, JavaScript, and images are stored locally with zero external web dependencies.

2. **Searchable Katalog & Documentation**:
   - **Live Header Search**: Instant auto-complete search bar on every page, searching across artwork catalog IDs (e.g. `0445`, `0132`), series titles, and biography texts (with umlaut and accent tolerance).
   - **Dedicated Search Page (`search.html`)**: Real-time filtering by category, live keyword matching, search result counts, highlighted search terms, and full text search across biographical sections.

3. **Whole-Image High-Resolution Display**:
   - Clicking on any artwork thumbnail or card opens the **full-resolution, whole original image** (`-scaled.jpg` / original full photo), not just the thumbnail.
   - **Responsive Lightbox Viewer**:
     - Automatically fits the whole image cleanly to the viewport without cropping.
     - **100% Zoom / Pan Mode**: Toggle between screen-fit and 100% natural pixel scale with smooth mouse drag-to-pan or scrolling to inspect fine brushstrokes and pencil lines.
     - **Direct File Link**: "Originaldatei" button opens the full-resolution image file directly in a new tab.
     - Keyboard navigation: `Left Arrow` (previous), `Right Arrow` (next), `Escape` (close), `Z` (toggle zoom).
     - Touch swipe navigation on mobile devices.
     - Fallback `<a href="images/..." target="_blank">` on cards ensures native opening even when middle-clicked or if JavaScript is disabled.

---

### How to Run

Execute `main.py` using PyCharm or Python:

```powershell
python main.py
```

To view the generated documentation, open in any web browser:
`file:///D:/Annalis_Gadea/html/index.html`
