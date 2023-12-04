from flask import Blueprint
from models.history_model import HistoryModel

history_controller = Blueprint('history', __name__)


@history_controller.route('/history/', methods=['GET'])
def get_history():
    history_records = HistoryModel.list_as_json()
    return history_records, 200
