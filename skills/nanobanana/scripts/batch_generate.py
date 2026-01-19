#!/usr/bin/env python3
"""
Batch image generation using Nano Banana (Gemini 3 Pro Image).

Usage:
    python batch_generate.py "pixel art logo" -n 20 -d ./logos -p logo
    python batch_generate.py "product photo" -n 10 --ratio 1:1 --size 4K
"""

import argparse
import sys
import time
from pathlib import Path

from generate import generate_image, VALID_ASPECT_RATIOS


def batch_generate(
    prompt: str,
    count: int = 10,
    output_dir: str = "./nanobanana-images",
    prefix: str = "image",
    aspect_ratio: str = None,
    image_size: str = None,
    delay: float = 3.0,
    verbose: bool = True,
) -> list[dict]:
    """
    Generate multiple images with sequential naming.
    
    Args:
        prompt: Text description for image generation
        count: Number of images to generate
        output_dir: Directory to save images
        prefix: Filename prefix
        aspect_ratio: Aspect ratio (1:1, 16:9, etc.)
        image_size: Resolution (2K or 4K)
        delay: Seconds to wait between generations
        verbose: Print progress
    
    Returns:
        List of result dicts
    """
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    results = []
    success_count = 0
    
    if verbose:
        print(f"Generating {count} images...")
        print(f"Prompt: {prompt}")
        print(f"Output: {output_dir}/{prefix}-XX.png")
        if aspect_ratio:
            print(f"Aspect ratio: {aspect_ratio}")
        if image_size:
            print(f"Size: {image_size}")
        print()
    
    for i in range(1, count + 1):
        filename = f"{prefix}-{str(i).zfill(2)}.png"
        filepath = output_path / filename
        
        if verbose:
            print(f"[{i}/{count}] Generating {filename}...", end=" ", flush=True)
        
        result = generate_image(
            prompt=prompt,
            output_path=str(filepath),
            aspect_ratio=aspect_ratio,
            image_size=image_size,
            verbose=False,
        )
        
        results.append(result)
        
        if result["success"]:
            success_count += 1
            if verbose:
                print("OK")
        else:
            if verbose:
                print(f"FAILED: {result['error']}")
        
        # Delay between requests (except for last one)
        if i < count and delay > 0:
            time.sleep(delay)
    
    if verbose:
        print()
        print(f"Complete: {success_count}/{count} images generated")
        print(f"Saved to: {output_dir}/")
    
    return results


def main():
    parser = argparse.ArgumentParser(
        description="Batch generate images using Nano Banana",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s "pixel art logo" -n 20 -d ./logos -p logo
  %(prog)s "product photo" -n 10 --ratio 1:1 --size 4K
  %(prog)s "landscape painting" -n 5 --ratio 16:9 --delay 5
        """
    )
    
    parser.add_argument("prompt", help="Text prompt for image generation")
    parser.add_argument("-n", "--count", type=int, default=10,
                       help="Number of images to generate (default: 10)")
    parser.add_argument("-d", "--dir", default="./nanobanana-images",
                       help="Output directory")
    parser.add_argument("-p", "--prefix", default="image",
                       help="Filename prefix (default: image)")
    parser.add_argument("-r", "--ratio", choices=VALID_ASPECT_RATIOS,
                       help="Aspect ratio")
    parser.add_argument("-s", "--size", choices=["2K", "4K", "2k", "4k"],
                       help="Image size (2K or 4K)")
    parser.add_argument("--delay", type=float, default=3.0,
                       help="Delay between generations in seconds (default: 3)")
    parser.add_argument("-q", "--quiet", action="store_true",
                       help="Suppress progress output")
    
    args = parser.parse_args()
    
    results = batch_generate(
        prompt=args.prompt,
        count=args.count,
        output_dir=args.dir,
        prefix=args.prefix,
        aspect_ratio=args.ratio,
        image_size=args.size.upper() if args.size else None,
        delay=args.delay,
        verbose=not args.quiet,
    )
    
    # Exit with error if all failed
    success_count = sum(1 for r in results if r["success"])
    if success_count == 0:
        sys.exit(1)


if __name__ == "__main__":
    main()
