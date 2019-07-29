#encoding=utf-8

class Stack:

    stk_lst = []

    def top(self):
        if len(self.stk_lst) == 0:
            return None
        else:
            return self.stk_lst[-1]
    
    def length(self):
        
        return len(self.stk_lst)


    def pop(self):

        if len(self.stk_lst) == 0:
            return None
        else:
            self.stk_lst.pop()

    
    def push(self, value):
        
        self.stk_lst.append(value)

    
    def output(self):
        
        for val in self.stk_lst:
            print(str(val))


def ParseParentheses(str_line):

    mapper = {}
    mapper['(']= ')'
    mapper['['] = ']'
    mapper['{'] = '}'

    valid_list = ['(',')','{','}','[',']']

    stk = Stack()

    str_lst = list(str_line)

    for str_word in str_lst:
      
        if str_word in valid_list:
            if str_word in mapper:
                stk.push(str_word)
            else: #need to match now
                if stk.length == 0:
                    return False

                if mapper[stk.top()] == str_word:
                    stk.pop()
                    continue
                else:
                    return False
    
    return True

        
def unit_test():
    stk = Stack()
    stk.push(1)
    stk.push(2)
    stk.push(4)
    stk.output()

    stk.pop()
    stk.output()

if __name__ == '__main__':

    str_line = '(){}[][{())}]'

    print(ParseParentheses(str_line))