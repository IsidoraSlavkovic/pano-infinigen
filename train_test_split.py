import zipfile
import random

# Path to the combined dataset zip
combined_zip_path = "/cluster/work/igp_psr/pano_infinigen.zip"

# Output split txt files
train_split_path = "/cluster/work/igp_psr/islavkovic/pano-infinigen/train_split.txt"
val_split_path = "/cluster/work/igp_psr/islavkovic/pano-infinigen/val_split.txt"
test_split_path = "/cluster/work/igp_psr/islavkovic/pano-infinigen/test_split.txt"

# Step 1: Extract top-level folder (scene) names
with zipfile.ZipFile(combined_zip_path, 'r') as z:
    scene_names = set()
    for name in z.namelist():
        print("Name list: ", name)
        if '/' in name:
            scene = name.split('/')[7]
            print("Scene name: ", scene)
            scene_names.add(scene)

# Step 2: Shuffle and split
scene_names = list(scene_names)
random.shuffle(scene_names)

print("Total scene count: ", len(scene_names))

train_scenes = scene_names[:7000]
val_scenes = scene_names[7000:8000]
test_scenes = scene_names[8000:10000]

# Step 3: Save to text files
with open(train_split_path, "w") as f:
    f.write("\n".join(train_scenes))
with open(val_split_path, "w") as f:
    f.write("\n".join(val_scenes))
with open(test_split_path, "w") as f:
    f.write("\n".join(test_scenes))

# ✅ Done
print("\n🎉 Split completed!")
print(f"📝 Train split: {train_split_path} ({len(train_scenes)} scenes)")
print(f"📝 Val split:   {val_split_path} ({len(val_scenes)} scenes)")
print(f"📝 Test split:  {test_split_path} ({len(test_scenes)} scenes)")
