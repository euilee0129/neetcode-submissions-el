class Solution:
    def isPalindrome(self, s: str) -> bool:
        stack = []
        j = 0
        text = ''.join(ch.lower() for ch in s if ch.isalnum())

        for i in range( len(text)-1, 0, -1):
            # if text[j].isalnum() and not text[i].isalnum():
            #     i-=1
            # elif not text[j].isalnum() and text[i].isalnum():
            #     j+=1
            # elif not text[j].isalnum() and not text[i].isalnum():
            #     i-=1
            #     j+=1
            # else:
            stack.append(text[i].lower())
            # print("stack in: ", stack[0], text[i])
            popped = stack.pop()
            if popped != text[j]:
                # print("stack out: ", popped, text[j])
                return False
            else:
                j+=1
        return True
        