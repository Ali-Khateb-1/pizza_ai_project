import tensorflow as tf
from PIL import Image
import numpy as np
import sys

# تحميل النموذج
model = tf.keras.models.load_model("model_cnn.h5")

# التأكد من تمرير اسم الصورة عبر سطر الأوامر
if len(sys.argv) < 2:
    print("❌ يجب تمرير اسم ملف الصورة لاختبار النموذج!")
    sys.exit(1)

# تحميل الصورة واختبارها
image_path = sys.argv[1]
image = Image.open(image_path).resize((64, 64))
image_array = np.array(image) / 255.0

prediction = model.predict(image_array.reshape(1, 64, 64, 3))

# تحديد التصنيف النهائي
labels = ["group_0", "group_1", "group_2"]
predicted_label = labels[np.argmax(prediction)]

print(f"🔍 الصورة: {image_path}, 🔎 التصنيف المتوقع: {predicted_label}")
