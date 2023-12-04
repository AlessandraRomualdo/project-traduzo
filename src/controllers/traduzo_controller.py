from flask import Blueprint, render_template, request
from models.language_model import LanguageModel
from deep_translator import GoogleTranslator
from models.history_model import HistoryModel


traduzo_controller = Blueprint("traduzo_controller", __name__)


@traduzo_controller.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        text_to_translate = request.form.get("text-to-translate")
        translate_from = request.form.get("translate-from")
        translate_to = request.form.get("translate-to")

        translated = GoogleTranslator(
            source=translate_from, target=translate_to
            ).translate(text_to_translate)

        history_data = {
            "text-to-translate": text_to_translate,
            "translate-from": translate_from,
            "translate-to": translate_to,
            "translated-text": translated
        }
        HistoryModel(history_data).save()

        return render_template(
            "index.html",
            languages=LanguageModel.list_dicts(),
            text_to_translate=text_to_translate,
            translate_from=translate_from,
            translate_to=translate_to,
            translated=translated,
        )
    else:
        return render_template(
            "index.html",
            languages=LanguageModel.list_dicts(),
            text_to_translate="O que deseja traduzir?",
            translate_from="pt",
            translate_to="en",
            translated="What do you want to translate?"
        )


@traduzo_controller.route("/reverse", methods=["POST"])
def reverse_translate():
    text_to_translate = request.form.get("text-to-translate")
    translate_from = request.form.get("translate-from")
    translate_to = request.form.get("translate-to")

    translated = GoogleTranslator(
        source=translate_from, target=translate_to
        ).translate(text_to_translate)

    history_data = {
        "text-to-translate": translated,
        "translate-from": translate_to,
        "translate-to": translate_from,
        "translated-text": text_to_translate
    }
    HistoryModel(history_data).save()
    return render_template(
        "index.html",
        languages=LanguageModel.list_dicts(),
        text_to_translate=translated,
        translate_from=translate_to,
        translate_to=translate_from,
        translated=text_to_translate,
    )
