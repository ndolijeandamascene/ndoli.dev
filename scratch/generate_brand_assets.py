import os
from PIL import Image, ImageDraw, ImageFont

static_img_dir = r"c:\Users\ndoli\Documents\WEBAPP\ndoli.dev\static\images"
os.makedirs(static_img_dir, exist_ok=True)

# 1. Helper function to draw the "ND" brand logo on an image
def draw_brand_mark(draw, x_center, y_center, size):
    # size is bounding box size
    scale = size / 512.0
    
    # N coordinates offset
    # N: (128, 152) -> (288, 360)
    # D: (308, 152) -> (432, 360)
    # Dot: (432, 352)
    # Center of 512x512 is (256, 256)
    
    ox = x_center - (256 * scale)
    oy = y_center - (256 * scale)
    
    def pt(x, y):
        return (ox + x * scale, oy + y * scale)
    
    # N path
    n_poly = [
        pt(128, 360), pt(128, 152), pt(172, 152), pt(248, 276), 
        pt(248, 152), pt(288, 152), pt(288, 360), pt(244, 360), 
        pt(168, 236), pt(168, 360)
    ]
    draw.polygon(n_poly, fill=(248, 250, 252))
    
    # D outer
    # Approximating rounded D with bbox arc / polygon
    d_left = ox + 308 * scale
    d_top = oy + 152 * scale
    d_right = ox + 432 * scale
    d_bottom = oy + 360 * scale
    
    draw.rounded_rectangle([d_left, d_top, d_right, d_bottom], radius=int(40 * scale), fill=(34, 197, 94))
    # D inner hole
    h_left = ox + 348 * scale
    h_top = oy + 192 * scale
    h_right = ox + 392 * scale
    h_bottom = oy + 320 * scale
    draw.rounded_rectangle([h_left, h_top, h_right, h_bottom], radius=int(20 * scale), fill=(15, 23, 27))
    
    # Yellow Dot
    dot_x = ox + 432 * scale
    dot_y = oy + 352 * scale
    dot_r = 16 * scale
    draw.ellipse([dot_x - dot_r, dot_y - dot_r, dot_x + dot_r, dot_y + dot_r], fill=(250, 204, 21))

# 2. Generate Favicon & App Icons
def create_app_icon(size, filename):
    img = Image.new("RGBA", (size, size), (11, 15, 16, 255))
    draw = ImageDraw.Draw(img)
    
    # Subtle border
    border_r = int(size * 0.22)
    draw.rounded_rectangle([1, 1, size - 2, size - 2], radius=border_r, outline=(34, 197, 94, 180), width=max(1, int(size * 0.02)))
    
    # Draw brand mark
    draw_brand_mark(draw, size / 2, size / 2, size * 0.75)
    
    out_path = os.path.join(static_img_dir, filename)
    img.save(out_path, "PNG")
    print(f"Generated {out_path} ({size}x{size})")

for sz, fn in [(16, "favicon-16x16.png"), (32, "favicon-32x32.png"), (180, "apple-touch-icon.png"), (192, "android-chrome-192x192.png"), (512, "android-chrome-512x512.png")]:
    create_app_icon(sz, fn)

# Also save a standard favicon.ico in static/
img_32 = Image.open(os.path.join(static_img_dir, "favicon-32x32.png"))
img_32.save(os.path.join(r"c:\Users\ndoli\Documents\WEBAPP\ndoli.dev\static", "favicon.ico"), format="ICO")

# 3. Generate High-Quality Open Graph Card (1200x630)
def create_og_image():
    W, H = 1200, 630
    img = Image.new("RGBA", (W, H), (11, 15, 16, 255))
    draw = ImageDraw.Draw(img)
    
    # Background subtle grid / accents
    for x in range(0, W, 60):
        draw.line([(x, 0), (x, H)], fill=(255, 255, 255, 6), width=1)
    for y in range(0, H, 60):
        draw.line([(0, y), (W, y)], fill=(255, 255, 255, 6), width=1)
        
    # Subtle green glow at top-right
    for r in range(300, 0, -20):
        alpha = int(12 * (1 - r / 300))
        draw.ellipse([W - 200 - r, 100 - r, W - 200 + r, 100 + r], fill=(34, 197, 94, alpha))
        
    # Card outer glowing border
    draw.rounded_rectangle([20, 20, W - 20, H - 20], radius=24, outline=(34, 197, 94, 90), width=2)
    
    # Brand Mark on left
    draw_brand_mark(draw, 160, 160, 140)
    
    # Try loading Arial / Trebuchet / default fonts
    try:
        font_brand = ImageFont.truetype("arialbd.ttf", 32)
        font_name = ImageFont.truetype("arialbd.ttf", 52)
        font_role = ImageFont.truetype("arialbd.ttf", 26)
        font_desc = ImageFont.truetype("arial.ttf", 24)
        font_tag = ImageFont.truetype("courbd.ttf", 20)
    except Exception:
        font_brand = font_name = font_role = font_desc = font_tag = ImageFont.load_default()
        
    # Brand Top Title
    draw.text((250, 120), "NDOLI", fill=(255, 255, 255), font=font_brand)
    draw.text((360, 120), ".DEV", fill=(34, 197, 94), font=font_brand)
    draw.text((250, 165), "AUTHORITATIVE PERSONAL PLATFORM & SYSTEMS ARCHITECTURE", fill=(148, 163, 184), font=ImageFont.load_default())
    
    # Divider line
    draw.line([(80, 240), (W - 80, 240)], fill=(34, 197, 94, 100), width=2)
    
    # Person Name
    draw.text((80, 275), "NDOLI JEAN DAMASCENE", fill=(255, 255, 255), font=font_name)
    
    # Professional Identity
    draw.text((80, 350), "IT PROFESSIONAL  ·  SOFTWARE DEVELOPER  ·  SYSTEMS BUILDER", fill=(250, 204, 21), font=font_role)
    
    # Mission statement
    desc_text = "Building practical digital systems, intelligent software, and enterprise technology solutions."
    draw.text((80, 410), desc_text, fill=(203, 213, 225), font=font_desc)
    
    # Bottom Tags / Badges
    tags = ["DJANGO", "PYTHON", "POSTGRESQL", "PGVECTOR / RAG", "LINUX INFRASTRUCTURE", "KIGALI, RWANDA"]
    tx = 80
    ty = 490
    for tag in tags:
        # Measure text or estimate
        tag_w = len(tag) * 11 + 24
        draw.rounded_rectangle([tx, ty, tx + tag_w, ty + 40], radius=8, fill=(20, 28, 32), outline=(34, 197, 94, 120), width=1)
        draw.text((tx + 12, ty + 10), tag, fill=(34, 197, 94) if "RWANDA" not in tag else (250, 204, 21), font=font_tag)
        tx += tag_w + 14
        
    # URL signature
    draw.text((80, 560), "https://ndoli.dev", fill=(148, 163, 184), font=font_tag)
    draw.text((W - 360, 560), "Official Verified Canonical Profile", fill=(34, 197, 94), font=font_tag)
    
    og_out_path = os.path.join(static_img_dir, "ndoli-og-image.png")
    img.save(og_out_path, "PNG")
    print(f"Generated OG Image: {og_out_path} ({W}x{H})")

create_og_image()
print("All static branding assets generated successfully!")
