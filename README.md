# Image2WEBP Converter

A high-performance desktop application for converting JPG, JPEG, and PNG images into optimized WEBP format.

Built with Python and PySide6, Image2WEBP Converter provides fast batch processing, configurable compression, and real-time conversion monitoring.

---

## Features

### Image Input

- Single image conversion
- Multiple image conversion
- Folder batch conversion
- Drag and drop image input
- Duplicate image detection
- Thumbnail preview
- Image list management
- Cached thumbnails for faster loading

---

### WEBP Conversion

- Lossless WEBP conversion
  - Preserve original image quality
  - Quality setting is ignored

- Lossy WEBP conversion
  - Adjustable quality control (1-100)
  - Higher quality produces better image quality with larger file size
  - Lower quality produces smaller file size with more compression

---

### Compression Profile

Choose conversion performance based on your needs:

| Profile | Method | Description |
|---|---|---|
| Fast Conversion | Method 2 | Faster processing for large batch conversion |
| Balanced Quality | Method 4 | Balance between speed and compression |
| Maximum Compression | Method 6 | Smaller output size with longer processing time |

---

### Performance Features

- Multiprocessing conversion engine
- Automatic hardware detection
- Adaptive worker allocation
- Background conversion thread
- Non-blocking GUI operation
- Cancel conversion support

---

### Conversion Monitoring

Real-time monitoring includes:

- Conversion progress
- Current processing file
- Success count
- Failed count
- CPU usage monitoring
- RAM usage monitoring
- Active worker information
- Selected WEBP compression profile

---

### Conversion Statistics

After conversion, the application provides:

- Total processed files
- Successful conversions
- Failed conversions
- Conversion duration
- Processing speed (images/second)
- Original file size
- Output WEBP size
- Storage reduction percentage

---

## Supported Input Formats

- JPG
- JPEG
- PNG

---

## Output Format

- WEBP

---

## Technology Stack

- Python
- PySide6 (Desktop GUI)
- Pillow (Image Processing)
- ProcessPoolExecutor (Multiprocessing)
- QThread (Background Processing)

---

## Performance Example

Test environment:

- CPU: 8 Cores / 16 Threads
- RAM: 16 GB

Example batch conversion:
