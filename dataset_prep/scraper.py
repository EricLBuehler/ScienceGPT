import praw
import tqdm

def clean_text(text: str) -> str: #Strip text
    return text.strip()

def scrape_subreddit(reddit: praw.Reddit, data: list, subreddit: str, skip: int, max_allow_len: int = 2048) -> int:
    print("Scraping", subreddit)
    hot_posts = reddit.subreddit(subreddit).hot(limit = 10000)
    maxlen = -1
    for i, post in tqdm.tqdm(enumerate(hot_posts)):
        if i < skip: # Skip headers
            continue
        question = ""
        if post.title[-1] not in [".", "!", "?"]:
            question += clean_text(post.title) + "."
        else:
            question += clean_text(post.title)

        question += " "
        question += clean_text(post.selftext)
        question += "\n"
        for top_level_comment in reddit.submission(id=post.id).comments:
            if isinstance(top_level_comment, praw.models.MoreComments):
                for comment in top_level_comment.comments():
                    if comment.body == "[removed]" or comment.stickied:
                        continue
                    res = question + clean_text(comment.body) + "\0"
                    if len(res) > max_allow_len:
                        continue
                    data.append(res)
                    if len(data[-1]) > maxlen:
                        maxlen = len(data[-1])
                continue

            if top_level_comment.body == "[removed]" or top_level_comment.stickied:
                continue
                    
            res = question + clean_text(top_level_comment.body) + "\0"
            if len(res) > max_allow_len:
                continue
            data.append(res)
            
            if len(data[-1]) > maxlen:
                maxlen = len(data[-1])

    return maxlen

reddit = praw.Reddit(client_id="fO05Zgvq53-yoAPrz-Yesw", client_secret='9rkeMCecw-qDgRrfWUQAuJ-yUoz6LQ', user_agent='Web Scraper')

data = []
maxlen = -1

max = scrape_subreddit(reddit, data, "AskScience", 2) 
if max > maxlen:
    maxlen = max

max = scrape_subreddit(reddit, data, "LearnPython", 1) 
if max > maxlen:
    maxlen = max

max = scrape_subreddit(reddit, data, "cpp_questions", 2) 
if max > maxlen:
    maxlen = max

max = scrape_subreddit(reddit, data, "javahelp", 1) 
if max > maxlen:
    maxlen = max

max = scrape_subreddit(reddit, data, "askprogramming", 1) 
if max > maxlen:
    maxlen = max

print(len(data),"data points")
print("Max length:",maxlen)
print("Average length:", sum([len(item) for item in data])/len(data))

with open("reddit_scrape.txt", "w") as f:
    f.write("\n".join(data))