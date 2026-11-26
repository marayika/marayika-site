# Handover: marayika.com

Notes for whoever works on this site next, including a new Claude session.
Read this before changing anything.

## What this is

The personal brand website of Ange Théonastine Ashimwe (pen name Marayika).
Five pages: Home, Portfolio, Diary, Soft Epilogue, Contact.

## Where everything lives

| Part | Where |
|---|---|
| Domain | Canva, marayika.com. Renews every November. |
| Website files | This repository, marayika/marayika-site (public). |
| Hosting | GitHub Pages, built by `.github/workflows/deploy.yml` on every push to `main`. |
| Diary editor | Pages CMS (app.pagescms.org), configured by `.pages.yml`. |
| Email | hello@marayika.com through Google Workspace. Separate from the website. |

### DNS records in Canva (do not change)

- A `@`: 185.199.108.153, 185.199.109.153, 185.199.110.153, 185.199.111.153
- CNAME `www`: marayika.github.io
- MX, SPF and DKIM records: email. Never delete.
- "Connected to Canva" is switched off on purpose.

## How the site is built

- Eleventy 3. Source in `src/`, output in `_site/` (not committed).
- `npm install && npm run build` builds it locally.
- Home, Portfolio, Soft Epilogue and Contact are plain HTML in `src/<page>/index.html`
  (Home is `src/index.html`). Edit them directly.
- The Diary page is `src/diary/index.njk`. It loops over `src/diary/posts/*.md`,
  which Pages CMS writes. Each post has: title, link, subtitle, date, category
  (Poetry, Essay or Gallery), cover, cover_alt, images, note.
- Images: `src/images/` (site images) and `src/media/` (Diary uploads from Pages CMS).

## The `design/` folder (history, not the live source)

The site was first designed as a Claude Design canvas, then exported to static HTML.

- `design/canvas/`: the canvas pages (`.dc.html`) and `canvas.json`, as of launch.
- `design/assets/`: the original compressed images.
- `design/scripts/export.py`: canvas pages to static HTML.
- `design/scripts/make_cms.py` and `diary_card.py`: built the Eleventy project
  and the first five Diary posts.
- `design/scripts/overflow.py` and `filtertest.py`: Playwright checks for phone
  overflow and the Diary filters.

**Do not rerun `make_cms.py` on this repository.** It regenerates the Diary posts
from hard-coded data and would overwrite anything added in Pages CMS. Its paths
also point to the old workspace (`/home/claude/...`). Since launch, `src/` is the
source of truth. Make changes there.

## Design rules Ange chose

- Grid-line notebook paper (28px squares) with a red margin line.
- Mostly black and white, accent red #BA2924 (her Substack red).
- Fonts: Bricolage Grotesque (headings), Inter (body), Caveat (handwriting).
  Newsreader appears only on the Diary page. Avoid adding more fonts.
- Taped photo and clipping style. Hand-drawn SVG arrows. Never emoji, never the ↗ glyph.
- Writing: plain, verb-first, one idea per sentence, no AI-sounding phrasing.
  Accuracy matters more than completeness.
- The email address is never shown as text. Buttons open a "Send an email / Copy address" menu.
- Do not type other writers' poems into the site. Ange adds quoted poems herself.
- Diary pieces live on Substack. The site shows a cover, title and subtitle, and links out.

## Links used on the site

- Substack: marayika.substack.com
- Instagram: marayika.diary (personal), softepilogue.atelier (bookshop)
- X: marayikadiary
- LinkedIn: linkedin.com/in/marayika, linkedin.com/company/soft-epilogue
- Free library (Google Drive): see `src/soft-epilogue/index.html`

## Checks before publishing a change

1. `npm run build` finishes without errors.
2. No page scrolls sideways at 360px, 390px and 1280px wide.
3. The Diary filters (All, Poetry, Essays, Gallery) show the right pieces.
