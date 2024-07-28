class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}

        for file_name in self.file_names:
            try:
                with open(file_name, 'r', encoding='utf-8') as file:
                    text = file.read().lower()  # Считываем содержимое файла и приводим к нижнему регистру

                    for punct in [',', '.', '=', '!', '?', ';', ':', ' - ']: # Избавляемся от пунктуации
                        text = text.replace(punct, '')

                    words = text.split()  # Разбиваем текст на слова
                    all_words[file_name] = words
            except FileNotFoundError:
                # В случае если файл не найден, продолжаем обработку следующих файлов
                print(f"File {file_name} not found. Skipping...")
                continue

        return all_words

    def find(self, word):
        word = word.lower()  # Приводим слово к нижнему регистру для сравнения
        all_words = self.get_all_words()
        result = {}

        for name, words in all_words.items():
            for i, w in enumerate(words):
                if w == word:
                    result[name] = i + 1
                    break

        return result

    def count(self, word):
        word = word.lower()
        all_words = self.get_all_words()
        result = {}

        for name, words in all_words.items():
            count = words.count(word)
            result[name] = count

        return result


# Пример использования
finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
