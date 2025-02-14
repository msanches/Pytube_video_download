# YouTube Playlist & Video Downloader
![Python](https://img.shields.io/badge/Python-3.x-blue) ![License](https://img.shields.io/badge/License-MIT-green)

Este é um script Python que permite baixar todos os vídeos de uma playlist do YouTube ou vídeos individuais em alta qualidade (até 1080p). Os arquivos são salvos em uma pasta organizada com um índice numérico no início do nome para facilitar a organização.

## 📋 Funcionalidades

- Baixa todos os vídeos de uma playlist do YouTube ou vídeos individuais.
- Força o download em até 1080p (ou outra resolução configurada).
- Cria automaticamente uma pasta com o nome da playlist (ou um nome limpo) dentro de `_downloads`.
- Adiciona um índice numérico ao início do nome do arquivo para melhor organização.
- Ignora erros ao baixar vídeos individuais, garantindo que a playlist seja processada completamente.
- Gera automaticamente um arquivo `README.md` no diretório de destino com informações sobre a playlist ou o vídeo baixado.
- Permite renomear a pasta caso o nome seja muito longo ou contenha caracteres especiais.

## 🛠️ Requisitos

- Python 3.x
- Biblioteca `yt-dlp`

### Instalação das Dependências

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/youtube-playlist-downloader.git
   cd youtube-playlist-downloader
   ```

2. Instale as dependências usando o arquivo `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

   > **Nota**: O arquivo `requirements.txt` contém todas as bibliotecas necessárias para o projeto. Certifique-se de ter o `pip` instalado no seu sistema.

### Conteúdo do `requirements.txt`
```txt
yt-dlp
```

## 🚀 Como Usar

1. Execute o script Python:
   ```bash
   python main.py
   ```

2. Insira a URL do YouTube (playlist ou vídeo):
   ```
   Insira a URL do YouTube (playlist ou vídeo): https://www.youtube.com/playlist?list=XXXXXXXXXXX
   ```

3. O script criará automaticamente uma pasta com o nome da playlist (ou um nome limpo) dentro de `_downloads`. Se o nome for muito longo, você poderá renomeá-lo.

4. Aguarde o download ser concluído. Os vídeos serão salvos no formato:
   ```
   01 - Título do Vídeo.mp4
   02 - Outro Título do Vídeo.mp4
   ```

5. Um arquivo `README.md` será gerado no diretório de destino com informações sobre a playlist ou o vídeo baixado.

## 📂 Estrutura do Projeto

```
youtube-playlist-downloader/
├── main.py                # Script principal para baixar playlists ou vídeos
├── requirements.txt       # Lista de dependências do projeto
└── README.md              # Documentação do projeto
```

## ⚙️ Configurações Avançadas

### Alterar Resolução
Você pode alterar a resolução máxima dos vídeos modificando o campo `format` no arquivo `main.py`. Por exemplo:

- Para forçar 720p:
  ```python
  'format': 'bestvideo[height<=720]+bestaudio/best[height<=720]'
  ```

- Para forçar 480p:
  ```python
  'format': 'bestvideo[height<=480]+bestaudio/best[height<=480]'
  ```

### Adicionar Legendas
Se desejar baixar legendas junto com os vídeos, adicione as seguintes opções ao dicionário `ydl_opts`:
```python
'subtitleslangs': ['en', 'pt'],  # Idiomas das legendas
'writeautomaticsub': True,      # Baixar legendas automáticas
```

## 📜 Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE). Você pode usá-lo, modificá-lo e distribuí-lo conforme necessário. 😊🚀