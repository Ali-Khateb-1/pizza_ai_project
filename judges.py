from flask import Blueprint, jsonify

# إنشاء الـ Blueprint لنقاط النهاية الخاصة بالحكام
judges_bp = Blueprint('judges_bp', __name__)

@judges_bp.route('/judges', methods=['GET'])
def judges_access():
    data = {
        "message": "مرحباً بالحكام! هذه هي نقطة النهاية المخصصة وسهلة الوصول."
    }
    return jsonify(data)
