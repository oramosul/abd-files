import sys

for linea in sys.stdin:
        claves = linea.split(',')
        if (len(claves)>8):
                subreddit = claves[7]
                n_upvotes = claves[6]
                n_downvotes = claves[8]
        else:
                continue
        if (n_upvotes.isnumeric() and n_downvotes.isnumeric()):
                print("{}|{}|{}".format(subreddit, n_upvotes, n_downvotes))
