trans = { '0':'rei', '1':'ichi', '2':'ni', '3':'san', '4': 'yon',
'5':'go', '6':'roku', '7':'nana', '8':'hachi', '9':'kyu',
'10': 'juu'}

Answer=""

def convert_to_japanese(ar_num):
    if ar_num in range(0,11):
        Answer = trans[str(ar_num)]
    elif ar_num in range (11,20):
        Answer = "juu" + trans[str((ar_num - 10))]
    elif ar_num in range(20,100):
        n = str(ar_num)
        Answer = trans[str(n[0])] + "juu" + trans[str(n[1])]
    return Answer
    
    
