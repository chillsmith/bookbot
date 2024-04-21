def main():
    path="books/frankenstein.txt"
    text=get_book_text(path)
    print(f'\n--- Begin report of {path} ---')
    print(f"{get_num_words(text)} words found in the document\n")
    character_dict=get_character_dict(text)
    List_char_dict=list_of_dict(character_dict)
    List_char_dict.sort(reverse=True, key=sort_on)
    for i in List_char_dict:
        print(f"The {i["character"]} character was found {i["count"]} times")

    

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_words(text):
    return len(text.split())

def get_character_dict(text):
    lowered=text.lower()
    char_count={}
    for _char in lowered:
        if _char in char_count:
            char_count[_char]+=1
        elif _char.isalpha():
            char_count[_char]=1
    return char_count

def list_of_dict(dict_):
    List=[]
    for key, value in dict_.items():
        temp={}
        temp["character"]=key
        temp["count"]=value
        List.append(temp)     
    return List 

def sort_on(dict):
    return dict["count"]

     
        

    
main()