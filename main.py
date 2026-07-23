import datetime

def ai_assistant_response(message):
    """
    Simulates a third-party AI assistant's response based on user input.
    This function represents the core logic of an external AI service
    that would process messages received from a platform like WhatsApp.
    """
    message_lower = message.lower()

    # --- Simulate summarization capability ---
    # In a real scenario, an LLM would process the text to summarize.
    # Here, we simulate by acknowledging the request and providing a mock summary.
    if "özetle" in message_lower or "summarize" in message_lower:
        if "toplantı notlarını" in message_lower or "meeting notes" in message_lower:
            # This simulates the AI processing specific content (meeting notes)
            return "Toplantı notlarınız özetleniyor... Ana noktalar: Proje X ilerlemesi, yeni görev dağılımı, bir sonraki toplantı tarihi."
        elif "bu metni" in message_lower or "this text" in message_lower:
            # General text summarization request
            return "Metni özetliyorum. Ana fikir: [Buraya özetlenmiş metin gelecek]."
        else:
            return "Neyi özetlememi istersiniz?"

    # --- Simulate translation capability ---
    # In a real scenario, an LLM or translation API would be used.
    # Here, we provide hardcoded translations for common phrases.
    elif "çevir" in message_lower or "translate" in message_lower:
        if "merhaba" in message_lower:
            # This simulates the AI translating a specific word/phrase
            return "Merhaba -> Hello"
        elif "nasılsın" in message_lower:
            return "Nasılsın -> How are you?"
        elif "görüşürüz" in message_lower:
            return "Görüşürüz -> See you!"
        else:
            return "Hangi kelime veya cümleyi çevirmemi istersiniz?"

    # --- Simulate information retrieval / general response ---
    elif "hava durumu" in message_lower or "weather" in message_lower:
        # Provides specific information, similar to an AI fetching data.
        return "Şu anki hava durumu bilgisi: Güneşli ve 25°C. (Bu bilgi gerçek zamanlı değildir, sadece bir simülasyondur.)"
    elif "saat kaç" in message_lower or "what time" in message_lower:
        # Uses a standard library function to provide dynamic information.
        return f"Şu an saat: {datetime.datetime.now().strftime('%H:%M')}. (Bu bilgi gerçek zamanlıdır.)"
    elif "merhaba" in message_lower or "hi" in message_lower:
        return "Merhaba! Size nasıl yardımcı olabilirim?"
    elif "teşekkürler" in message_lower or "thanks" in message_lower:
        return "Rica ederim! Başka bir isteğiniz var mı?"
    elif "yardım" in message_lower or "help" in message_lower:
        return "Size toplantı notlarını özetleyebilir, kelime çevirebilir veya genel sorularınıza yanıt verebilirim. Ne yapmak istersiniz?"
    elif "çıkış" in message_lower or "exit" in message_lower or "quit" in message_lower:
        return "Görüşmek üzere! Hoşça kalın."
    else:
        # General AI response for unhandled queries, prompting for more specific input.
        return "Anladım. Bu konuda size nasıl yardımcı olabilirim? Örneğin, 'toplantı notlarını özetle' veya 'merhaba çevir' diyebilirsiniz."

def main():
    print("WhatsApp Üçüncü Parti AI Asistanı Simülatörüne Hoş Geldiniz!")
    print("Çıkmak için 'çıkış' yazın.")
    print("-" * 50)

    while True:
        user_message = input("Siz: ")
        if user_message.lower() in ["çıkış", "exit", "quit"]:
            print("Asistan: Görüşmek üzere! Hoşça kalın.")
            break
        
        # This line simulates the message being sent to and processed by
        # the third-party AI assistant, just as it would happen if integrated
        # with a messaging platform like WhatsApp.
        assistant_reply = ai_assistant_response(user_message)
        print(f"Asistan: {assistant_reply}")

if __name__ == "__main__":
    main()
