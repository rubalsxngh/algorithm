'''
the below soundex function takes input of two words and
1. declared in the function is hm, a list of list, which groups the similar sounding letters.
2. Check soundex for word1
3. check soundex for word2
4. if matches, the words sounds similar
'''

def soundex(word1, word2):
    hm= [['a', 'e', 'i', 'o', 'u', 'h', 'w', 'y'], 
        ['b', 'f', 'p', 'v'],
        ['c', 'g', 'j', 'k', 'q', 's', 'x', 'z'],
        ['d', 't'], 
        ['l'],
        ['m', 'n'],
        ['r']]
    
    # calculating soundex of 1st word
    sound1=''
    for ch in word1:

        i=0 

        while i< len(hm):
            if ch in hm[i]:
                sound1+=str(i+1)
            
            i+=1
    
    # calculating soundex of 2nd word
    sound2=''
    for ch in word2:

        i=0 

        while i< len(hm):
            if ch in hm[i]:
                sound2+=str(i+1)
            
            i+=1

    if sound1== sound2:
        return 1
    
    else:
        return 0



def main():
    word1= list(input())
    word2= list(input())


    ans= soundex(word1, word2)

    if ans==1:
        print('the sound of words matches...')
    else:
        print('the sound doesnt match.....')



if __name__== '__main__':
    main()