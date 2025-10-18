from flask import Flask, render_template, request, jsonify, send_file
import os
import uuid
import yt_dlp

app = Flask(__name__)

DOWNLOAD_FOLDER = "downloads"
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    data = request.get_json()
    url = data.get('url')

    try:
        # Identificador único
        uid = str(uuid.uuid4())
        temp_folder = os.path.join(DOWNLOAD_FOLDER, uid)
        os.makedirs(temp_folder, exist_ok=True)

        # Configuración de yt_dlp
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': os.path.join(temp_folder, '%(title)s.%(ext)s'),
            'quiet': True,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'noplaylist': True,  # solo un video, no listas
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            title = info.get('title', 'audio')
            mp3_path = os.path.join(temp_folder, f"{title}.mp3")

        # Mover el archivo final a downloads/
        final_path = os.path.join(DOWNLOAD_FOLDER, f"{title}.mp3")
        os.replace(mp3_path, final_path)

        # Limpiar carpeta temporal
        os.rmdir(temp_folder)

        return jsonify({
            "success": True,
            "download": f"/download/{os.path.basename(final_path)}",
            "filename": f"{title}.mp3"
        })

    except Exception as e:
        return jsonify({"success": False, "error": str(e)})

@app.route('/download/<filename>')
def download(filename):
    return send_file(os.path.join(DOWNLOAD_FOLDER, filename), as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
