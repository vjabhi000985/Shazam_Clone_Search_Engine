import gradio as gr
import numpy as np
import json
import assemblyai as aai
from sentence_transformers import SentenceTransformer
import chromadb
import zipfile
import os

# Loading the environment variables
api_key = os.environ.get("ASSEMBLYAI_API_KEY")

# Initialize AssemblyAI API key from environment variables.
aai.settings.api_key = api_key

# Unzip the db folder.
db_zip_path = os.path.join(".", "db.zip") 
db_extract_path = os.path.join(".", "db_extracted")

if os.path.exists(db_zip_path):
    os.makedirs(db_extract_path, exist_ok=True)  # create the folder if it does not exist.
    with zipfile.ZipFile(db_zip_path, 'r') as zip_ref:
        zip_ref.extractall(db_extract_path)
    print(f"db.zip extracted to: {db_extract_path}")

# ChromaDB Setup configurations
client = chromadb.PersistentClient(path=db_extract_path)
collection = client.get_or_create_collection(name="subtitle_chunks")

def transcribe_audio(audio_file):
    """Transcribes audio from the given file using AssemblyAI."""
    if audio_file is None:
        return "Please upload an audio file.", None

    config = aai.TranscriptionConfig(language_code="en")
    transcriber = aai.Transcriber(config=config)
    transcript = transcriber.transcribe(audio_file)

    return transcript.text, transcript.text

def format_results_as_json(results):
    """Formats subtitle search results into a JSON string."""
    formatted_results = []
    if results and results["metadatas"] and results["metadatas"][0]:
        for i, metadata in enumerate(results["metadatas"][0]):
            subtitle_name = metadata["subtitle_name"]
            subtitle_id = metadata["subtitle_id"]
            url = f"https://www.opensubtitles.org/en/subtitles/{subtitle_id}"
            formatted_results.append({
                "Result": i + 1,
                "Subtitle Name": subtitle_name.upper(),
                "URL": url,
            })
        return json.dumps(formatted_results, indent=4)
    else:
        return json.dumps([{"Result": "No results found"}], indent=4)

def retrieve_and_display_results(query):
    """Retrieves and displays subtitle search results based on the given query."""
    if not query:
        return "No transcription text available for search."

    model = SentenceTransformer("all-MiniLM-L6-v2")
    query_embedding = model.encode([query], show_progress_bar=False).tolist()
    results = collection.query(query_embeddings=query_embedding, n_results=5, include=["metadatas"])

    return format_results_as_json(results)

def clear_all():
    """Clears the transcribed text and search results."""
    return "", ""

# Gradio Interface with Styling
custom_css = """
    .gradio-container { width: 90% !important; margin: auto; }
    button { padding: 10px; border-radius: 5px; cursor: pointer; transition: opacity 0.3s; }
    .transcribe-btn { background-color: green; color: white; }
    .transcribe-btn:hover { opacity: 0.8; }
    .search-btn { background-color: blue; color: white; }
    .search-btn:hover { opacity: 0.8; }
    .clear-btn { background-color: #ff4500; color: white; }
    .clear-btn:hover { opacity: 0.8; }
"""

with gr.Blocks(css=custom_css) as demo:
    gr.Markdown("# 🎵 Shazam Clone : Audio Transcription & Subtitle Search", elem_id="title")
    text_state = gr.State(value="")

    with gr.Row():
        audio_input = gr.Audio(type="filepath", label="Upload Audio")
        transcribed_text = gr.Textbox(label="Transcribed Text", interactive=False)

    with gr.Row():
        transcribe_button = gr.Button("Transcribe", elem_classes=["transcribe-btn"])
        search_button = gr.Button("Search Subtitles", elem_classes=["search-btn"])
        clear_button = gr.Button("Clear", elem_classes=["clear-btn"])

    search_results = gr.Textbox(label="Subtitle Search Results")

    # Button Click Actions
    transcribe_button.click(transcribe_audio, inputs=[audio_input], outputs=[transcribed_text, text_state])
    search_button.click(retrieve_and_display_results, inputs=[text_state], outputs=[search_results])
    clear_button.click(clear_all, inputs=[], outputs=[transcribed_text, search_results])

# Launch App
demo.launch()