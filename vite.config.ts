import tailwindcss from '@tailwindcss/vite';
import react from '@vitejs/plugin-react';
import path from 'path';
import fs from 'fs';
import { defineConfig } from 'vite';

const photoUploadPlugin = () => ({
  name: 'photo-upload-handler',
  configureServer(server: any) {
    server.middlewares.use('/api/upload-photo', (req: any, res: any) => {
      if (req.method === 'POST') {
        const chunks: Buffer[] = [];
        req.on('data', (chunk: Buffer) => chunks.push(chunk));
        req.on('end', () => {
          try {
            const buffer = Buffer.concat(chunks);
            fs.writeFileSync(path.resolve(__dirname, 'public/kishor_photo.jpg'), buffer);
            fs.writeFileSync(path.resolve(__dirname, 'src/assets/images/kishor_photo.jpg'), buffer);
            res.setHeader('Content-Type', 'application/json');
            res.end(JSON.stringify({ success: true, url: '/kishor_photo.jpg?v=' + Date.now() }));
          } catch (e: any) {
            res.statusCode = 500;
            res.end(JSON.stringify({ error: e.message }));
          }
        });
      } else {
        res.statusCode = 405;
        res.end();
      }
    });
  },
});

export default defineConfig(() => {
  return {
    base: './',
    plugins: [react(), tailwindcss(), photoUploadPlugin()],
    resolve: {
      alias: {
        '@': path.resolve(__dirname, '.'),
      },
    },
    server: {
      port: 3000,
      host: '0.0.0.0',
      // HMR is disabled in AI Studio via DISABLE_HMR env var.
      // Do not modify—file watching is disabled to prevent flickering during agent edits.
      hmr: process.env.DISABLE_HMR !== 'true',
      // Disable file watching when DISABLE_HMR is true to save CPU during agent edits.
      watch: process.env.DISABLE_HMR === 'true' ? null : {},
    },
  };
});
