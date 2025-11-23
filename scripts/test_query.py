from modules.rag import answer_query
if __name__ == '__main__':
    q = input('Query: ')
    print(answer_query(q))
