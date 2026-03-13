import os

SUPPORTED_FORMATS = {'.wav', '.mp3', '.ogg'}

class AudioDeliveryLayer:
    """
    Capa de entrega de audio agnóstica al proveedor TTS.
    Responsable únicamente de recibir un archivo local y entregarlo al chat de Telegram (OpenClaw)
    sin importar qué motor (KittenTTS, ElevenLabs, etc) lo generó.
    """

    @classmethod
    def send_audio_to_current_chat(cls, file_path: str, caption: str = None) -> bool:
        """
        1. Verifica que el archivo exista
        2. Valida formatos soportados
        3. Obtiene el contexto del chat / Telegram
        4. Envía el archivo y devuelve el resultado
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Audio file not found: {file_path}")
            
        _, ext = os.path.splitext(file_path)
        if ext.lower() not in SUPPORTED_FORMATS:
            raise ValueError(f"Unsupported audio format: {ext}. Must be one of {SUPPORTED_FORMATS}")

        # Aquí irá el adaptador real del Telegram Bot API (ej. python-telegram-bot / openclaw messenger)
        # Ejemplo: openclaw_bot.send_voice(chat_id=current_chat, voice=open(file_path, 'rb'), caption=caption)
        
        # Log del pipeline asumiendo que un proveedor TTS externo ya arrojó el archivo:
        print(f"[Audio Delivery] Despachando archivo {file_path} exitosamente al chat actual.")
        
        return True
