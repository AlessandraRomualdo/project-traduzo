from flask import Blueprint, render_template, request
from models.language_model import LanguageModel

traduzo_controller = Blueprint("traduzo_controller", __name__)


@traduzo_controller.route("/", methods=["GET"])
def index():
    languages = LanguageModel.list_dicts()
    text_to_translate = request.form.get(
        'text-to-translate') or 'O que deseja traduzir?'
    translate_from = request.form.get('translate-from')
    translate_to = request.form.get('translate-to')
    translated = request.form.get(
        'translated') or 'What do you want to translate?'
    return render_template(
        "index.html",
        languages=languages,
        text_to_translate=text_to_translate,
        translate_from=translate_from,
        translate_to=translate_to,
        translated=translated,
    )
