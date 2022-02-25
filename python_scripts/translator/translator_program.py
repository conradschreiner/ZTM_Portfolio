from translate import Translator

translator = Translator(to_lang='es')
try:
	with open('python_sublime_projects/translate_exercise.txt', mode='r') as my_file:
		text = my_file.read()
		translation = translator.translate(text)
		with open('python_sublime_projects/translate_exercise_result2.txt', mode='w') as my_file_result:
			my_file_result.write(translation)
except FileNotFoundError as e:
	print('Check your path something is wrong')