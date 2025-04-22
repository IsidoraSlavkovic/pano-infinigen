import zipfile
import os
from pathlib import Path
import shutil

# Paths to your original zip files
zip_files = [
    "/cluster/work/igp_psr/pano_infinigen_part1.zip",
    "/cluster/work/igp_psr/pano_infinigen_part2.zip",
    "/cluster/work/igp_psr/pano_infinigen_part3.zip"
]

# Output zip file that will contain only Image folders
output_zip = "/cluster/work/igp_psr/pano_infinigen_rgb_only.zip"

# Temporary extraction folder
temp_dir = Path("temp_extract")
temp_dir.mkdir(exist_ok=True)
image_count = 0

with zipfile.ZipFile(output_zip, 'w', compression=zipfile.ZIP_STORED, allowZip64=True) as out_zip:
    for zip_path in zip_files:
        print(f"Processing zip: {zip_path}")
        with zipfile.ZipFile(zip_path, 'r') as z:
            for file in z.namelist():
                # Target only files under '.../frames/Image/...'
                if '/frames/Image/camera_0/' in file and not file.endswith('/'):
                    # Extract file temporarily
                    extracted_path = temp_dir / file
                    extracted_path.parent.mkdir(parents=True, exist_ok=True)
                    with open(extracted_path, 'wb') as f:
                        f.write(z.read(file))
                    
                    # Add to new zip without compression
                    out_zip.write(extracted_path, arcname=file)
                    print(f"Wrote: {file}")

                    # Remove temporary file to save disk space
                    extracted_path.unlink()
                    image_count += 1

# Optional: clean up temp folder
shutil.rmtree(temp_dir)

print(f"\n Done! Created uncompressed zip: {output_zip}")
print(f"Total images written: {image_count}")

