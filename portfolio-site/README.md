# ORGANVM Portfolio Site

The unified front door for the eight-organ creative-institutional system.

## Architecture

- **Framework**: Astro (static site generator)
- **Data source**: `registry-v2.json` via `praxis-portfolio-generate.py`
- **Design tokens**: Derived from `taste.yaml` aesthetic pillars
- **Deploy target**: Vercel or GitHub Pages

## Pages

| Page | Path | Data Source |
|------|------|-------------|
| Landing | `/` | `site-data/landing.json` |
| Projects | `/projects/` | `site-data/projects.json` |
| Essays | `/essays/` | `site-data/essays.json` |
| Architecture | `/architecture/` | `site-data/graph.json` |
| Dashboard | `/dashboard/` | `system-metrics.json` |
| About | `/about/` | `site-data/about.json` |

## Development

```bash
# Generate site data from registry
npm run generate-data

# Install dependencies
npm install

# Development server
npm run dev

# Production build
npm run build
```

## Data Pipeline

```
registry-v2.json
       |
       v
praxis-portfolio-generate.py  -->  site-data/*.json
       |
       v
    Astro build  -->  dist/  -->  Vercel/GitHub Pages
```

## Design

The visual language follows the `taste.yaml` aesthetic pillars:
- **Density**: Information-rich layouts, no wasted space
- **Structure**: Clear hierarchy, organ-based color coding
- **Reference**: Links to source repos, essays, registry
- **Precision**: Monospace metrics, exact counts
- **Warmth**: Serif body text, warm color palette
