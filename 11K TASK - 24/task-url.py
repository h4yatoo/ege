from re import finditer

data = 'Я был на сайте https://future-step.ru/ и нашел там отличную статью https://future-step.ru/tutor/python-regexp/ и теперь хорошо понимаю регулярки.'
pattern = r'(http|https)://\S+'

matches = [match.group() for match in finditer(pattern, data)]

print(matches)