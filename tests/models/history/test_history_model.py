import json
from src.models.history_model import HistoryModel


# Req. 7
def test_request_history():
    query = {
        "text_to_translate": "O que deseja traduzir?",
        "translate_from": "pt",
        "translate_to": "en",
        "translated_text": "What do you want to translate?"
    }
    HistoryModel(query).save()
    data = HistoryModel.list_as_json()
    json_data = json.loads(data)
    assert len(json_data) > 0
    assert isinstance(json_data[0], dict)
    assert "text_to_translate" in json_data[0]
    assert "translate_from" in json_data[0]
    assert "translate_to" in json_data[0]
    assert "O que deseja traduzir?" in json_data[2]["text_to_translate"]
    assert "pt" in json_data[2]["translate_from"]
    assert "en" in json_data[2]["translate_to"]
    assert "What do you want to translate?" in json_data[2]["translated_text"]
