class Twitter:

    def __init__(self):
        self.time = 0
        self.following = {} # userId -> list of ids this user follows
        self.tweets = {} # userId -> list of [timestamp, tweetId]
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets:
            self.tweets[userId] = []
        self.tweets[userId].append([self.time, tweetId])
        self.time += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []

        following = self.following.get(userId, [])

        for uid in self.tweets:
            if uid in following or uid == userId:
                tweets = self.tweets[uid]

                for timestamp, tweetId in tweets:
                    heapq.heappush(heap, [timestamp, tweetId])

                    if len(heap) > 10:
                        heapq.heappop(heap)

        ans = []

        while heap:
            timestamp, tweetId = heapq.heappop(heap)
            ans.append(tweetId)

        ans.reverse()
        return ans
                

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.following:
            self.following[followerId] = set()
        self.following[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following:
            self.following[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)