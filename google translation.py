from google.cloud import translate


strings_to_translate = ["Hello", "Good bye", "I love you", "The cat in the hat likes green eggs and ham"]
languages = ["en", "es", "ru", "zh-CN"]
translate_client = translate.Client()
for i, s in enumerate(strings_to_translate):
    for j, l in enumerate(languages):
        print(translate_client.translate(s, target_language=l))