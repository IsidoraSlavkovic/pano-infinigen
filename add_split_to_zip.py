import zipfile

zip_path = "/cluster/work/igp_psr/pano_infinigen.zip"

# Local split files you want to add into the zip
split_files = [
    "/cluster/work/igp_psr/islavkovic/pano-infinigen/train_split.txt", 
    "/cluster/work/igp_psr/islavkovic/pano-infinigen/val_split.txt", 
    "/cluster/work/igp_psr/islavkovic/pano-infinigen/test_split.txt"]

# Append to the existing zip
with zipfile.ZipFile(zip_path, 'a', compression=zipfile.ZIP_STORED) as z:
    print(f"📥 Adding {split_files[0]} to zip")
    z.write(split_files[0], arcname="train_split.txt")
    print(f"📥 Adding {split_files[1]} to zip")
    z.write(split_files[1], arcname="val_split.txt")
    print(f"📥 Adding {split_files[2]} to zip")
    z.write(split_files[2], arcname="test_split.txt")

print(f"\n✅ Added split files to {zip_path}")
