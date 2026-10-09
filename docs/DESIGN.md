# Profile design and maintenance

This repository powers Janidu Kalhara's GitHub profile. The design uses GitHub Flavored Markdown, supported HTML, and local SVG assets. It does not require a web framework or a deployment service.

## Design

- Navy, cyan, and restrained violet accents, with separate light and dark hero artwork selected by a `picture` element.
- Original, unedited portrait supplied by Janidu.
- A decorative SVG orbit with a `prefers-reduced-motion` override. Essential information never depends on animation.
- Six public project cards, readable descriptions, and working repository destinations.
- Native text repeats essential information for accessibility and narrow screens; all images have alt text.
- Local assets avoid availability dependencies on remote badge, GIF, and statistics services.

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

## Research references

These sources informed the layout; they do not establish a universal 2026 design trend. YouTube research used the public video description and chapter list, not a claim of watching the video. General web search and targeted Reddit/YouTube searches were used.

- [GitHub Docs: Using your GitHub profile to enhance your resume](https://docs.github.com/en/account-and-profile/tutorials/using-your-github-profile-to-enhance-your-resume) — concise introduction and selected, relevant work.
- [GitHub Community: Prepping Your GitHub Profile for 2026](https://github.com/orgs/community/discussions/186153) — current focus, accessible profiles, simple SVG headers.
- [YouTube: How to Create a Professional GitHub Profile README in 2026](https://www.youtube.com/watch?v=JEFOzaeEJaw), Uday Dot Ai, 2026-08-10 — profile structure, skills, and contact information.
- [Reddit: Replacing my generated profile README template to a clean, minimal one](https://www.reddit.com/r/github/comments/1r0cd83/replacing_my_generated_profile_readme_template_to/) — a community example of simplifying template-heavy profiles.
- [Reddit: Any tips to customize my profile readme?](https://www.reddit.com/r/github/comments/1q9kg8e/any_tips_to_customize_my_profile_readme/) — differing preferences for animation and visual density.

## Optional profile settings

GitHub's pinned repositories and account bio are separate from this README. Good pin candidates are Culinary Assistant, MediLink, Nexus J Commerce, TerraMind Analytics, eScrap-Link, and OEH Traders. Use the profile's **Customize your pins** control if desired.
