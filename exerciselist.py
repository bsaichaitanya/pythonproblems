def list_thing(words):
    if len(words) == 1:
        return words[0]
    return '{}, and {}'.format(', '.join(words[:-1]), words[-1])




data_call1 =  list_thing(['microsoft','google','ibm','virtusa'])
#data_call2 = list_any(['deloitte','xerox','apple','nissan','tata','synopsis'])


print(data_call1)
#print(data_call2)