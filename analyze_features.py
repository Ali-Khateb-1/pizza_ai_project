import cv2
import numpy as np
import os

# تحديد مسار مجلد الصور
image_folder = "~/pizza_ai_project/data/images"
image_folder = os.path.expanduser(image_folder)

# الحصول على قائمة الصور
images = sorted([f for f in os.listdir(image_folder) if f.lower().endswith(('jpg', 'jpeg', 'png'))])

for image_name in images:
    img_path = os.path.join(image_folder, image_name)
    img = cv2.imread(img_path)
    
    # تحليل الألوان باستخدام Histogram
    hist = cv2.calcHist([img], [0], None, [256], [0,256])
    
    # كشف الحواف باستخدام Canny Edge Detection
    edges = cv2.Canny(img, 100, 200)
    
    print(f"✅ تم تحليل الميزات البصرية للصورة: {image_name}")

print("🎉 تحليل الميزات البصرية لجميع الصور اكتمل!")
