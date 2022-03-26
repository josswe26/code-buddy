from django.db import models
from django.contrib.auth.models import User

SCORE = ((1, 'Upvote'), (-1, 'Downvote'))


class Question(models.Model):
    """ Question model """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='user_questions'
    )
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    votes_score = models.IntegerField(default=0)
    upvoted = models.BooleanField(default=False)
    downvoted = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


class Reply(models.Model):
    """ Reply model """
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name='replies'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='user_replies'
    )
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    votes_score = models.IntegerField(default=0)
    upvoted = models.BooleanField(default=False)
    downvoted = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'replies'
        ordering = ['-created_on']

    def __str__(self):
        return f"Reply: {self.body} by {self.author}"


class QuestionVote(models.Model):
    """ Question votes model """
    voter = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='user_question_votes'
    )
    score = models.IntegerField(choices=SCORE)
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name='question_votes'
    )


class ReplyVote(models.Model):
    """ Reply votes model """
    voter = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='user_reply_votes'
    )
    score = models.IntegerField(choices=SCORE)
    reply = models.ForeignKey(
        Reply,
        on_delete=models.CASCADE,
        related_name='reply_votes')
