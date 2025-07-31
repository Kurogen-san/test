from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.db.models import Count
from django.utils import timezone
from datetime import timedelta
from chat.models import ChatMessage
from .models import AdminLog, SystemSettings
import json

def admin_login(request):
    """管理画面ログイン"""
    if request.user.is_authenticated:
        return redirect('admin_panel:dashboard')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None and user.is_staff:
            login(request, user)
            # ログインログを記録
            AdminLog.objects.create(
                user=user,
                action='ログイン',
                details=f'管理画面にログインしました',
                ip_address=request.META.get('REMOTE_ADDR', '0.0.0.0')
            )
            messages.success(request, 'ログインしました。')
            return redirect('admin_panel:dashboard')
        else:
            messages.error(request, 'ユーザー名またはパスワードが正しくありません。')
    
    return render(request, 'admin_panel/login.html')

@login_required
def admin_logout(request):
    """管理画面ログアウト"""
    # ログアウトログを記録
    AdminLog.objects.create(
        user=request.user,
        action='ログアウト',
        details=f'管理画面からログアウトしました',
        ip_address=request.META.get('REMOTE_ADDR', '0.0.0.0')
    )
    logout(request)
    messages.success(request, 'ログアウトしました。')
    return redirect('admin_panel:login')

@login_required
def dashboard(request):
    """管理画面ダッシュボード"""
    # 統計データを取得
    total_messages = ChatMessage.objects.count()
    today_messages = ChatMessage.objects.filter(
        created_at__date=timezone.now().date()
    ).count()
    week_messages = ChatMessage.objects.filter(
        created_at__gte=timezone.now() - timedelta(days=7)
    ).count()
    
    # 最近のチャットメッセージ
    recent_messages = ChatMessage.objects.order_by('-created_at')[:10]
    
    # 最近の管理ログ
    recent_logs = AdminLog.objects.order_by('-created_at')[:5]
    
    # 日別メッセージ数（過去7日間）
    daily_stats = []
    for i in range(7):
        date = timezone.now().date() - timedelta(days=i)
        count = ChatMessage.objects.filter(created_at__date=date).count()
        daily_stats.append({
            'date': date.strftime('%m/%d'),
            'count': count
        })
    daily_stats.reverse()
    
    context = {
        'total_messages': total_messages,
        'today_messages': today_messages,
        'week_messages': week_messages,
        'recent_messages': recent_messages,
        'recent_logs': recent_logs,
        'daily_stats': daily_stats,
    }
    
    return render(request, 'admin_panel/dashboard.html', context)

@login_required
def chat_messages(request):
    """チャットメッセージ管理"""
    messages_list = ChatMessage.objects.order_by('-created_at')
    
    # 検索機能
    search = request.GET.get('search', '')
    if search:
        messages_list = messages_list.filter(
            user_message__icontains=search
        ) | messages_list.filter(
            ai_response__icontains=search
        )
    
    context = {
        'messages': messages_list,
        'search': search,
    }
    return render(request, 'admin_panel/chat_messages.html', context)

@login_required
def system_settings(request):
    """システム設定"""
    if request.method == 'POST':
        # 設定の更新
        for key, value in request.POST.items():
            if key.startswith('setting_'):
                setting_key = key.replace('setting_', '')
                setting, created = SystemSettings.objects.get_or_create(key=setting_key)
                setting.value = value
                setting.save()
        
        messages.success(request, '設定を更新しました。')
        return redirect('admin_panel:system_settings')
    
    settings_list = SystemSettings.objects.all()
    context = {
        'settings': settings_list,
    }
    return render(request, 'admin_panel/system_settings.html', context)

@login_required
def admin_logs(request):
    """管理ログ"""
    logs = AdminLog.objects.order_by('-created_at')
    
    # フィルタリング
    action_filter = request.GET.get('action', '')
    if action_filter:
        logs = logs.filter(action__icontains=action_filter)
    
    context = {
        'logs': logs,
        'action_filter': action_filter,
    }
    return render(request, 'admin_panel/admin_logs.html', context)

@login_required
def delete_message(request, message_id):
    """メッセージ削除"""
    try:
        message = ChatMessage.objects.get(id=message_id)
        message.delete()
        
        # 削除ログを記録
        AdminLog.objects.create(
            user=request.user,
            action='メッセージ削除',
            details=f'メッセージID: {message_id}を削除しました',
            ip_address=request.META.get('REMOTE_ADDR', '0.0.0.0')
        )
        
        return JsonResponse({'status': 'success'})
    except ChatMessage.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'メッセージが見つかりません'})
