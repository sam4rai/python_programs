from googletrans import Translator


def get_translate(text="Hello", src="ru", dest="en"):
    
    try:
        translator = Translator()
        
        translation = translator.translate(text=text, src=src, dest='en')
        
        return translation.text
    
    except Exception as ex:
        return ex


def main():
    print(get_translate(text=input("Mess: ")))


if __name__ == "__main__":
    main()
    