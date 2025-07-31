from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json
import openai
import os
from django.conf import settings
from .models import ChatMessage

def home(request):
    """トップページ"""
    return render(request, 'chat/home.html')

def about(request):
    """アバウトページ"""
    return render(request, 'chat/about.html')

def contact(request):
    """お問い合わせページ"""
    return render(request, 'chat/contact.html')

@csrf_exempt
@require_http_methods(["POST"])
def chat_api(request):
    """AIチャットAPI"""
    try:
        data = json.loads(request.body)
        user_message = data.get('message', '')
        
        if not user_message:
            return JsonResponse({'error': 'メッセージが空です'}, status=400)
        
        # OpenAI APIキーの確認
        print(f"DEBUG: settings.OPENAI_API_KEY type: {type(settings.OPENAI_API_KEY)}")
        print(f"DEBUG: settings.OPENAI_API_KEY value: {settings.OPENAI_API_KEY}")
        print(f"DEBUG: settings.OPENAI_API_KEY length: {len(settings.OPENAI_API_KEY) if settings.OPENAI_API_KEY else 0}")
        print(f"DEBUG: os.getenv('OPENAI_API_KEY'): {os.getenv('OPENAI_API_KEY')[:20] if os.getenv('OPENAI_API_KEY') else 'None'}")
        
        if not settings.OPENAI_API_KEY:
            print(f"DEBUG: OPENAI_API_KEY is None or empty")
            return JsonResponse({'error': 'OpenAI APIキーが設定されていません'}, status=500)
        
        print(f"DEBUG: Using OpenAI API key: {settings.OPENAI_API_KEY[:20]}...")
        
        # OpenAIクライアントの初期化
        client = openai.OpenAI(api_key=settings.OPENAI_API_KEY)
        
        # AI応答の取得
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "あなたは親切で役立つAIアシスタントです。日本語で丁寧に回答してください。"},
                {"role": "user", "content": user_message}
            ],
            max_tokens=1000,
            temperature=0.7
        )
        
        ai_response = response.choices[0].message.content
        
        # データベースに保存
        ChatMessage.objects.create(
            user_message=user_message,
            ai_response=ai_response
        )
        
        return JsonResponse({
            'response': ai_response,
            'status': 'success'
        })
        
    except openai.APIError as e:
        return JsonResponse({'error': f'OpenAI APIエラー: {str(e)}'}, status=500)
    except Exception as e:
        return JsonResponse({'error': f'エラーが発生しました: {str(e)}'}, status=500)
