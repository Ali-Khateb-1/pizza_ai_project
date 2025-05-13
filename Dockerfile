# استخدام أحدث إصدار متوافق من Python
FROM python:3.12

# تعيين مجلد العمل داخل الحاوية
WORKDIR /app

# نسخ ملف المتطلبات فقط أولًا لتسريع بناء الصورة
COPY requirements.txt /app/

# تثبيت المكتبات المطلوبة بدون تخزين مؤقت
RUN pip install --no-cache-dir -r requirements.txt

# نسخ باقي ملفات المشروع بعد تثبيت التبعيات
COPY . /app/

# تعيين المتغيرات البيئية الافتراضية (إذا كان ذلك مطلوبًا)
ENV FLASK_ENV=production
ENV API_KEY=your_api_key_here

# فتح منفذ الاتصالات (إذا كان المشروع يعتمد على ذلك)
EXPOSE 5000

# تعيين نقطة تشغيل الحاوية
CMD ["python", "app.py"]
