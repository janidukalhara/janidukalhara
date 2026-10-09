# Profile design and maintenance

This repository powers Janidu Kalhara's GitHub profile. The design uses GitHub Flavored Markdown, supported HTML, and local SVG assets. It does not require a web framework or a deployment service.

## October 2026 animated redesign

The first version was too restrained for Janidu's preference. The current version uses a dark neon cyan/purple/pink palette, animated typography, moving borders, and animated project illustrations.

- `assets/hero.svg`: gradient lettering, a moving highlight over the name, floating code/cube motifs, stars, and a travelling border.
- The former standalone typing GIF has been removed from the README. The role now types inside the terminal section.
- Six project illustrations animate scanning, heartbeat traces, floating shapes, bar charts, and circuit details.
- `assets/divider.svg` and the social buttons add smaller supporting animations.
- The toolkit is integrated into the terminal, with a readable Markdown alternative. React and Python silhouette masks derive from Skill Icons; see `skill-icons-LICENSE.txt`.
- `assets/github-snapshot.svg` contains a dated, real public-repository snapshot, not invented contribution or streak data. Refresh it when needed; it is not a live widget.
- Run `python scripts/generate_visuals.py` with Pillow installed to regenerate the original motion assets. The icon board and dated repository snapshot are maintained separately. The script needs DejaVu Sans Mono on Linux or Consolas on Windows.
- SVG animations stop under `prefers-reduced-motion: reduce`. The main name, project labels, and contact destinations remain readable without animation.

## Portrait terminal and contribution snake

The banner and complete selected-project section were preserved byte-for-byte in this revision, as requested.

- `assets/about-{dark,light}.svg`: desktop terminal; portrait and skills on the left, system information on the right.
- `assets/about-{dark,light}-mobile.svg`: stacked mobile composition with larger type. README picture sources select the layout and color scheme.
- `scripts/generate_terminal.py`: deterministic generator using Pillow, NumPy, and SciPy. Run `python scripts/generate_terminal.py` from the repository root after installing `scripts/requirements-terminal.txt`. DejaVu Sans Mono is required for the code glyph.
- `scripts/data/portrait-*.npy` and `logo-points.npy`: generated point arrays. React/Python PNGs are source alpha masks; code.png is generated. Original portrait remains in assets/janidu.jpg.
- Portrait: 300×340 serpentine Floyd–Steinberg dithering, background mask, 60 scattered reveal groups, 94 noisy drift groups. A 3.2-second intro leads into a 14.2-second portrait → React → Python → code loop with 900 individually matched particles.
- Reduced motion shows a still portrait and fully readable heading; no motion or third-party runtime is required for the terminal. SVGs contain no JavaScript, embedded raster images, or external fonts.
- `.github/workflows/snake.yml` generates real contribution-calendar SVGs every 12 hours and on manual dispatch. It publishes only to the `output` branch. Both actions are pinned to commit SHAs. The built-in GITHUB_TOKEN is enough; no PAT or external deployment is required.
- The first snake run succeeded: [workflow run](https://github.com/janidukalhara/janidukalhara/actions/runs/37931526594). Scheduled runs can be delayed by GitHub; manually run the workflow if needed.

Visual direction follows Janidu's supplied terminal screenshot, setup guide, and master prompt. The [Instagram reel](https://www.instagram.com/reel/DePNFhmT8aa/) caption was accessible; audiovisual playback was not available. Only the relevant terminal and snake instructions were applied; no separate stats deployment or token setup was needed.

## Edit the profile

- Edit `README.md` for the introduction, skills, contact links, and project summaries.
- Edit SVG files in `assets/` to change the banner and card artwork. Keep `<title>`, `<desc>`, and reduced-motion support.
- Replace `assets/janidu.jpg` only when changing the portrait.
- Check the rendered README in GitHub's light and dark themes and on a narrow screen after editing.
- The original README remains available in Git history.

## Project evidence reviewed on 2026-10-09

| Project | Sources | Accuracy notes |
| --- | --- | --- |
| Culinary Assistant | [README](https://github.com/janidukalhara/Culinary-Assistant/blob/main/README.md), backend and frontend file tree | Has pretrained modes and training scripts. No claim of completed custom training, validated accuracy, or production deployment. |
| MediLink | [README](https://github.com/janidukalhara/medilink/blob/main/README.md), service/controller/component tree | Described as a project, not a clinically validated service. |
| Nexus J Commerce | [Architecture](https://github.com/janidukalhara/Nexus-J-Commerce/blob/main/replit.md), routes and schema tree | No claim of verified live payment processing. |
| TerraMind Analytics | [Prediction implementation](https://github.com/janidukalhara/TerraMind-Analytics/blob/main/artifacts/api-server/src/lib/waste-prediction.ts), architecture notes | The fallback uses keywords and random values; described as simulated, not a trained BERT model. |
| eScrap-Link | [Image analysis route](https://github.com/janidukalhara/eScrap-Link/blob/main/artifacts/api-server/src/routes/analyze.ts), workspace docs and route tree | AI suggestions are described without implying verified recovery or safety results. |
| OEH Traders | [Backend](https://github.com/janidukalhara/OEH-TRADERS/blob/main/backend/server.py), frontend tree | Product, account, cart, and quotation models support the summary. |

Education, availability, and the Digital Vesak award use information supplied by Janidu. The email and LinkedIn destination were retained from his previous profile. Private repositories were not linked or made public. Digital Vesak is linked to the public demo previously supplied by Janidu.

## User-provided video references

The descriptions of both videos were retrieved directly from their public YouTube pages. Full audiovisual playback was not available, so no claim is made of watching them end-to-end. No vidIQ credits were spent.

- [Uday Dot Ai tutorial](https://www.youtube.com/watch?v=JEFOzaeEJaw): introduction, technology icons, social links, stats cards, and activity graphics.
- [BrainHuntclub Short](https://www.youtube.com/shorts/kdEUUcpdY-I): recommends Readme Typing SVG, Shields.io, skill/project sections, GitHub stats, and streak tools.

This design uses original local animation assets to apply the requested visual direction. It retains accurate project information. It does not claim that repository-language counts measure programming proficiency.

## Research references

These sources informed the layout; they do not establish a universal 2026 design trend. YouTube research used the public video description and chapter list, not a claim of watching the video. General web search and targeted Reddit/YouTube searches were used.

- [GitHub Docs: Using your GitHub profile to enhance your resume](https://docs.github.com/en/account-and-profile/tutorials/using-your-github-profile-to-enhance-your-resume) — concise introduction and selected, relevant work.
- [GitHub Community: Prepping Your GitHub Profile for 2026](https://github.com/orgs/community/discussions/186153) — current focus, accessible profiles, simple SVG headers.
- [YouTube: How to Create a Professional GitHub Profile README in 2026](https://www.youtube.com/watch?v=JEFOzaeEJaw), Uday Dot Ai, 2026-08-10 — profile structure, skills, and contact information.
- [Reddit: Replacing my generated profile README template to a clean, minimal one](https://www.reddit.com/r/github/comments/1r0cd83/replacing_my_generated_profile_readme_template_to/) — a community example of simplifying template-heavy profiles.
- [Reddit: Any tips to customize my profile readme?](https://www.reddit.com/r/github/comments/1q9kg8e/any_tips_to_customize_my_profile_readme/) — differing preferences for animation and visual density.

## Optional profile settings

GitHub's pinned repositories and account bio are separate from this README. Good pin candidates are Culinary Assistant, MediLink, Nexus J Commerce, TerraMind Analytics, eScrap-Link, and OEH Traders. Use the profile's **Customize your pins** control if desired.
