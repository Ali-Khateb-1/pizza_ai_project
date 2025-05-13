import os

# تحديد مسار مجلد الصور
image_folder = "~/pizza_ai_project/data/images"
image_folder = os.path.expanduser(image_folder)  # دعم المسارات داخل WSL

# الحصول على قائمة بجميع الصور
images = sorted([f for f in os.listdir(image_folder) if f.lower().endswith(('jpg', 'jpeg', 'png'))])

# إعادة التسمية بترقيم تلقائي
for i, filename in enumerate(images):
    extension = filename.split(".")[-1]  # الحصول على امتداد الملف
    new_name = f"pizza_{i+1}.{extension}"  # اسم جديد بصيغة pizza_1, pizza_2...
    old_path = os.path.join(image_folder, filename)
    new_path = os.path.join(image_folder, new_name)

    os.rename(old_path, new_path)
    print(f"✅ تم إعادة تسمية {filename} إلى {new_name}")

print("🎉 جميع الصور أصبحت منظمة بأسماء مرتبة!")