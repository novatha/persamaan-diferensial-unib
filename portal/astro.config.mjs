// @ts-check
import { defineConfig } from 'astro/config';
import mdx from '@astrojs/mdx';
import remarkMath from 'remark-math';
import rehypeKatex from 'rehype-katex';

// Configuration for subpath deployment at https://www.ndaratha.my.id/persamaan-diferensial/
export default defineConfig({
  site: 'https://www.ndaratha.my.id',
  base: '/persamaan-diferensial',
  integrations: [mdx()],
  markdown: {
    remarkPlugins: [remarkMath],
    rehypePlugins: [rehypeKatex],
  },
  prefetch: {
    prefetchAll: true,
    defaultStrategy: 'hover'
  }
});
