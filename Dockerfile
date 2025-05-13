# استخدم إصدار Python الأساسي
FROM python:3.8

# تعيين مجلد العمل داخل الحاوية
WORKDIR /app

# نسخ جميع ملفات المشروع إلى الحاوية
COPY . /app

# تثبيت المكتبات المطلوبة
RUN pip install -r requirements.txt

# تحديد نقطة التشغيل
CMD ["python", "main.py"]
