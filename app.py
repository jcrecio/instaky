from instapy import InstaPy
from instapy import smart_run

insta_username = 'mohernanz'
insta_password = 'mohernanzpass'

instagram_session = InstaPy(username=insta_username,
                  password=insta_password)

with smart_run(instagram_session):
    instagram_session.set_do_follow(True, percentage=50)

    instagram_session.set_do_comment(True, percentage=100)

    instagram_session.set_comments(["nice!", ":heart_eyes: :heart_eyes: :heart_eyes: @{}", "amazing"])

    instagram_session.set_quota_supervisor(enabled=True, 
        peak_comments_daily=20, 
        peak_comments_hourly=2, 
        peak_likes_daily=250,
        peak_likes_hourly=30, 
        sleep_after=['likes', 'follows'])

    instagram_session.set_relationship_bounds(enabled=True,
                                    delimit_by_numbers=True,
                                    max_followers=3000,
                                    min_followers=150,
                                    min_following=50)

    instagram_session.like_by_tags(['ufc','mma', 'martialarts', 'salsa', 'boxing', 'padel'], amount=300)

instagram_session.end()