# The Year You Arrived

A personal birthday archive with the original sequence:
1. Opening screen — **The Year You Arrived**
2. Birthday wish, letter, and original photo
3. Six-clue birthday treasure hunt
4. Surprise video and final note

The original photo and original 80-second 2160 × 3840 MP4 are included in this project.

## Run locally

Requires Node.js 22 or newer.

```bash
npm ci
npm run dev
```

## Deploy to GitHub Pages

1. Create a GitHub repository and upload/push the contents of this ZIP to the repository's `main` branch. Keep the `.github/workflows/deploy.yml` file.
2. Open **Settings → Pages** in the repository.
3. Under **Build and deployment**, select **GitHub Actions** as the source.
4. Open the **Actions** tab and wait for **Deploy website to GitHub Pages** to finish successfully.
5. Open the URL shown by the deployment workflow.

The Vite build uses relative asset paths so the bundled photo/video and other assets can load from a GitHub Pages project URL.

## Important notes

- The website's core sequence and supplied media are included in the repository; no Google AI Studio token is needed to build or host it.
- Browser-local customization uploads are not a server-side publishing mechanism. GitHub Pages is static hosting, so uploaded replacements cannot update the repository or become visible to other visitors automatically.
- The video is bundled from `src/assets/birthday_video.mp4`. Its source file in this project reports an 80-second duration, H.264 video at 2160 × 3840, with AAC audio.
