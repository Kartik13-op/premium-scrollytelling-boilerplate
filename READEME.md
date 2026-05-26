# Premium Video Frame Scroll Template

A lightweight, high-performance boilerplate for building cinematic "scrollytelling" landing pages using an HTML5 Canvas and an optimized WebP image sequence. This approach delivers smooth, low-latency frame scrubbing on scroll without heavy third-party libraries or embedded video players.

Key benefits:
- Fast, frame-accurate scrubbing
- Small, efficient WebP assets
- Minimal JS — paste-and-go template

**Repository structure**

- [Example/index.html](Example/index.html) — Demo page (drop-in to preview)
- [Example/frames/](Example/frames/) — Example WebP frame sequence (demo assets)
- [scripts/video_to_frames.py](scripts/video_to_frames.py) — Video → WebP extraction tool (Python + OpenCV)
- [scripts/template.html](scripts/template.html) — Copy-ready HTML template showing how to wire frames into a page
- [LICENSE](LICENSE) — MIT License

## Quick start (run the demo)

1. Install the required Python package:

```bash
pip install opencv-python
```

2. Generate the frames (from the project root):

```bash
python scripts/video_to_frames.py
```

By default the script expects a video named `orange_cola.mp4` (change the `INPUT_VIDEO` constant at the bottom of the script). It writes a sequential `0.webp`, `1.webp`, ... series to the `frames/` folder.

3. Open the demo in your browser:

Open [Example/index.html](Example/index.html) in a modern browser and scroll to scrub the sequence.

## How to use this for your project

1. Prepare your source video and keep it short (3–10s recommended for single-section scrollytelling).

2. Edit `scripts/video_to_frames.py` if needed:

- `INPUT_VIDEO` — set to your filename
- `OUTPUT_DIR` — output folder for frames
- `WEBP_QUALITY` — 1–100 (higher = better quality, larger files)
- `FRAME_SKIP` — 1 = every frame, 2 = every 2nd frame, etc.

Run the script to produce a `frames/` folder.

3. Copy `scripts/template.html` into your deployment folder (rename to `index.html`), or adapt the logic into your existing page. In the template you'll find a CONFIG block where you must set:

- `playbackSpeed` — how many scroll pixels map to one second of playback
- `totalFrames` — the exact number of frames produced by the Python script
- `currentFrame()` — the function that resolves an index into a relative URL for your `frames` folder

Example config snippet to edit inside the HTML template:

```js
const playbackSpeed = 1.0;
const totalFrames = 120; // update to match generated frames
const currentFrame = index => `./frames/${index}.webp`;
```

4. Add overlays (text, UI) by placing a positioned layer above the canvas. Example:

```html
<div style="position:relative; z-index:2; height:100vh; display:flex; align-items:center; justify-content:center;">
    <h1 style="color:#fff; font-size:4rem;">Your Headline</h1>
</div>
```

## Tips & best practices

- Use `FRAME_SKIP` to reduce frame-count for very long or high-fps videos.
- Keep `WEBP_QUALITY` between 70–90 for a good quality/size tradeoff.
- Pre-generate frames at deployment time (CI or build step) rather than on the client.
- Serve frames from a CDN for best performance on production sites.

## Troubleshooting

- If frames don't appear, confirm `totalFrames` matches the number printed by the extraction script.
- If `cv2` cannot be imported, run `pip install opencv-python`.

## License

This project is released under the MIT License. See [LICENSE](LICENSE) for details.

---

If you'd like, I can also:
- Update `Example/index.html` to include clearer configuration comments
- Add a small `requirements.txt` and a one-line npm-free demo server command
Reply with which next step you'd like.