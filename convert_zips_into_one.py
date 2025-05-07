import zipfile

# Paths to input zip files
input_zips = [
    "/cluster/work/igp_psr/infinigen_outdoor_3000s.zip",
    "/cluster/work/igp_psr/infinigen_outdoor_3000s_part2.zip",
    "/cluster/work/igp_psr/infinigen_outdoor_3000s_part3.zip",
    "/cluster/work/igp_psr/infinigen_outdoor_3000s_part4.zip",
]

# Output zip file
output_zip = "/cluster/work/igp_psr/pano_infinigen_outdoor.zip"

# Combine zips without compression
with zipfile.ZipFile(output_zip, 'w', compression=zipfile.ZIP_STORED) as out_zip:
    for zip_path in input_zips:
        print(f"Adding from: {zip_path}")
        with zipfile.ZipFile(zip_path, 'r') as in_zip:
            for item in in_zip.infolist():
                if item.is_dir():
                    continue  # Skip directory entries
                out_zip.writestr(item, in_zip.read(item.filename))

# Verification
print("\n✅ Combined zip created:", output_zip)
with zipfile.ZipFile(output_zip, 'r') as z:
    entries = z.namelist()
    print(f"Total files: {len(entries)}")
    print("Sample entries:")
    for name in entries[:10]:
        print("  ", name)
