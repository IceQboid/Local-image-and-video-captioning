# Local Image/Video Captioner



## Installation
1. **Get Ollama**:
    - Install Ollama to locally host models and abstract away model handling: https://ollama.com/download
    - Run the Ollama app
    - Pull LLaVa model
    ```bash
    ollama pull llava
    ```

2. **Create a virtual environment**:
    ```bash
    conda create -n projectname python=3.10
    conda activate projectname  
    ```

3. **Install dependencies**:
    ```bash
    pip install gradio pillow opencv-python requests
    ```

    
## Usage
1. **Ollama CLI**:
    - To use the model for image captioning in terminal, Run:
    ```bash
    ollama run llava
    ```
   After pulling the llava model initially.
1.1 Then at the prompt, include the path to your image in the prompt:
   
   ```bash
   What's in this image? `/Users/jmorgan/Desktop/smile.png`
   ```
   
    OR
   
    In our case, to get the desired output format use:

     ```bash
    Give a title, 2 or 3 sentences of description and at least 3 features to at most 5 features for this image `image_path`
     ```

3. **Interface**:
    - To use the model for both image or video captioning through Interface, Run:
    ```bash
    python main.py
    ```
    - Make sure Ollama desktop app is running in the background. 
    - Upload either photo or video and submit to get the output. 



4. **Example Outputs**:
   - CLI:
     ![output1_CLI](https://github.com/user-attachments/assets/882577f1-64ba-4e55-a20c-56c8974abb1c)
     ![output2_CLI](https://github.com/user-attachments/assets/497286de-68b7-4d29-81b1-7ea9e2a72b88)
   - Interface:
     ![output1_UI](https://github.com/user-attachments/assets/80f3c844-cacb-418d-8bef-05184a24bf87)
     ![output2_UI](https://github.com/user-attachments/assets/74b93373-bac1-4d35-b207-289a72f110d1)
     ![video_output](https://github.com/user-attachments/assets/71cb6a6a-8cc1-4f1c-8548-98db70f7c51b)
     
     

