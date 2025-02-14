import yt_dlp
import os
import re

def limpar_nome(nome):
    """
    Remove caracteres inválidos para nomes de arquivos/diretórios.
    """
    return re.sub(r'[<>:"/\\|?*]', '', nome)

def baixar_playlist_ou_video(url):
    try:
        # Diretório base
        base_dir = './_downloads'

        # Extrair informações do conteúdo (playlist ou vídeo)
        with yt_dlp.YoutubeDL() as ydl:
            info = ydl.extract_info(url, download=False)

        # Verificar se é uma playlist ou um vídeo individual
        if 'entries' in info:  # É uma playlist
            playlist_title = info.get('title', 'Playlist sem título')
            playlist_url = url
            video_list = [entry['title'] for entry in info['entries'] if entry is not None]
            is_playlist = True
        else:  # É um vídeo individual
            playlist_title = "Videos"
            playlist_url = url
            video_list = [info['title']]
            is_playlist = False

        # Limpar o nome da playlist/vídeo para uso como nome de diretório
        cleaned_title = limpar_nome(playlist_title)

        # Verificar se o nome é muito longo
        if len(cleaned_title) > 50:
            print(f"O nome da playlist/vídeo é muito longo: {cleaned_title}")
            suggested_name = cleaned_title[:50]  # Sugerir os primeiros 50 caracteres
            new_name = input(f"Deseja usar este nome sugerido? [{suggested_name}] (ENTER para aceitar ou digite outro): ")
            cleaned_title = new_name.strip() or suggested_name

        # Construir o caminho de destino
        caminho_destino = os.path.join(base_dir, cleaned_title)

        # Limpar o terminal
        os.system('cls' if os.name == 'nt' else 'clear')

        # Exibir mensagem de confirmação
        print(f"Os arquivos serão criados em: {caminho_destino}")
        input("Pressione ENTER para continuar...")

        # Criar o diretório de destino
        os.makedirs(caminho_destino, exist_ok=True)
        print(f"Diretório criado: {caminho_destino}")

        # Configurações do yt-dlp
        ydl_opts = {
            'format': 'bestvideo[height<=1080]+bestaudio/best[height<=1080]',  # Prioriza até 1080p
            'outtmpl': f'{caminho_destino}/%(playlist_index)02d - %(title)s.%(ext)s' if is_playlist else f'{caminho_destino}/%(title)s.%(ext)s',
            'merge_output_format': 'mp4',  # Formato final (vídeo + áudio)
            'ignoreerrors': True,  # Ignorar erros ao baixar vídeos individuais
        }

        # Baixar os vídeos
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            if is_playlist:
                print(f"Baixando playlist: {playlist_title}")
            else:
                print(f"Baixando vídeo: {video_list[0]}")
            ydl.download([url])
            print("Download concluído!")

        # Criar o arquivo README.md se for playlist
        if is_playlist:
            readme_path = os.path.join(caminho_destino, 'README.md')
            with open(readme_path, 'w', encoding='utf-8') as readme_file:
                readme_file.write(f"# Informações do Conteúdo\n\n")
                readme_file.write(f"**Nome da Playlist:** {playlist_title}\n\n")
                readme_file.write(f"**Link da Playlist:** [{playlist_url}]({playlist_url})\n\n")
                readme_file.write(f"**Vídeos Baixados:**\n\n")
                for i, video_title in enumerate(video_list, start=1):
                    readme_file.write(f"{i}. {video_title}\n")

            print(f"Arquivo README.md criado em: {readme_path}")

    except Exception as e:
        print(f"Erro ao baixar o conteúdo: {e}")

if __name__ == "__main__":
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        url = input("Insira a URL do YouTube (playlist ou vídeo): ")
        baixar_playlist_ou_video(url)

        if input("Deseja baixar outro conteúdo? (s/n): ").lower() != 's':
            os.system('cls' if os.name == 'nt' else 'clear')
            break