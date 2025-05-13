import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications import EfficientNetB0
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D
import os

# 🔹 تحسين البيانات عبر `Data Augmentation`
datagen = ImageDataGenerator(
    rotation_range=20,   # تدوير الصورة
    width_shift_range=0.2,  # إزاحة الصورة أفقيًا
    height_shift_range=0.2,  # إزاحة عموديًا
    shear_range=0.2,  # تأثير القص
    zoom_range=0.2,  # تكبير/تصغير
    horizontal_flip=True,  # قلب الصورة أفقيًا
    fill_mode='nearest'  # ملء الفجوات بعد التعديلات
)

# 🔹 تحميل بيانات التدريب
train_generator = datagen.flow_from_directory(
    'data/clusters',
    target_size=(64, 64),
    batch_size=32,
    class_mode='categorical'
)

# 🔹 تحسين النموذج باستخدام `EfficientNetB0`
base_model = EfficientNetB0(weights="imagenet", include_top=False, input_shape=(64, 64, 3))
x = base_model.output
x = GlobalAveragePooling2D()(x)
x = Dense(128, activation="relu")(x)
predictions = Dense(3, activation="softmax")(x)

model = Model(inputs=base_model.input, outputs=predictions)

# 🔹 ضبط معلمات التدريب لتحسين الدقة
model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.0001),
              loss="categorical_crossentropy",
              metrics=["accuracy"])

# 🔹 تدريب النموذج
model.fit(train_generator, epochs=10)

# 🔹 إنشاء مجلد لحفظ النموذج إذا لم يكن موجودًا
save_path = "models"
if not os.path.exists(save_path):
    os.makedirs(save_path)

# 🔹 حفظ النموذج بعد التدريب
model.save(os.path.join(save_path, "model_cnn_updated.h5"))

print("🎉 تم تدريب النموذج المعدّل وحفظه بنجاح في مجلد 'models'!")
