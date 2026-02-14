import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
  site: 'https://organvm.dev',
  integrations: [sitemap()],
  build: {
    format: 'directory',
  },
});
