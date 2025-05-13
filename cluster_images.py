import cv2

import numpy as np
import os
from sklearn.cluster import KMeans

# تحديد مسار مجلد الصور
image_folder = "~/pizza_ai_project/data/images"
image_folder = os.path.expanduser(image_folder)

# تحديد مسار مجلدات التجميع
cluster_folder = os.path.expanduser("~/pizza_ai_project/data/clusters")

# إنشاء مجلدات التجميع إذا لم تكن موجودة
for i in range(3):  # لأن لدينا 3 مجموعات
    cluster_path = os.path.join(cluster_folder, f"group_{i}")
    os.makedirs(cluster_path, exist_ok=True)  # التأكد من أن المجلد موجود

# الحصول على قائمة الصور
images = sorted([f for f in os.listdir(image_folder) if f.lower().endswith(('jpg', 'jpeg', 'png'))])
image_features = []

for image_name in images:
    img_path = os.path.join(image_folder, image_name)
    img = cv2.imread(img_path)

    # تحويل الصورة إلى بيانات عددية
    img_resized = cv2.resize(img, (64, 64))
    img_flattened = img_resized.flatten()

    image_features.append(img_flattened)

# تطبيق `K-Means` لتجميع الصور إلى 3 مجموعات
kmeans = KMeans(n_clusters=3, random_state=42)
clusters = kmeans.fit_predict(image_features)

# نقل الصور إلى مجلدات التجميع المناسبة
for i, image_name in enumerate(images):
    cluster_group = clusters[i]  # رقم المجموعة التي تنتمي إليها الصورة
    old_path = os.path.join(image_folder, image_name)
    new_folder = os.path.join(cluster_folder, f"group_{cluster_group}")
    new_path = os.path.join(new_folder, image_name)

    os.rename(old_path, new_path)
    print(f"✅ تم نقل {image_name} إلى المجموعة {cluster_group}")

print("🎉 تم تجميع الصور ونقلها إلى مجلداتها المناسبة!")
