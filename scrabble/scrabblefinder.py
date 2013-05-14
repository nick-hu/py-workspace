#!/usr/bin/python

with open('owl.txt') as f:
    words = f.read().split()

while True:
    query = raw_input('\nWord search (type help! for syntax): ').upper()

    if query == '':
        break

    if len(query.split()) == 2:
        lengths = [int(n) for n in query.split()[1].split('/')]
    else:
        lengths = range(1, len(query.split()[0]) + 1)
    query = query.split()[0]

    if query == 'HELP!':
        print '''
    SYNTAX (by precedence):
        Letter: a/b/c/... A/B/C/...
        Vowel: ^
        Consonant: *
        Wildcard: ?
        List possible word lengths as x/y/z/... separated by a space
        from the letters.
        '''
    else:
        search = []
        for word in words:
            w, q = list(word), list(query)

            if len(w) in lengths:
                for let in word:
                    if let in q:
                        w.remove(let)
                        q.remove(let)
                    elif let in 'AEIOU' and '^' in q:
                        w.remove(let)
                        q.remove('^')
                    elif let not in 'AEIOU' and '*' in q:
                        w.remove(let)
                        q.remove('*')
                    elif '?' in q:
                        w.remove(let)
                        q.remove('?')
                if not w:
                    search.append(word)

        search, prev = sorted(search, key=len), ' '
        for word in search:
            if len(word) > len(prev):
                print '\n\n' + str(len(word)) + '-letter words:\n', word,
            else:
                print word,
            prev = word

        print
