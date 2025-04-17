#!/bin/bash

mkdir subset_images

for zipfile in /cluster/work/igp_psr/pano_infinigen_part1.zip /cluster/work/igp_psr/pano_infinigen_part2.zip /cluster/work/igp_psr/pano_infinigen_part3.zip; do
    scene=$(unzip -Z1 "$zipfile" | grep -oE '^[^/]+/' | sort -u | shuf -n 1)
    echo "📦 Extracting $scene from $zipfile..."
    unzip "$zipfile" "${scene}*" -d subset_images
done

echo "✅ Done! Scenes saved to subset_images/"
