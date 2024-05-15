import sys

subreddit = None
suma1 = 0
suma2 = 0

for linea in sys.stdin:
        subreddit_nuevo, upvote, downvote = linea.split('|')
        if (subreddit_nuevo == subreddit):
                suma1 += int(upvote)
                suma2 += int(downvote)
        else:
                if (subreddit != None):
                        print(subreddit, suma1, suma2)
                suma1 = 0
                suma2 = 0
                subreddit = subreddit_nuevo
