from django.db import models

# Create your models here.

class ChatMessage(models.Model):
    """チャットメッセージモデル"""
    user_message = models.TextField(verbose_name='ユーザーメッセージ')
    ai_response = models.TextField(verbose_name='AI応答')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='作成日時')
    
    class Meta:
        verbose_name = 'チャットメッセージ'
        verbose_name_plural = 'チャットメッセージ'
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.user_message[:50]}... ({self.created_at.strftime('%Y-%m-%d %H:%M')})"
