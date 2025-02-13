import yt_dlp

def baixar_playlist(url_playlist, caminho_destino='.'):
    try:
        # Configurações do yt-dlp
        ydl_opts = {
            'format': 'bestvideo[height<=720]+bestaudio/best[height<=720]',  # Prioriza até 720p
            'outtmpl': f'{caminho_destino}/%(title)s.%(ext)s',  # Nome dos arquivos
            'merge_output_format': 'mp4',  # Formato final (vídeo + áudio)
            'ignoreerrors': True,  # Ignorar erros ao baixar vídeos individuais
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"Baixando playlist: {url_playlist}")
            ydl.download([url_playlist])
            print("Download concluído!")
    except Exception as e:
        print(f"Erro ao baixar a playlist: {e}")

# Exemplo de uso
if __name__ == "__main__":
    url_playlist = input("Insira a URL da playlist do YouTube: ")
    caminho_destino = input("Insira o caminho de destino (pressione Enter para usar o diretório atual): ") or '.'
    
    baixar_playlist(url_playlist, caminho_destino)