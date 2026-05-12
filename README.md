# 21Bloom — homepage concepts

Three homepage directions for 21Bloom (Dubai same-day gifting florist), exported
from Claude Design and packaged for GitHub Pages so a client can review them in
a browser.

The deployable site lives in `docs/`:

```
docs/
  index.html         # overview — links to all three concepts
  01-editorial.html  # ivory paper, serif-led, magazine quiet
  02-noir.html       # black canvas, champagne accents
  03-desert.html     # sand + terracotta, Gulf-rooted
  tweaks-panel.jsx   # shared live-tweak panel (palette / type / hero)
  .nojekyll          # tells Pages to skip Jekyll processing
```

Each concept page has its own Tweaks panel (bottom-right) for live palette /
typography / hero-layout swaps, and a top-of-page switcher to jump between
concepts.

## Deploy to GitHub Pages

1. Create an empty repo on GitHub (e.g. `21bloom-design`).
2. From this directory:

   ```sh
   git init
   git add docs README.md
   git commit -m "21Bloom homepage concepts"
   git branch -M main
   git remote add origin git@github.com:<you>/<repo>.git
   git push -u origin main
   ```

3. On GitHub: **Settings → Pages → Build and deployment**
   - Source: **Deploy from a branch**
   - Branch: **`main`** / **`/docs`**
   - Save.

The site will be live at `https://<you>.github.io/<repo>/` within a minute or two.

## Local preview

```sh
cd docs && python3 -m http.server 8000
# open http://localhost:8000
```

## Notes for the client review

- Static HTML/CSS/JS — no build step.
- Designed at 1440px (desktop-only mockup); resize the browser to see how it
  holds up but treat narrow widths as out of scope for this round.
- Placeholder striped panels stand in for product photography — drop real
  images in their place before launch.
