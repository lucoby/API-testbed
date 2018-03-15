import json
from watson_developer_cloud import LanguageTranslatorV2

language_translator = LanguageTranslatorV2(
    username=USERNAME,
    password=PASSWORD)


# models = language_translator.list_models()
# print(json.dumps(models, indent=2))


strings_to_translate = ["Hello", "Good bye", "I love you", "The cat in the hat likes green eggs and ham"]
models = ["en-es-conversational", "en-ko", "en-ja"]
for i, s in enumerate(strings_to_translate):
    for j, m in enumerate(models):
        translation = language_translator.translate(text=s, model_id=m)
        print(json.dumps(translation, indent=2, ensure_ascii=False))