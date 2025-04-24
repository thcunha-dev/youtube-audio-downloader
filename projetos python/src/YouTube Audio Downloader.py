from pytubefix import YouTube
from pathlib import Path
import sys

# Configurações personalizadas para seu ambiente
BASE_DIR = Path(r"C:\Users\Taros\Desktop\projetos python")
FFMPEG_PATH = r"C:\Program Files\ffmpeg\bin\ffmpeg.exe"  # Mantenha se necessário
AUDIO_DIR = BASE_DIR / "audios"

def baixar_audio(url):
    """
    Baixa áudio de vídeos do YouTube e converte para MP3
    Retorna o caminho completo do arquivo ou None em caso de erro
    """
    try:
        yt = YouTube(url)
        
        # Pega a melhor qualidade de áudio disponível
        audio_stream = yt.streams.filter(only_audio=True).order_by('abr').last()
        
        # Cria diretório se não existir
        AUDIO_DIR.mkdir(exist_ok=True)
        
        # Baixa e converte para MP3
        caminho_temp = audio_stream.download(output_path=str(AUDIO_DIR))
        caminho_mp3 = Path(caminho_temp).with_suffix('.mp3')
        Path(caminho_temp).rename(caminho_mp3)
        
        return str(caminho_mp3.resolve())
        
    except Exception as e:
        print(f"\n❌ Erro durante o download: {str(e)}")
        return None

def main():
    print("\n" + "="*50)
    print(" 🎧 YouTube para MP3 - by Taros ")
    print("="*50)
    
    url = input("\n🔗 Cole a URL do vídeo: ").strip()
    
    if (caminho := baixar_audio(url)):
        print(f"\n✅ Download concluído!\n📂 Arquivo salvo em:\n{caminho}")
    else:
        print("\n⚠️ Não foi possível completar o download")
    
    input("\nPressione Enter para sair...")

if __name__ == "__main__":
    main()