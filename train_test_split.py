import zipfile
import random

# Path to the dataset zip(s)
zip_paths = [
    "/cluster/work/igp_psr/infinigen_outdoor_1000s_part4.zip",
    "/cluster/work/igp_psr/infinigen_outdoor_3000s_part3.zip",
    "/cluster/work/igp_psr/infinigen_outdoor_3000s_part2.zip",
    "/cluster/work/igp_psr/infinigen_outdoor_3000s.zip"
]

# Output split txt files
train_split_path = "/cluster/work/igp_psr/islavkovic/pano-infinigen/train_split_outdoor.txt"
val_split_path = "/cluster/work/igp_psr/islavkovic/pano-infinigen/val_split_outdoor.txt"
test_split_path = "/cluster/work/igp_psr/islavkovic/pano-infinigen/test_split_outdoor.txt"

scene_names = set()
# Step 1: Extract top-level folder (scene) names
for zip_path in zip_paths:
    with zipfile.ZipFile(zip_path, 'r') as z:
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

train_scenes = scene_names[:8000]
val_scenes = scene_names[8000:9000]
test_scenes = scene_names[9000:10000]

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
