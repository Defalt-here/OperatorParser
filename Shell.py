import IncelLang as il

while True:
		text = input('basic > ')
		result, error = il
		il.run('<stdin>', text)

		if error: print(error.as_string())
		else: print(result)