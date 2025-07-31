from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class AdminLog(models.Model):
    """管理画面ログ"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='ユーザー')
    action = models.CharField(max_length=100, verbose_name='アクション')
    details = models.TextField(blank=True, verbose_name='詳細')
    ip_address = models.GenericIPAddressField(verbose_name='IPアドレス')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='作成日時')
    
    class Meta:
        verbose_name = '管理ログ'
        verbose_name_plural = '管理ログ'
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.user.username} - {self.action} ({self.created_at.strftime('%Y-%m-%d %H:%M')})"

class SystemSettings(models.Model):
    """システム設定"""
    key = models.CharField(max_length=100, unique=True, verbose_name='設定キー')
    value = models.TextField(verbose_name='設定値')
    description = models.TextField(blank=True, verbose_name='説明')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新日時')
    
    class Meta:
        verbose_name = 'システム設定'
        verbose_name_plural = 'システム設定'
    
    def __str__(self):
        return f"{self.key}: {self.value[:50]}..."
